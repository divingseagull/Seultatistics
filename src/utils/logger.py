import sys
import datetime
from enum import Enum


class LogLevel(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Event(Enum):
    ON_READY = "on_ready",
    ON_COMMAND = "on_command",
    ON_MESSAGE = "on_message",
    ON_ERROR = "on_error"


class Logger:
    def __init__(self, configs: dict, encoding: str = "utf-8"):
        self.log_config = configs
        self.log_config["encoding"] = encoding

        filename = datetime.datetime.now().strftime(self.log_config['filename'])
        self.filename = f"{self.log_config['path']}/{filename}"

    def write(self, message: str, log_level: LogLevel, event: Event | None = None):
        if self.log_config["logging"]:
            if (event is None) or \
                    (event.value in [on_event for (on_event, value) in self.log_config["on_events"].items() if value]):
                timestamp = datetime.datetime.now().strftime(self.log_config['timestamp'])
                with open(self.filename, "a", encoding=self.log_config["encoding"]) as log_io:
                    sys.stdout = log_io
                    sys.stdout.write(f"[{log_level.value}][{timestamp}]: {message}\n")

    def read(self, start: int, stop: int) -> list[str]:
        pass
