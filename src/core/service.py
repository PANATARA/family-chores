from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from typing import Any


class BaseService(metaclass=ABCMeta):

    def __call__(self) -> Any:
        self.validate()
        return self.execute()

    def get_validators(self) -> list[Callable]:
        return []

    def validate(self) -> None:
        validators = self.get_validators()
        for validator in validators:
            validator()

    @abstractmethod
    def execute(self) -> Any:
        raise NotImplementedError("Please implement in the service class")