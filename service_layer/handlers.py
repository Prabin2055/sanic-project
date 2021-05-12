from domain import command
from domain import model


async def add_shipment(cmd:command.AddShipment) -> model.Shipment:
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
    if isinstance(cmd, command.UpdateShipmentBatch):
        return cmd.shipment.update({
            'batch_ref': cmd.batch_ref
        })
    elif isinstance(cmd,command.UpdateShipmentQuantity):
        return cmd.shipment.update({
            'quantity': cmd.quantity
        })

# async def delete_shipment(cmd:command.DeleteOrder)->model.Shipment:


async def add_order(cmd: command.AddOrder) -> model.Order:
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


async def update_order(cmd: command.OrderCommand) -> model.Order:
    if isinstance(cmd, command.UpdateOrderItem):
        return cmd.order.update({
            'item': cmd.item
        })
    elif isinstance(cmd, command.UpdateOrderQuantity):
        return cmd.order.update({
            'quantity': cmd.quantity
        })
    elif isinstance(cmd, command.UpdateOrderAmount):
        return cmd.order.update({
            'amount': cmd.amount
        })


async def add_order_detail(cmd: command.AddOrderDetail) -> model.OrderDetail:
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


async def update_order_detail(cmd: command.OrderDetailCommand) -> model.OrderDetail:
    if isinstance(cmd, command.UpdateOrderDetailQuantity):
        return cmd.order_detail.update({
            'quantity': cmd.quantity
        })


async def add_sku(cmd: command.AddSku) -> model.Sku:
    return sku_factory(
        sku_id=cmd.sku_id,
        brand=cmd.brand,
        size=cmd.size,
        color=cmd.color,
        product=cmd.product
    )


async def update_sku(cmd: command.SkuCommand) -> model.Sku:
    if isinstance(cmd, command.UpdateSkuProduct):
        return cmd.sku.update({
            'product': cmd.product
        })


async def add_batch(cmd: command.AddBatch) -> model.Batch:
    return model.batch_factory(
        sku = cmd.sku,
        batch_ref = cmd.batch_ref,
        quantity = cmd.quantity,
        manufacture_date = cmd.manufacture_date,
        expire_date = cmd.expire_date,
    )  # pass factory argu


async def update_batch(cmd: command.BatchCommand) -> model.Batch:
    if isinstance(cmd, command.UpdateBatchQuantity):
        return cmd.batch.update({
            'quantity': cmd.quantity
        })




async def add_order_line(cmd: command.AddOrderLine) -> model.OrderLine:
    return model.orderline_factory(
        sku = cmd.sku,
        quantity = cmd.quantity,
        order_id = cmd.order_id
    )
