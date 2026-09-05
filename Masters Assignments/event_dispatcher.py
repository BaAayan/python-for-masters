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

