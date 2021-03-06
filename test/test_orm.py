import model
from datetime import date


def test_orderline_mapper_can_load_lines(session):
    session.execute(
        "INSERT INTO order_lines(orderid, sku,quantity) VALUES"
        '("order1", "RED-CHAIR"12),'
        '("order1", "RED-TABLE",13),'
        '("order2", "BLUE-LIPSTICK",14)'

    )
    expected = [
        model.OrderLine("order1", "RED-CHAIR", 12),
        model.OrderLine("order1", "RED-TABLE", 13),
        model.OrderLine("order2", "BLUE-LIPSTICK", 14),

    ]
    assert session.query(model.OrderLine).all() == expected


def test_orderline_mapper_can_save_lines(session):
    new_line = model.OrderLine("order1", "DECORATIVE-WIDGET", 12)
    session.add(new_line)
    session.commit()

    rows = list(session.execute(
        'SELECT orderid,sku, quantity FROM "order_lines"'))
    assert rows == [("order1", "DECORATIVE-WIDGET", 12)]


def test_retrieving_batches(session):
    session.execute(
        "INSERT INTO batches (reference, sku, _purchased_quantity, manufacture_date)"
        'VALUES("batch1", "sku1",100,null)'

    )
    session.execute(
        "INSERT INTO batches(reference, sku,_purchased_quantity, manufacture_date)"
        'VALUES ("batch2", "sku2", 200, "2021-04-11")'

    )
    expected = [
        model.Batch("batch1", "sku1", 100, manufacture_date=None),
        model.Batch("batch2", "sku2", 200, manufacture_date=date(2021, 4, 4)),

    ]
    assert session.query(model.Batch).all() == expected


def test_saving_batches(session):
    batch = model.Batch[("batch1", "sku1", 100, None)]
    session.add(batch)
    session.commit()
    rows = session.execute(
        'SELECT reference, sku, _purchased_quantity, manufacture_date from "batches"'
    )
    assert list(rows) == [("batch1", "sku1", 100, None)]


def test_saving_allocations(session):
    batch = model.Batch("batch1", "sku1", 100, manufacture_date=None)
    line = model.OrderLine("order1", "sku1", 10)
    batch.allocate(line)
    session.add(batch)
    session.commit()
    rows = list(session.execute(
        'SELECT orderline_id, batch_id FROM "allocations"'))
    assert rows == [(batch.id, line.id)]


def test_retrieving_allocations(session):
    session.execute(
        'INSERT INTO order_lines (orderid, sku,quantity') VALUES("order1", "sku1", 12)

    )
    [[olid]]=session.execute(
        "SELECT id FROM order_lines WHERE orderid=:orderid AND skw=:sku",
        dict(orderid="order1", sku="sku1"),

    )
    session.execute(
        "INSERT INTO batches(reference, sku, _purchased_quantity, manufacture_date)"
        'VALUES("batch1","sku1",100,null)'

    )
    [[bid]]=session.execute(
        "SELECT id FROM batches WHERE reference=:ref AND sku=:sku",
        dict(ref="batch1", sku="sku1"),

    )
    session.execute(
        "INSERT INTO allocations(orderline_id,batch_id) VALUES(:olid,:bid)",
        dict(olid=olid, bid=bid),
    )
    batch=session.query(model.Batch).one()

    assert batch._allocations == {model.OrderLine("order1", "sku1", 12)}
