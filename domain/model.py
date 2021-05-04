from pydantic import BaseModel, validator
from datetime import Optional, date, datetime
from email import email
from typing import Optional
from uuid import UUID
from pydantic.color import Color
from pydantic.float import float
"""
1. product is identified bya a sku
2. customers place order, order  is identified by an order reference
3. a batch of stock has a unique id called a reference , sku, quantity
4. allocate order line to batch-> send stock from specific batch to the customers delivery address
5.shipment Batch


Notifies about shipment
Notifies about orders
Asks for stock levels
send instructions to warehouse

"""


class Shipment(BaseModel):
    id_: UUID
    item: str
    quantity: int
    purchase_date: date
    received_date: date
    address: str
    contact: str
    sku_id: str
    batch_ref: str

    class Config:
        # whether or not models are faux-immutable, i.e. whether __setattr__ is allowed (default: True)
        allow_mutation = False
        extra = "forbid"  # forbid extra attributes during model initialization
        title = 'Shipment'

    def update(self, mapping: typing.Dict[str, typing.Any]) -> Shipment:
        return self.copy(update=mapping)


def shipment_factory(
    id_: UUID,
    item: str,
    quantity: int,
    purchase_date: date,
    received_date: date,
    address: str,
    contact: str,
    sku_id: str,
    batch_ref: str,
) -> Shipment:
 return Shipment(
     id_=Id_,
     item=item,
     quantity=quantity,
     purchase_date=purchase_date,
     received_date=received_date,
     address=address,
     contact=contact,
     sku_id=sku_id,
     batch_ref=batch_ref,
)


class Order(BaseModel):
    order_id: UUID
    customer_id: UUID
    item: str
    amount: float
    quantity: int
    shipperId: UUID
    shipping_address: str
    order_address: str
    order_email: email
    order_date: date
    order_status: bool
    timestamp: datetime
    paymentDate: datetime
    payementId: UUID
    paid: bool

    class Config:
        allow_mutation = False
        extra = "forbid"
        title = "Order"

    def update(self, mapping: typing.Dict[str, typing.Any]) -> Order:
        return self.copy(update=mapping)

    def add_order(self, channel: ChannelReference) -> User:
        channels = set(self.channels)
        channels.add(channel)
        return self.copy(update={"channels": tuple[ChannelReference]})

    def add_channels(self, channels: typing.Tuple[ChannelReference]) -> User:
        _channels = set(self.channels) | channels
        return self.copy(update={"channnels": tuple(_channels)})

def order_factory(
     id_: UUID,
     customer_id: UUID,
     item: str
     amount: float,
     quantity: int,
     shipperId: UUID,
     shipping_address: str,
     order_address: str,
     order_email: email,
     order_date: date,
     order_status: bool,
     timestamp: datetime,
     paymentDate: datetime,
     payementId: UUID,
     paid: bool, 
     ) -> Order:
    return Order(
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
        paid=paid,

    )


class OrderDetail(BaseModel):
    id_: UUID
    order_id: UUID
    product_id: str
    sku_id: str
    price: float
    quantity: int
    tax: float
    discount: float
    total: float
    shipdate: date
    billdate: datetime

    class Config:
        allow_mutation = False
        extra = 'forbid' 
        title='OrderDetail'

    def update(self, mapping: typing.Dict[str, typing.Any]) -> OrderDetail:
        return self.copy(update=mapping)

def order_detail_factory(
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
    ) -> OrderDetail:
    return OrderDetail(
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
        billdate=billdate,
    )

            

    

class Sku(BaseModel):
    """
    sku_id, brand, size, color, product
    """
    sku_id: UUID
    brand: str
    size: str
    color: Color
    product: str

    class Config:
        allow_mutation = False
        extra = "forbid"
        title="Sku"


    def update(self, mapping: typing.Dict[str, typing.Any]) -> Sku:
        return self.copy(update=mapping)

    @validator('sku_id')
    def check_sku_id_not_empty(cls, v):
        for skuid in v:
            assert skuid != '', 'Empty strings are not allowed.'
        return v


def sku_factory(
    sku_id: UUID,
    brand: str,
    size: str,
    color: str,
    product: str,
    ) -> Sku:
    return(
        sku_id=sku_id,
        brand=brand,
        size=size,
        color=color,
        product=product,
    )


class Batch(BaseModel):
    """
    batchid,
     quantity, 
     eta(date),
     sku,

    """
    id_: uuid4()
    sku: str
    batch_ref: str
    quantity: int
    manufacture_date: date
    expire_date = date

    class Config:
        allow_mutation = False
        extra = 'forbid'
        title="Batch"

    def update(self, mapping: typing.Dict[str, typing.Any]) -> Batch:
        return self.copy(update=mapping)

    @validator("manufacture_date")
    def manufacture_within_three_years(cls, manufacture_date):
        if not abs(time_in_delta.days) <= 3*365:
            raise ValueError(
                "must be manufacture not exceeding three years from now")
        return manufacture_date

    

def batch_factory(
    id_: UUID,
    sku: str,
    batch_ref: str,
    quantity: int,
    manufacture_date: date,
    expire_date: date,
    ) -> Batch:
    return Batch(
        id_=id_,
        sku=sku,
        batch_ref=batch_ref,
        quantity=quantity,
        manufacture_date=manufacture_date,
        expire_date=expire_date,
     )

   


class OrderLine(BaseModel):
    """
    order_id,
    pruduct_name,
    batch_num
    sku,
    quantity

    """
    id_: UUID  # order_id = order-123
    sku: str
    quantity: int
    order_id: str

    class Config:
        allow_mutation = False
        extra = "forbid"
        title="OrderLine"

    def update(self, mapping: typing.Dict[str, typing.Any]) -> OrderLine:
        return self.copy(update=mapping)

def orderline_factory(
    id_: UUID,
    sku: str,
    quantity: int,
    order_id: UUID,
    ) -> OrderLine:
    return OrderLine(
        id_=id_,
        sku=sku,
        quantity=quantity,
        order_id=order_id,

    )