from pydantic import BaseModel
from datetime import date
from source.domain.model import Batch, Shipment, Order, Sku, OrderDetail


class AddShipment(BaseModel):
    item: str,
    quantity: int,
    purchase_date: date,
    received_date: date,
    address: str,
    contact: str,
    sku_id: str,
    batch_ref: str


class ShipmentCommand(BaseModel):
    shipment = Shipment


class UpdateShipmentBatch(ShipmentCommand):
    batch_ref: str


class UpdateShipmentQuantity(ShipmentCommand):
    quantity: int


class AddOrder(BaseModel):
    order_id: UUID,
    customer_id: UUID,
    item: str,
    amount: float,
    quantity: int,
    shipperId: UUID,
    shipping_address: str,
    order_address: str
    order_email: email,
    order_date: date,
    order_status: bool,
    timestamp: datetime,
    paymentDate: datetime,
    payementId: UUID,
    paid: bool


class OrderCommand(BaseModel):
    order = Order


class UpdateOrderItem(OrderCommand):
    item = str


class UpdateOrderAmount(OrderCommand):
    amount: float


class UpdateOrderQuantity(OrderCommand):
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


class OrderDetailCommand(BaseModel):
    order_detail = OrderDetail


class UpdateOrderDetailQuantity(OrderDetailCommand):
    quantity: int


class AddSku(BaseModel):
    brand: str,
    size: str,
    color: Color,
    product: str


class SkuCommand(BaseModel):
    sku = Sku


class UpdateSkuProduct(SkuCommand):
    product: str


class AddBatch(BaseModel):
    sku: str,
    batch_ref: str,
    qunatity: int,
    manufactire_date: date,
    expire_date: date


class BatchCommand(BaseModel):
    batch = Batch


class UpdateBatchQuantity(BatchCommand):
    quantity: int

# class UpdateSku(BatchCommand):
#     sku:


class AddOrderLine(BaseModel):
    sku: str,
    quantity: int,
    order_id: str
