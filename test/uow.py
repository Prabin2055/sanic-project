

def test_add_batch():
    uow = FakeUnitOfWork()  # (3)
    services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, uow)  # (3)
    assert uow.batches.get("b1") is not None
    assert uow.committed


def test_allocate_returns_allocation():
    uow = FakeUnitOfWork()  # (3)
    services.add_batch("batch1", "COMPLICATED-LAMP", 100, None, uow)  # (3)
    result = services.allocate("o1", "COMPLICATED-LAMP", 10, uow)  # (3)
    assert result == "batch1"


#  Reallocate service function
def realllocate(
    line: OrderLine,
    uow: AbstractUnitOfWork,
) -> str:
    with uow:
        bacth = uow.batches.get(ske=line.sku)
        if batch is None:
            raise InvalidSku('invalid sku{line.sku}')
        batches.deallocate(line)
        allocate(line)
        uow.commit()
