from source.domain import model
from source.adapters import repository
from source.service_layer import service


def test_returns_allocation():
    batch = model.Batch("batch1", "Lamp", 100, manufacture_date=None)
    repo = repository.BatchRepository([batch])

    result = service.allocate("01", "Lamp", 10, repo)
    assert result == "batch1"


def test_allocate_returns_allocation():
    repo = repository.BatchRepository([])
    service.add_batch("batch1", "Lamp", 100, None, None, repo)
    result = service.allocate("01", "Lamp", 10, repo)
    assert result == "batch1"


def test_allocate_errors_for_invalid_sku():
    repo = repository.BatchRepository([])
    service.add_batch("b1", "ASKU", 100, None, None, repo)
    with pytest.raises(service.InvalidSku, match="Invalid sku NonExistentSKU"):
        service.allocate("01", "NonExistentSKU", 10, repo)
