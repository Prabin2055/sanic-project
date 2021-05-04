import command
from source.domain.model import Shipment, Order, OrderDetail, Sku, Batch, OrderLine
from source.service_layer.commmand import AddShipment, AddOrder, AddOrderDetail, AddBatch, AddOrderLine, AddSku, UpdateShipment
from source.domain.model import shipment_factory, order_detail_factory,  sku_factory, batch_factory, orderline_factory, order_factory


async def add_shipment(cmd: command.AddShipment) -> model.Shipment:
    return model.shipment_factory(
        id_=Id_,
        item=item,
        quantity=quantity,
        purchase_date=purchase_date,
        received_date=received_date,
        address=address,
        contact=contact,
        sku_id=sku_id,
        batch_ref=batch_ref

    )


async def update_shipment(cmd: command.UpdateShipment) -> model.Shipment:
    return model.shipment_factory(
        id_=Id_,
        item=item,
        quantity=quantity,
        purchase_date=purchase_date,
        received_date=received_date,
        address=address,
        contact=contact,
        sku_id=sku_id,
        batch_ref=batch_ref

    )

        # async def Shipment:
        # if isinstance(cmd:command.AddShipment) -> model.Shipment:
        #     return model.shipment_factory(#pass factory argument)
        # elif isinstance(cmd:command.UpdateShipment) ->model.Shipment:
        #     return model.shipment_factory( )
          
async def add_order(cmd: command.AddOrder) -> model.Order:
    return model.order_factory(
        id_=id_,
        customer_id=customer_id,
        item=item,
        amount=amount,
        quantity=quantity,
        shipperId=shipperId,
        shipping_address=shipping_address,
        order_address=order_address,
        order_email=order_email,
        order_date=order_date,
        order_status=order_status,
        timestamp=timestamp,
        payementId=payementId,
        paymentDate=paymentDate,
        paid=paid
    )


async def add_order_detail(cmd: command.AddOrderDetail) -> model.OrderDetail:
    return model.order_detail_factory(
        id_=id_,
        order_id=order_id,
        product_id=product_id,
        sku_id=sku_id,
        price=price,
        quantity=quantity,
        tax=tax,
        discount=discount,
        total=total,
        shipdate=shipdate,
        billdate=billdate
    )


async def add_sku(cmd: command.AddSku) -> model.Sku:
    return Model.sku_factory(
        sku_id=sku_id,
        brand=brand,
        size=size,
        color=color,
        product=product
    )


async def add_batch(cmd: command.AddBatch) -> model.Batch:
    return model.batch_factory(
        id_=id_,
        sku=sku,
        batch_ref=batch_ref,
        quantity=quantity,
        manufacture_date=manufacture_date,
        expire_date=expire_date,
    )  # pass factory argu


async def add_orderline(cmd: command.AddOrderLine) -> model.OrderLine:
    return model.orderline_factory(
        id_=id_,
        sku=sku,
        quantity=quantity,
        order_id=order_id
    )
