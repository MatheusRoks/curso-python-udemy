from abc import ABC, abstractmethod


@abstractmethod
class Log(ABC):
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')
