from datetime import date, timedelta
from pytest
from model import allocate, Batch, OrderLine, OutOfStock

today = date.today()
tommorrow = today+timedelta(days=1)
later = tommorrow+timedelta(days=10)


def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK",
                           100, manufacture_date=None)
    shipment_batch = Batch("shipment-batch", "RETRO-clock",
                           100, manufacture_date=tommorrow)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    allocate(line, [in_stock_batch, shipment_batch])
    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100


def test_returns_allocated_batch_ref():
    in_stock_batch = Batch("in-stock-batch-ref",
                           "HIGHBROW-POSTER", 100, manufacture_date=None)
    shipment_batch = Batch("shipment-batch-ref",
                           "HIGHBROW-POSTER", 100, manufacture_date=tommorrow)
    line = OrderLine("oref", "HIGHBROW-POSTER", 10)
    allocation = allocate(line, [in_stock_batch, shipment_batch])
    assert allocation == in_stock_batch.reference


def test_raises_out_of_stock_exception_if_cannot_allocate():
    batch = Batch("batch1", "SMALL-FORK", 10, manufacture_date=today)
    allocate(OrderLine("order1", "SMALL-FORK", 10), [batch])

    with pytest.raises(OutOfStock, match="SMALL-FORK"):
        allocate(OrderLine("order2", "SMALL-FORK", 1), [batch])
