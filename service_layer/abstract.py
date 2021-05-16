from pydantic import BaseModel
from datetime import date, datetime
from uuid import uuid4, UUID
from domain.model import Shipment, Order, OrderDetail, Sku, Batch, OrderLine
from pydantic.color import Color
from typing import Optional

class AddShipment(BaseModel):
    item: str
    quantity: int
    purchase_date: date
    received_date: date
    address: str
    contact: str
    sku_id: str
    batch_ref: str


class UpdateShipment(BaseModel):
    item: Optional[str]=None
    quantity: Optional[int]=None
    purchase_date: Optional[date]=None
    received_date: Optional[date]=None
    address: Optional[str]=None
    contact: Optional[str]=None
    sku_id: Optional[str]=None
    batch_ref: Optional[str]=None


class UpdateShipmentBatch(BaseModel):
    batch_ref: str


class UpdateShipmentQuantity(BaseModel):
    quantity: int


class AddOrder(BaseModel):
    order_id: uuid4
    customer_id: uuid4
    item: str
    amount: float
    quantity: int
    shipperId: uuid4
    shipping_address: str
    order_address: str
    order_email: str
    order_date: date
    order_status: bool
    timestamp: datetime
    paymentDate: datetime
    payementId: UUID
    paid: bool


class UpdateOrderItem(BaseModel):
    item: str


class UpdateOrderAmount(BaseModel):
    amount: float


class UpdateOrderQuantity(BaseModel):
    quantity: str


class AddOrderDetail(BaseModel):
    order_id: UUID
    product_id: str
    sku_id: str
    price: float
    quantity: int
    tax: float
    discount: float
    total: float
    shipdate: date
    billdate: date



class UpdateOrderDetailQuantity(BaseModel):
    quantity: int


class AddSku(BaseModel):
    brand: str
    size: str
    color: Color
    product: str


class UpdateSkuProduct(BaseModel):
    product: str


class AddBatch(BaseModel):
    sku: str
    batch_ref: str
    quantity: int
    manufacture_date: date
    expire_date: date


class AddOrderLine(BaseModel):
    sku: str
    quatity: int
    order_id: str


class UpdateBatchQuantity(BaseModel):
    quantity: int
