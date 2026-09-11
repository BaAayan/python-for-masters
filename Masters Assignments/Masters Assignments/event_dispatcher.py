class EventDispatcher:
    def __init__(self):
        self._subscribers = {}  # event_type -> ordered list of callbacks

    def subscribe(self, event_type: str, callback: callable):
        self._subscribers.setdefault(event_type, []).append(callback)

    def unsubscribe(self, event_type: str, callback: callable):
        callbacks = self._subscribers.get(event_type, [])
        if callback in callbacks:
            callbacks.remove(callback)

    def dispatch(self, event_type: str, *args, **kwargs):
        for callback in self._subscribers.get(event_type, []):
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"Error in callback for event '{event_type}': {e}")

# --- callbacks testing code ---
def on_login(username):
    print(f"Welcome, {username}!")

def log_login(username):
    print(f"[LOG] {username} logged in")


dispatcher = EventDispatcher()
dispatcher.subscribe("login", on_login)
dispatcher.subscribe("login", log_login)

# --- simple menu loop for manual testing ---
while True:
    print("\n1. Dispatch 'login' event")
    print("2. Unsubscribe log_login")
    print("3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter a username: ")
        dispatcher.dispatch("login", username)
    elif choice == "2":
        dispatcher.unsubscribe("login", log_login)
        print("log_login unsubscribed.")
    elif choice == "3":
        break
    else:
        print("Invalid option, try again.")