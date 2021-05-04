from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship
from pydantic.Color import color
from source.domain import model
from email import Email
from bool import Boolean
from datetime import date, datetime

metadata = MetaData()

shipment = Table(
    "shipments",
    metadata,
    Column("id_", Integer, primary_key=True, autoincrement=True),
    Column("item", String(255)),
    Column("quantity", Integer),
    Column("purchase_date", Date, nullable=True),
    Column("received_date", Date, nullable=True),
    Column("address", String(255)),
    Column("contact", String(255)),
    Column("sku_id", String(255)),
    Column("batch_ref", String(255)),

)

orders = Table(
    "orders",
    metadata,
    Column("order_id", Integer, primary_key=True),
    Column("customer_id", ForeignKey("user.username")),
    Column("amount", float()),
    Column("quantity", Integer()),
    Column("shipperId", Integer()),
    Column("order_address", String(255)),
    Column("order_email", Email()),
    Column("order_date", Date()),
    Column("order_status", Boolean()),
    Column("timestamp", datetime()),
    Column("paymentDate", datetime()),
    Column("paymentId", Integer, primary_key=True),
    Column("payentId", ForeignKey("payments.id")),
    Column("paid", Boolean()),

)

orderdetail = Table(
    "orderdetails",
    metadata,
    Column("id_", Integer, primary_key=True),
    Column("order_id", ForeignKey("orders.id")),
    Column("product_id", ForeignKey("products.id")),
    Column("sku_id", ForeignKey("skues.id")),
    Column("price", float()),
    Column("quantity", Integer()),
    Column("tax", float()),
    Column("discount", float()),
    Column("total", float()),
    Column("shipdate", Date()),
    Column("billdate", datetime()),

)


sku = Table(
    "skues",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("brand", String(255)),
    Column("size", String(30)),
    Column("color", color),
    Column("product", ForeignKey("products.name")),

)


batches = Table(
    "batches",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("batch_ref", String(255)),
    Column("sku", ForeignKey("skues.id")),
    Column("quantity", Integer, nullable=False),
    Column("manufacture_date", Date, nullable=True),
    Column("expire_date", Date, nullable=True),

)

order_lines = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", ForeignKey("skues.id")),
    Column("quantity", Integer, nullable=False),
    Column("order_id", ForeignKey("orders.id")),

)

allocations = Table(
    "allocations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("orderline_id", ForeignKey("order_lines.id")),

)


def start_mapper = mapper(models.OrderLine, order_lines)


mapper(
    models.Batch,
    batches,
    properties={
        "_allocations": relationship(
            lines_mapper, secondary=allocations, collection_class=set,
        )
    }
)
