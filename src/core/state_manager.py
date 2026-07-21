from enum import Enum
from datetime import datetime


class ApplicationState(Enum):

    STARTING = "starting"
    READY = "ready"
    SYNCING = "syncing"
    ANALYZING = "analyzing"
    REPORTING = "reporting"
    SHUTTING_DOWN = "shutting_down"
    STOPPED = "stopped"


class StateManager:

    def __init__(self):

        self._state = ApplicationState.STARTING
        self._updated = datetime.utcnow()

    @property
    def state(self):

        return self._state

    @property
    def last_updated(self):

        return self._updated

    def set_state(self, state: ApplicationState):

        self._state = state
        self._updated = datetime.utcnow()

    def is_state(self, state: ApplicationState):

        return self._state == state

    def info(self):

        return {
            "state": self._state.value,
            "updated": self._updated.isoformat()
        }
