import abc
from domain import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    async def get(self, id_=None):
        raise NotImplementedError

    @abc.abstractmethod
    async def add(self, model=None):
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self,id_=None, model=None) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self,id_=None, model=None):
        raise NotImplementedError
