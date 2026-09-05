import time

def rate_limit(max_calls: int, period: int):
    def decorator(func):
        calls = []
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove timestamps older than the period window
            calls = [t for t in calls if now - t < period]
            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, period=10)
def fetch_user_data(user_id):
    return f"Data for {user_id}"

print(fetch_user_data(1))