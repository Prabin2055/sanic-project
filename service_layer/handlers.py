import command
from source.domain.model import Shipment, Order, OrderDetail, Sku, Batch, OrderLine
from source.service_layer.commmand import (AddShipment, AddOrder, AddOrderDetail, AddBatch, AddOrderLine, AddSku, UpdateShipment, BatchCommand, UpdateBatchQuantity,
                    ShipmentCommand, UpdateShipmentBatch, UpdateShipmentQuantity)

from source.domain.model import shipment_factory, order_detail_factory,  sku_factory, batch_factory, orderline_factory, order_factory


async def add_shipment(cmd: AddShipment) -> model.Shipment:
    return model.shipment_factory(
        item=cmd.item,
        quantity=cmd.quantity,
        purchase_date=cmd.purchase_date,
        received_date=cmd.received_date,
        address=cmd.address,
        contact=cmd.contact,
        sku_id=cmd.sku_id,
        batch_ref=cmd.batch_ref

    )


async def update_shipment(cmd: command.ShipmentCommand) -> model.Shipment:
    if isinstance(cmd, UpdateShipmentBatch):
        return cmd.shipment.update({
            'batch_ref': cmd.batch_ref
        })
    elif isinstance(cmd, UpdateShipmentQuantity):
        return cmd.shipment.update({
            'quantity': cmd.quantity
        })


async def add_order(cmd: AddOrder) -> model.Order:
    return model.order_factory(
        customer_id=cmd.customer_id,
        item=cmd.item,
        amount=cmd.amount,
        quantity=cmd.quantity,
        shipperId=cmd.shipperId,
        shipping_address=cmd.shipping_address,
        order_address=cmd.order_address,
        order_email=cmd.order_email,
        order_date=cmd.order_date,
        order_status=cmd.order_status,
        timestamp=cmd.timestamp,
        payementId=cmd.payementId,
        paymentDate=cmd.paymentDate,
        paid=cmd.paid
    )


async def add_order_detail(cmd: AddOrderDetail) -> model.OrderDetail:
    return model.order_detail_factory(
        order_id=cmd.order_id,
        product_id=cmd.product_id,
        sku_id=cmd.sku_id,
        price=cmd.price,
        quantity=cmd.quantity,
        tax=cmd.tax,
        discount=cmd.discount,
        total=cmd.total,
        shipdate=cmd.shipdate,
        billdate=cmd.billdate
    )


async def add_sku(cmd: AddSku) -> model.Sku:
    return Model.sku_factory(
        sku_id=cmd.sku_id,
        brand=cmd.brand,
        size=cmd.size,
        color=cmd.color,
        product=cmd.product
    )


async def add_batch(cmd: AddBatch) -> model.Batch:
    return model.batch_factory
        sku = cmd.sku,
        batch_ref = cmd.batch_ref,
        quantity = cmd.quantity,
        manufacture_date = cmd.manufacture_date,
        expire_date = cmd.expire_date,
    )  # pass factory argu


async def update_batch(cmd: BatchCommand) -> model.Batch:
    if isinstance(cmd, UpdateBatchQuantity):
        return cmd.batch.update({
            'quantity': cmd.quantity
        })
    # elif isinstance(cmd, UpdateSku):
    #     return cmd.batch.update({
    #         'sku': cmd.sku
    #     })



async def add_orderline(cmd: AddOrderLine) -> model.OrderLine:
    return model.orderline_factory(
        sku = cmd.sku,
        quantity = cmd.quantity,
        order_id = cmd.order_id
    )
