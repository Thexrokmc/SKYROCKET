from dataclasses import dataclass
from typing import Callable, List
import time


@dataclass
class PipelineStep:
    name: str
    action: Callable


class Pipeline:

    def __init__(self, logger):

        self.logger = logger
        self.steps: List[PipelineStep] = []

    def add_step(self, name: str, action: Callable):

        self.steps.append(

            PipelineStep(

                name=name,

                action=action

            )

        )

    def run(self):

        self.logger.info("Pipeline started.")

        start = time.perf_counter()

        for step in self.steps:

            self.logger.info(

                "Running step: %s",

                step.name

            )

            step.action()

        elapsed = time.perf_counter() - start

        self.logger.info(

            "Pipeline completed in %.2f seconds.",

            elapsed

        )
