from __future__ import annotations
import abc
from adapters import abstract_repository


class AbstractUnitOfWork(abc.ABC):
    # which will give us access to the model repository.
    # model: repository.AbstractRepository
    repo: abstract_repository.AbstractRepository

    @abc.abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    # The __enter__() returns the resource that needs to be managed
    @abc.abstractmethod
    def __enter__(self) -> AbstractUnitOfWork:
        raise NotImplementedError

    # he __exit__() does not return anything but performs the cleanup operations.
    @abc.abstractmethod
    def __exit__(self, *args):
        self.rollback()

    # call this method to explicitly commit our work when we are ready.
    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):  # we don’t commit, or if we exit the context manager by raising an error, we do a rollback
        raise NotImplementedError
