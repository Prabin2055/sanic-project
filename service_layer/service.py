"""
Typical service-layer functions have similar steps:

1.We fetch some objects from the repository.

W2.e make some checks or assertions about the request against the current state of the world.

3.We call a domain service.

4.If all is well, we save/update any state we’ve changed.

"""
from __future__ import annotations
from os import O_TMPFILE
from service_layer.abstract import AddBatch, AddOrder, AddShipment, AddSku, AddOrderDetail, AddOrderLine, UpdateShipment
from typing import Optional
from datetime import date
from uuid import UUID
from domain import model
from service_layer import handlers, unit_of_work
from domain import command
from service_layer import abstract
from adapters.repository import BatchRepository, OrderRepository, OrderdDetailRepository, OrderLineRepository, SkuRepository, ShipmentRepository
import asyncio

async def add_shipment(
    # call abstract.py
    validated_data: abstract.AddShipment, uow: unit_of_work.ShipmentUnitOfWork
) -> None:
    with uow()as w:
        shipment = await handlers.add_shipment(command.AddShipment(
            item=validated_data.item,
            quantity=validated_data.quantity,
            purchase_date=validated_data.purchase_date,
            received_date=validated_data.received_date,
            address=validated_data.address,
            contact=validated_data.contact,
            sku_id=validated_data.sku_id,
            batch_ref=validated_data.batch_ref

        ))
        # repo = ShipmentRepository()
        # repo.add(shipment)
        # uow.commit()
        # w.storedata.append(shipment)
        w.storedata=shipment
        w.commit()


async def update_shipment(id_: UUID, validated_data: abstract.UpdateShipment, uow: unit_of_work.ShipmentUnitOfWork) -> None:
    with uow:
        repo = ShipmentRepository()
        shipment = repo.get(id_)
        # await asyncio.sleep(2)
        # print("Responce from repo", shipment, type(shipment), validated_data)
        shipment_data = await asyncio.wait( handlers.update_shipment(command.UpdateShipment(
            shipment=shipment,
            item=validated_data.item if validated_data.item else shipment.item,
            quantity=validated_data.quantity if validated_data.quantity else shipment.quantity,
            purchase_date=validated_data.purchase_date if validated_data.purchase_date else shipment.purchase_date,
            received_date=validated_data.received_date if validated_data.received_date else shipment.received_date,
            address=validated_data.address if validated_data.address else shipment.address,
            contact=validated_data.contact if validated_data.contact else shipment.contact,
            sku_id=validated_data.sku_id if validated_data.sku_id else shipment.sku_id,
            batch_ref=validated_data.batch_ref if validated_data.batch_ref else shipment.batch_ref

        )))
        repo.update(id_, shipment_data)
        uow.commit()
    

async def update_shipment_batch(id_: UUID, validated_data: abstract.UpdateShipmentBatch):
    repo = ShipmentRepository()
    shipment_ = repo.get(id_)
    shipment = handlers.update_shipment(command.UpdateShipmentBatch(
        shipment=shipment_, batch_ref=validated_data.batch_ref
    ))
    repo.update(shipment)


async def update_shipment_quantity(id_: UUID, validated_data: abstract.UpdateShipmentQuantity):
    repo = ShipmentRepository()
    shipment = repo.get(id_)
    shipment = handlers.update_shipment(command.UpdateShipmentQuantity(
        shipment=shipment, quantity=validated_data.quantity
    ))
    repo.update(shipment)

# def delete_shipment(id_:UUID, validated_data:abstract.ShipmentAbstract):
#     repo = ShipmentRepository()
#     shipment = repo.get(id_)
#     shipment=handlers.delete_shipment(command.ShipmentCommand(validated_data.ShipmentCommand))
#     repo.delete(shipment)

async def add_order(
    validated_data: AddOrder
) -> None:
    order = handlers.add_order(command.AddOrder(
        order_id=validated_data.order_id,
        customer_id=validated_data.customer_id,
        item=validated_data.item,
        amount=validated_data.amount,
        quantity=validated_data.quantity,
        shipperId=validated_data.shipperId,
        shipping_address=validated_data.shipping_address,
        order_address=validated_data.order_address,
        order_email=validated_data.order_email,
        order_date=validated_data.order_date,
        order_status=validated_data.order_status,
        timestamp=validated_data.timestamp,
        paymentDate=validated_data.paymentDate,
        payementId=validated_data.payementId,
        paid=validated_data.paid
    ))
    repo = OrderRepository()
    repo.add(order)


async def update_order_item(id_: UUID, validated_data: abstract.UpdateOrderItem):
    repo = OrderRepository()
    order = repo.get(id_)
    order = handlers.update_order(command.UpdateOrderItem(
        order=order, item=validated_data.item
    ))
    repo.update(order)


async def update_order_quantity(id_: UUID, validated_data: abstract.UpdateOrderQuantity):
    repo = OrderRepository()
    order = repo.get(id_)
    order = handlers.update_order(command.UpdateOrderQuantity(
        order=order, quantity=validated_data.quantity
    ))
    repo.update(order)


async def update_order_amount(id_: UUID, validated_data: abstract.UpdateOrderAmount):
    repo = OrderRepository()
    order = repo.get(id_)
    order = handlers.update_order(command.UpdateOrderAmount(
        order=order, amount=validated_data.amount
    ))
    repo.update(order)


def add_orderdetail(
    validated_data: AddOrderDetail
) -> None:
    order_detail = handlers.add_order_detail(command.AddOrderDetail(
        order_id=validated_data.order_id,
        product_id=validated_data.product_id,
        sku_id=validated_data.sku_id,
        price=validated_data.price,
        quantity=validated_data.quantity,
        tax=validated_data.tax,
        discount=validated_data.discount,
        total=validated_data.total,
        shipdate=validated_data.shipdate,
        billdate=validated_data.billdate
    ))
    repo = OrderdDetailRepository()
    repo.add(order_detail)


def update_order_detail(id_: UUID, validated_data: abstract.OrderDetailCommand):
    repo = OrderdDetailRepository()
    order_detail = repo.get(id_)
    order_detail = handlers.update_order_detail(command.UpdateOrderDetailQuantity(
        order_detail=order_detail, quantity=validated_data.quantity
    ))
    repo.update(order_detail)


def add_sku(
    validated_data: AddSku
) -> None:
    sku = handlers.add_sku(command.AddSku(
        brand=validated_data.brand,
        size=validated_data.size,
        color=validated_data.color,
        product=validated_data.product
    ))
    repo = SkuRepository()
    repo.add(sku)


def update_sku(id_: UUID, validated_data: abstract.UpdateSkuProduct):
    repo = SkuRepository()
    sku = repo.get(id_)
    sku = handlers.update_sku(command.UpdateSkuProduct(
        sku=sku, product=validated_data.product
    ))
    repo.update(sku)


def add_batch(
    validated_data: AddBatch  # from call abstract.py
) -> None:
    batch = handlers.add_batch(command.AddBatch(
        sku=validated_data.sku,
        batch_ref=validated_data.batch_ref,
        quantity=validated_data.quantity,
        manufacture_date=validated_data.manufacture_date,
        expire_date=validated_data.expire_date
    ))   #
    repo = BatchRepository()  # replace batchrepo to batchUow
    repo.add(batch)


def update_batch_quantity(id_: UUID, validated_data: abstract.UpdateBatchQuantity):
    repo = BatchRepository()  # store 10 batch -> 4batch
    batch = repo.get(id_)
    batch = handlers.update_batch(command.UpdateBatchQuantity(
        batch=batch, quantity=validated_data.quantity
    ))
    repo.update(batch)


def add_order_line(
    validated_data: AddOrderLine  # from call abstract.py
) -> None:
    order_line = handlers.add_order_line(command.AddOrderLine(
        sku=validated_data.sku,
        quantity=validated_data.quantity,
        order_id=validated_data.order_id
    ))  # call handlers.py
    repo = OrderLineRepository()  # call repository.py
    repo.add(order_line)  # add repository method eg add


# unit of work

# def add_batch(
#     sku: str, batch_ref: str, quantity: int, manufacture_date: date, expire_date: date,
#     uow: unit_of_work.BatchUnitOfWork
# ):
#     with uow:
#         uow.batch_ref.add(model.Batch(
#             sku, batch_ref, quantity, manufacture_date, expire_date))
#         uow.commit()


# def allocate(
#     orderid: str, sku: str, qty: int,
#     uow: unit_of_work.AbstractUnitOfWork,
# ) -> str:
#     line = OrderLine(orderid, sku, qty)
#     with uow:
#         product = uow.products.get(sku=line.sku)
#         if product is None:
#             raise InvalidSku(f"Invalid sku {line.sku}")
#         try:
#             batchref = product.allocate(line)
#             uow.commit()
#             return batchref
#         except model.OutOfStock:
#             email.send_mail("stock@made.com", f"Out of stock for {line.sku}")
#             raise

async def add_shipment(
    validated_data: abstract.AddShipment,
    uow: unit_of_work.ShipmentUnitOfWork,
) -> str:
    with uow:
        shipment = await handlers.add_shipment(command.AddShipment(
            item=validated_data.item,
            quantity=validated_data.quantity,
            purchase_date=validated_data.purchase_date,
            received_date=validated_data.received_date,
            address=validated_data.address,
            contact=validated_data.contact,
            sku_id=validated_data.sku_id,
            batch_ref=validated_data.batch_ref

        ))
        repo = ShipmentRepository()
        repo.add(shipment)
        uow.commit()
