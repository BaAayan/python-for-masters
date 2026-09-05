import time

def rate_limit(max_calls: int, period: int):
    def decorator(func):
        calls_by_instance = {}  # FIX (Bug 2): dictionary keyed per instance instead of one shared list,
                                 # so each instance gets its own independent call history

        def wrapper(*args, **kwargs):
            key = args[0] if args else None  # FIX (Bug 2): use the instance (self) as the key

            if key not in calls_by_instance:
                calls_by_instance[key] = []

            now = time.time()

            # Remove timestamps older than the period window
            # FIX (Bug 1): update the dict entry in place instead of doing
            # "calls = [t for t in calls ...]", which would make 'calls' a
            # local variable and cause an UnboundLocalError
            calls_by_instance[key] = [t for t in calls_by_instance[key] if now - t < period]

            if len(calls_by_instance[key]) >= max_calls:
                raise Exception("Rate limit exceeded")

            calls_by_instance[key].append(now)
            return func(*args, **kwargs)

        return wrapper
    return decorator

@rate_limit(max_calls=3, period=10)
def fetch_user_data(user_id):
    return f"Data for {user_id}"

print(fetch_user_data(1))
print(fetch_user_data(2))
print(fetch_user_data(3))