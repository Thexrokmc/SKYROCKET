import logging
from pathlib import Path


class SkyrocketLogger:

    def __init__(

        self,

        name="SKYROCKET",

        log_file="logs/skyrocket.log",

        level=logging.INFO

    ):

        Path(log_file).parent.mkdir(

            parents=True,

            exist_ok=True

        )

        self.logger = logging.getLogger(name)

        self.logger.setLevel(level)

        if not self.logger.handlers:

            formatter = logging.Formatter(

                "%(asctime)s | %(levelname)s | %(message)s"

            )

            file_handler = logging.FileHandler(log_file)

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

            self.logger.addHandler(console_handler)

    def info(self, message):

        self.logger.info(message)

    def warning(self, message):

        self.logger.warning(message)

    def error(self, message):

        self.logger.error(message)

    def debug(self, message):

        self.logger.debug(message)
