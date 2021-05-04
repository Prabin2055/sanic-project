import model
import abc
from source.domain.model import Order, OrderDetail, OrderLine, Sku, Shipment, Batch
from pydantic.dict import Dict
from .app import sku_list, batch_list


# abstartrepository is a port and  fake&sql repository is a adapter


# class AbstractRepository(abc.ABC):
#     @abc.abstractmethod
#     def add(self, batch: models.Batch):
#         raise NotImplementedError

#     @abc.abstractmethod
#     def get(self, batch_ref) -> models.Batch:
#         raise NotImplementedError


# class SqlAlchemyRepository(AbstractRepository):
#     def __init__(self, session):
#         self.session = session

#     def add(self, batch):
#         self.session.add(batch)

#     def get(self, batch_ref):
#         return self.session.query(models.Batch).filter_by(batch_ref=batch_ref).one()

#     def list(self):
#         return self.session.query(models.Batch).all()


# async def update_values(self: list[Dict], values: Dict):
#     for i in range(len(model)+1):
#         if model[i]["id_"] == values.id_:
#             model[i].update(values)
#         return model[i]


class ShipmentRepository:
    async def add_shipment(self, model: Shipment):
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
        await model.append(values)

    async def update_shipment(self, model: Shipment) -> None:
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
        for i in range(len(self)+1):
            if self[i]["id_"] == values.id_:
                await self[i].update(values)

    async def get_shipment(self, id_) -> Shipment:
        shipment = {}
        if id_ in shipment_list[id_]:
            shipment = shipment_list[id_]
        return Shipment.construct(shipment)

    # async def get_shipment(self, id_) -> Dict:
    #     return self.query(models.Shipment).filter_by(id_=id_).one()

    async def delete_shipment(self, model: Shipment) -> None:
        if self.id_ in model.id_:
            del model[id_]


class OrderRepository:
    async def add_order(self, model: Order):
        values = {
            "order_id": model.Id_,
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
        await model.append(values)

    async def update_order(self, model: Order) -> Order:
        values = {
            "order_id": model.Id_,
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
        for i in range(len(self)+1):
            if self[i]["id_"] == values.id_:
                await self[i].update(values)

    async def get_order(self, customer_id) -> Dict:
        return self.query(models.Order).filter_by(customer_id=customer_id).one()

    async def delete_order(self, model: Order) -> None:
        if self.id_ in model.id_:
            def model[id_]


class OrderdDetailRepository:
    async def add_order_detail(self, model: OrderDetail):
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
        await model.append(values)

    async def update_order_detail(self, model: OrderDetail) -> None:
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
        for i in range(len(self)+1):
            if self[i]["id_"] == values.id_:
                await self[i].update(values)

    async def get_order_detail(self, order_id) -> Dict:
        return self.query(models.OrderDetail).filter_by(order_id=order_id).one()

    async def delete_order_detail(self, model: OrderDetail) -> None:
        if self.id_ in model.id_:
            del model[id_]


class SkuRepository:
    async def add_sku(self, model: Sku):
        values = {
            "sku_id": model.sku_id,
            "brand": model.brand,
            "size": model.size,
            "color": model.color,
            "product": model.product,
        }
        await model.append(values)

    async def update_sku(self, model: Sku) -> Sku:
        values = {
            "sku_id": model.sku_id,
            "brand": model.brand,
            "size": model.size,
            "color": model.color,
            "product": model.product,
        }
        await model.update(values)

    async def get_sku(self, sku_id) -> Sku:
        sku = {}
        if sku_id in sku_list[sku_id]:
            sku = sku_list[sku_id]
        return Sku.construct(sku)

    async def delete_sku(self, model: Sku) -> None:
        if self.sku_id in model.sku_id:
            del model[sku_id]


class BatchRepository:
    async def add_batch(self, model: Batch):
        values = {
            "id_": model.id_,
            "sku": model.sku,
            "batch_ref": model.batch_ref,
            "quantity": model.quantity,
            "manufacture_date": model.manufacture_date,
            "expire_date": model.expire_date,
        }
        await model.append(values)

    async def update_batch(self, model: Batch) -> None:
        values = {
            "id_": model.id_,
            "sku": model.sku,
            "batch_ref": model.batch_ref,
            "quantity": model.quantity,
            "manufacture_date": model.manufacture_date,
            "expire_date": model.expire_date,
        }
        for i in range(len(self)+1):
            if self[i]["id_"] == values.id_:
                await self[i].update(values)

    async def get_batch(self, batch_ref) -> Batch:
        batch = {}
        if batch_ref in batch_list[batch_ref]:
            batch = batch_list[batch_ref]
        return Batch.construct(batch)

    async def delete_batch(self, model: Batch) -> None:
        if self.id_ in model.id_:
            del model[id_]

    async


class OrderLineRepository:
    async def add_order_line(self, model: OrderLine):
        values = {
            "id_": model.Id_,
            "sku": model.sku,
            "quantity": model.quantity,
            "order_id": model.order_id
        }
        await model.append(values)

    async def update_order_line(self, model: OrderLine) -> None:
        values = {
            "id_": model.Id_,
            "sku": model.sku,
            "quantity": model.quantity,
            "order_id": model.order_id
        }
        for i in range(len(self)+1):
            if self[i]["id_"] == values.id_:
                await self[i].update(values)

    async def get_order_line(self, id_) -> OrderLine:
        order_line = {}
        if id_ in order_line_list[id_]:
            order_line = order_line_list[id_]
        return OrderLine.construct(order_line)

    async def delete_order_line(self, model: OrderLine) -> None:
        if self.id_ in model.id_:
            del model[id_]
