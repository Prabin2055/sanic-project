"""
Typical service-layer functions have similar steps:

1.We fetch some objects from the repository.

W2.e make some checks or assertions about the request against the current state of the world.

3.We call a domain service.

4.If all is well, we save/update any state we’ve changed.
"""

from source.service_layer.abstract import AddBatch, AddOrder, AddSku, AddShipment, AddOrderDetail, AddOrderLine, UpdateShipment
from __future__ import annotations
from typing import Optional
from datetime import date
from source.domain import model
from source.domain.model import OrderLine, Order, OrderDetail
from source.adapters.repository import BatchRepository, OrderRepository, OrderdDetailRepository, OrderLineRepository, SkuRepository, ShipmentRepository
from handlers import add_shipment, add_order, add_order_detail, add_sku, add_batch, add_orderline


def add_shipment(
    validated_data: AddShipment  # call abstract.py
) -> None:
    shipment = handlers.add_shipment(command.AddShipment(
        item=validated_data.item,
        quantity=validated_data.quantity,
        purchase_date=validated_data.purchase_date,
        received_date=validated_data.received_date,
        address=validated_data.address,
        contact=validated_data.contact,
        sku_id=validated_data.sku_id,
        batch_ref=validated_data.batch_ref

    ))
    repo = ShipmentRepository
    repo.add_shipment(shipment)


def update_shipment(
    validated_data: UpdateShipment 
) -> None:
    shipment = handlers.update_shipment(command.UpdateShipment(
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
    repo.update_shipment(shipment)


def add_order(
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
    repo = OrderRepository
    repo.add_order(order)


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
    repo = OrderdDetailRepository
    repo.add_order_detail(order_detail)


def add_sku(
    validated_data: AddSku
) -> None:
    sku = handlers.add_sku(command.AddSku(
        brand=validated_data.brand,
        size=validated_data.size,
        color=validated_data.color,
        product=validated_data.product
    ))
    repo = SkuRepository
    repo.add_sku(sku)


def add_batch(
    validated_data: AddBatch  # call commmand.py
) -> None:
    batch = handlers.add_batch(command.AddBatch(
        sku=validated_data.sku,
        batch_ref=validated_data.batch_ref,
        quantity=validated_data.quantity,
        manufacture_date=validated_data.manufacture_date,
        expire_date=validated_data.expire_date
    ))   #
    repo = BatchRepository
    repo.add_batch(batch)


def add_orde_line(
    validated_data: AddOrderLine  # call command.py
) -> None:
    order_line = handlers.add_order_line(command.AddOrderLine(
        sku=validated_data.sku,
        quantity=validated_data.quantity,
        order_id=validated_data.order_id
    ))  # call handlers.py
    repo = OrderLineRepository  # call repository.py
    repo.add_order_line(order_line)  # add repository method eg add_order_line


def update_batch(
    id_: uuid4,
    sku: str,
    batch_ref: str,
    quantity: int,
    manufacture_date: date,
    expire_date: date,
    repo: BatchRepository
) -> None:
    repo.update(model.Batch(id_, sku, batch_ref, quantity, manufacture_date,
                            expire_date))
    model.commit()


def allocate(
    order_id: str, sku: str, quantity: int, repo: OrderLineRepository,  # session
) -> str:
    line = OrderLine(order_id, sku, quantity)
    batches = repo.list()
    if not is_valid_sku(line.sku, batches):
        raise InvalidSku("Invalid sku {line.sku}")
    batch_ref = model.allocate(line, batches)
    model.commit()  # session.commit()
    return batch_ref


class InvalidOrder(Exception):
    pass


def is_valid_order(item, orders):
    retu item in {b.item for b in orders}


def add_order(
    order_id: UUID,
    customer_id: UUID,
    item: str,
    amount: float,
    quantity: int,
    shipperId: UUID,
    shipping_address: str,
    order_address: str,
    order_email: email,
    order_date: date,
    order_status: bool,
    timestamp: ,
    paymentDate: datetime,
    payementId: UUID,
    paid: bool,
    repo: OrderRepository,
    # session,
) -> None:
    repo.add(model.Order(order_id, customer_id, item, amount, quantity, shipperId,
                         shipping_address, order_address, order_email, order_date, order_status,
                         timestamp, paymentDate, payementId, paid))
    model.commit()  # session.commit()


def update_order(
    order_id: UUID,
    customer_id: UUID,
    item: str,
    amount: float,
    quantity: int,
    shipperId: UUID,
    shipping_address: str,
    order_address: str,
    order_email: email,
    order_date: date,
    order_status: bool,
    timestamp: ,
    paymentDate: datetime,
    payementId: UUID,
    paid: bool,
    repo: OrderRepository,

) -> None:
    repo.update(model.Order(order_id, customer_id, item, amount, quantity, shipperId,
                            shipping_address, order_address, order_email, order_date, order_status,
                            timestamp, paymentDate, payementId, paid))
    model.commit()


def allocate_order(
    id_: UUID,
    order_id: UUID,
    product_id: str,
    sku_id: str,
    price: float,
    quantity: int,
    tax: float,
    discount: float,
    total: float,
    shipdate: date,
    billdate: datetime,
    repo: OrderdDetailRepository,
) -> str:
    order_detail = OrderDetail(order_id, product_id, sku_id, price,
                               quantity, tax, discount, total, shipdate, billdate)
    orders = repo.list()
    if not is_valid_order(order_detail.order_id, orders):
        raise InvalidOrder("Invalid order (order_detail.order_id}")
    order_id = model.allocate_order(order_detail, orders)
    model.commit()
    return order_id
