from pydantic import BaseModel
from datetime import date
from uuid import uuid4
from source.domain.model import Shipment, Order, OrderDetail, Sku, Batch, OrderLine


class AddShipment(BaseModel):
    item: str,
    quantity: int,
    purchase_date: date,
    received_date: date,
    address: str,
    contact: str,
    sku_id: str,
    batch_ref: str


class ShipmentAbstract(BaseModel):
    shipment: Shipment


class UpdateShipmentBatch(ShipmentAbstractBaseModel):
    batch_ref: str


class UpdateShipmentQuantity(ShipmentAbstractBaseModel):
    quantity: int


class AddOrder(BaseModel):
    order_id: uuid4,
    customer_id: uuid4,
    item: str,
    amount: float,
    quantity: int,
    shipperId: uuid4,
    shipping_address: str,
    order_address: str,
    order_email: email,
    order_date: date,
    order_status: bool,
    timestamp: datetime,
    paymentDate: datetime,
    payementId: UUID,
    paid: bool


class OrderAbstract(BaseModel):
    order: Order


class UpdateOrderItem(OrderAbstract):
    item: str


class UpdateOrderAmount(OrderAbstract):
    amount: float


class UpdateOrderQuantity(OrderAbstract):
    quantity: str


class AddOrderDetail(BaseModel):
    order_id: UUID,
    product_id: str,
    sku_id: str,
    price: float,
    quantity: int,
    tax: float,
    discount: float,
    total: float,
    shipdate: date,
    billdate: datetime


class OrderDetailAbstract(BaseModel):
    order_detail: OrderDetail


class UpdateOrderDetailQuantity(OrderDetailAbstract):
    quantity: int


class AddSku(BaseModel):
    brand: str,
    size: str,
    color: Color,
    product: str


class SkuAbstract(BaseModel):
    sku: Sku


class UpdateSkuProduct(SkuAbstract):
    product: str


class AddBatch(BaseModel):
    sku: str,
    batch_ref: str,
    quantity: int,
    manufacture_date: date,
    expire_date: date


class AddOrderLine(BaseModel):
    sku: str,
    quatity: int,
    order_id: str


class BatchAbstact(BaseModel):
    batch: Batch


class UpdateBatchQuantity(BatchAbstact):
    quantity: int
