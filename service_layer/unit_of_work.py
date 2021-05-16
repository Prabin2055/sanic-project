"""
1.The UoW acts as a single entrypoint to our persistent storage, and it keeps track of what objects were loaded 
and of the latest state.

2.A stable snapshot of the database to work with, so the objects we use aren’t changing halfway through an operation

3..A way to persist all of our changes at once, so if something goes wrong, we don’t end up in an inconsistent state

4..A simple API to our persistence concerns and a handy place to get a repository
"""

from __future__ import annotations
import abc
from adapters import repository
from service_layer.abstract_unit_of_work import AbstractUnitOfWork


class ShipmentUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.repo = repository.ShipmentRepository()

    def __enter__(self):
        self.storeData = []
        return self

    def __exit__(self, *args):
        return super().__exit__(*args)

    def commit(self):
        self.repo.add(self.storedata)

    def rollback(self):
        self.rollback


class UpdateShipmentUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.repo = repository.ShipmentRepository()

    def __enter__(self):
        self.id_=None
        self.storeDataUpdate = None
        return self

    def __exit__(self, *args):
        return super().__exit__(*args)

    def commit(self):
        self.repo.update(self.id_, self.storeDataUpdate)

    def rollback(self):
        self.rollback


class OrderUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.order = repository.OrderRepository()

    def __enter__(self):
        self.storedata = []
        return self

    def __exit__(self, *args):
        return super().__exit__(*args)

    def commit(self):
        self.order.add(self.storedata[0])

    def rollback(self):
        return super().rollback()


class SkuUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.sku = repository.SkuRepository()

    def __enter__(self):
        self.storedata = []
        return self

    def __exit__(self, *args):
        return super().__exit__(*args)

    def commit(self):
        self.sku.add(self.storedata[0])

    def rollback(self):
        return super().rollback()


class BatchUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.batch = repository.BatchRepository([])

    def __enter__(self):
        self.storedata = []
        return self

    def __exit__(self, *args):
        super().__exit__(*args)
        self.close()

    def commit(self):
        self.batch.add(self.storedata[0])

    def rollback(self):
        self.rollback()
