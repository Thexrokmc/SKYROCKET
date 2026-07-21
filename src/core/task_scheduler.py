import threading
import time
from dataclasses import dataclass
from typing import Callable


@dataclass
class ScheduledTask:
    name: str
    interval: int
    callback: Callable


class TaskScheduler:

    def __init__(self):

        self.tasks = []
        self.running = False
        self.thread = None

    def add_task(
        self,
        name: str,
        interval: int,
        callback: Callable
    ):

        self.tasks.append(
            ScheduledTask(
                name=name,
                interval=interval,
                callback=callback
            )
        )

    def _worker(self):

        last_run = {}

        while self.running:

            now = time.time()

            for task in self.tasks:

                if (
                    task.name not in last_run
                    or now - last_run[task.name] >= task.interval
                ):

                    try:
                        task.callback()
                    except Exception as e:
                        print(
                            f"Task '{task.name}' failed: {e}"
                        )

                    last_run[task.name] = now

            time.sleep(1)

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._worker,
            daemon=True
        )

        self.thread.start()

    def stop(self):

        self.running = False

        if self.thread:
            self.thread.join()

    def list_tasks(self):

        return [

            task.name

            for task in self.tasks

        ]
