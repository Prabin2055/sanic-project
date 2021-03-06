from domain.model import Order, OrderDetail, OrderLine, Sku, Shipment, Batch
from pydantic import Dict
from app import sku_list, batch_list
from uuid import UUID, uuid4
from adapters.abstract_repository import AbstractRepository
import os
import pickle

database = {}
i = 0

# abstartrepository is a port and  fake&sql repository is a adapter
# archive, active , inactive

# class AbstractRepository(abc.ABC):
#     @abc.abstractmethod
#     def add(self, batch: models.Batch):
#         raise NotImplementedError

#     @abc.abstractmethod
#     def get(self, batch_ref) -> models.Batch:
#         raise NotImplementedError


# class SqlAlchemyRepository(AbstractRepository)
#     def __init__(self, session):
#         self.session = session

#     def add(self, batch):
#         self.session.add(batch)

#     def get(self, batch_ref):
#         return self.session.query(models.Batch).filter_by(batch_ref=batch_ref).one()

#     def list(self):
#         return self.session.query(models.Batch).all()


class ShipmentRepository(AbstractRepository):
    async def get(self, id_: UUID) -> Shipment:
        data = database[id_]
        print("GET, data", data)
        shipment_data = Shipment(**data)
        return shipment_data

    async def add(self, model: Shipment) -> None:
        values = {
            "id_": model.Id_,
            "item": model.item,
            "quantity": model.quantity,
            "purchase_date": model.purchase_date,
            "received_date": model.received_date,
            "address": model.address,
            "contact": model.contact,
            "sku_id": model.sku_id,
            "batch_ref": model.batch_ref,

        }
        # await model.append(values)
        global i
        i += 1
        database[i] = values
        with open('database.pickle', 'wb') as handle:
            pickle.dump(database, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print(database)

    async def update(self, id_, model: Shipment) -> None:
        values = {
            "id_": model.Id_,
            "item": model.item,
            "quantity": model.quantity,
            "purchase_date": model.purchase_date,
            "received_date": model.received_date,
            "address": model.address,
            "contact": model.contact,
            "sku_id": model.sku_id,
            "batch_ref": model.batch_ref
        }
        database[id_] = values
        print(database)

    async def delete(self, id_, model: Shipment) -> None:
        if self.id_ in model.id_:
            del model[id_]


class OrderRepository(AbstractRepository):
    async def get(self, id_: UUID) -> Order:
        data = database[id_]
        print("GET, data", data)
        order_data = Order(**data)
        return order_data

    async def add(self, model: Order) -> None:
        values = {
            "order_id": model.order_id,
            "customer_id": model.customer_id,
            "item": model.item,
            "amount": model.amount,
            "quantity": model.quantity,
            "shipperId": model.shipperId,
            "shipping_address": model.shipping_address,
            "order_address": model.order_address,
            "order_email": model.order_email,
            "order_date": model.order_date,
            "order_status": model.order_status,
            "timestamp": model.timestamp,
            "paymentDate": model.paymentDate,
            "payementId": model.payementId,
            "paid": model.paid,
        }
        # await model.append(values)
        with open("file.json", "a+") as f:
            f.write(f'{values}\n')

    async def update(self, id_, model: Order) -> None:
        values = {
            "order_id": model.order_id,
            "customer_id": model.customer_id,
            "item": model.item,
            "amount": model.amount,
            "quantity": model.quantity,
            "shipperId": model.shipperId,
            "shipping_address": model.shipping_address,
            "order_address": model.order_address,
            "order_email": model.order_email,
            "order_date": model.order_date,
            "order_status": model.order_status,
            "timestamp": model.timestamp,
            "paymentDate": model.paymentDate,
            "payementId": model.payementId,
            "paid": model.paid

        }
        database[id_] = values
        print(database)

    # async def get(self, customer_id) -> Dict:
    #     return self.query(models.Order).filter_by(customer_id=customer_id).one()

    async def delete(self, id_, model: Shipment) -> None:
        if self.id_ in model.id_:
            del model[id_]


class OrderdDetailRepository(AbstractRepository):
    async def get(self, id_: UUID) -> OrderDetail:
        data = database[id_]
        print("GET, data", data)
        order_detail_data = OrderDetail(**data)
        return order_detail_data

    async def add(self, model: OrderDetail) -> None:
        values = {
            "id_": model.Id_,
            "order_id": model.order_id,
            "product_id": model.product_id,
            "sku_id": model.sku_id,
            "price": model.price,
            "quantity": model.quantity,
            "tax": model.tax,
            "discount": model.discount,
            "total": model.total,
            "shipdate": model.shipdate,
            "billdate": model.billdate,
        }
        # await model.append(values)
        with open("file.json", "a+") as f:
            f.write(f'{values}\n')

    async def update(self, id_, model: OrderDetail) -> None:
        values = {
            "id_": model.Id_,
            "order_id": model.order_id,
            "product_id": model.product_id,
            "sku_id": model.sku_id,
            "price": model.price,
            "quantity": model.quantity,
            "tax": model.tax,
            "discount": model.discount,
            "total": model.total,
            "shipdate": model.shipdate,
            "billdate": model.billdate,
        }
        database[id_] = values
        print(database)

    async def delete(self, id_, model: OrderDetail) -> None:
        if self.id_ in model.id_:
            del model[id_]


class SkuRepository(AbstractRepository):
    async def get(self, sku_id: UUID) -> Sku:
        data = database[sku_id]
        print("GET, data", data)
        sku_data = Sku(**data)
        return sku_data

    async def add(self, model: Sku) -> None:
        values = {
            "sku_id": model.sku_id,
            "brand": model.brand,
            "size": model.size,
            "color": model.color,
            "product": model.product,
        }
        # await model.append(values)
        with open("file.json", "a+") as f:
            f.write(f'{values}\n')

    async def update(self, sku_id, model: Sku) -> None:
        values = {
            "sku_id": model.sku_id,
            "brand": model.brand,
            "size": model.size,
            "color": model.color,
            "product": model.product,
        }
        database[sku_id] = values
        print(database)

    async def delete(self, sku_id, model: Sku) -> None:
        if self.sku_id in model.sku_id:
            del model[sku_id]


class BatchRepository(AbstractRepository):
    async def get(self, id_: UUID) -> Batch:
        data = database[id_]
        print("GET, data", data)
        batch_data = Batch(**data)
        return batch_data

    async def add(self, model: Batch):
        values = {
            "id_": model.id_,
            "sku": model.sku,
            "batch_ref": model.batch_ref,
            "quantity": model.quantity,
            "manufacture_date": model.manufacture_date,
            "expire_date": model.expire_date,
        }
        # await model.append(values)
        with open("file.json", "a+") as f:
            f.write(f'{values}\n')

    async def update(self, id_, model: Batch) -> None:
        values = {
            "id_": model.id_,
            "sku": model.sku,
            "batch_ref": model.batch_ref,
            "quantity": model.quantity,
            "manufacture_date": model.manufacture_date,
            "expire_date": model.expire_date,
        }
        database[id_] = values
        print(database)

    async def delete(self, id_, model: Batch) -> None:
        if self.id_ in model.id_:
            del model[id_]


class OrderLineRepository(AbstractRepository):
    async def get(self, id_: UUID) -> OrderLine:
        data = database[id_]
        print("GET, data", data)
        orderdata = OrderLine(**data)
        return orderdata

    async def add(self, model: OrderLine) -> None:
        values = {
            "id_": model.Id_,
            "sku": model.sku,
            "quantity": model.quantity,
            "order_id": model.order_id
        }
        # await model.append(values)
        with open("file.json", "a+") as f:
            f.write(f'{values}\n')

    async def update(self, id_, model: OrderLine) -> None:
        values = {
            "id_": model.Id_,
            "sku": model.sku,
            "quantity": model.quantity,
            "order_id": model.order_id
        }
        database[id_] = values
        print(database)

    async def delete(self, id_, model: OrderLine) -> None:
        if self.id_ in model.id_:
            del model[id_]
