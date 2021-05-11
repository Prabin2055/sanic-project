"""
1.The UoW acts as a single entrypoint to our persistent storage, and it keeps track of what objects were loaded 
and of the latest state.

2.A stable snapshot of the database to work with, so the objects we use aren’t changing halfway through an operation

3..A way to persist all of our changes at once, so if something goes wrong, we don’t end up in an inconsistent state

4..A simple API to our persistence concerns and a handy place to get a repository
"""

from __future__ import annotations
import abc
from source.adapters import repository


class AbstractUnitOfWork(abc.ABC):
    # which will give us access to the model repository.
    model: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    # call this method to explicitly commit our work when we are ready.
    def commit(self):
        raise NotImplementedError

    def rollback(self):  # we don’t commit, or if we exit the context manager by raising an error, we do a rollback
        raise NotImplementedError


class ShipmentUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.model = ShipmentRepository([])
        self.committed = False

    def __enter__(self):
        self.model = repository.ShipmentRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.close()

    def commit(self):
        self.committed = True

    def rollback(self):
        pass
