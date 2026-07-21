from collections import defaultdict
from typing import Callable, Any


class EventBus:
    """
    Simple publish/subscribe event bus.
    """

    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        callback: Callable[..., Any]
    ):

        if callback not in self._subscribers[event_name]:
            self._subscribers[event_name].append(callback)

    def unsubscribe(
        self,
        event_name: str,
        callback: Callable[..., Any]
    ):

        if callback in self._subscribers[event_name]:
            self._subscribers[event_name].remove(callback)

    def publish(
        self,
        event_name: str,
        **payload
    ):

        for callback in self._subscribers[event_name]:
            callback(**payload)

    def clear(self):

        self._subscribers.clear()

    def registered_events(self):

        return sorted(self._subscribers.keys())
