from sanic import Sanic
from sanic import response
from sanic.response import text, json
from domain.model import Shipment, Order, OrderLine, Sku, Batch
from datetime import date, datetime
from sanic.response import HTTPResponse
from service_layer import service, unit_of_work
from service_layer import abstract
from pydantic import HttpUrl


app = Sanic(__name__)

sku_list = [{
    'sku_id': 101,
    'brand': 'dell',
    'size': 'small',
    'color': 'black',
    'product': 'laptop'
}, {
    'sku_id': 102,
    'brand': 'apple',
    'size': 'mini',
    'color': 'white',
    'product': 'laptop'
}]

batch_list = [{
    'id': 100,
    'sku': 'Lp-Dl-SM-Bl',
    'batch_ref': 'batch-001',
    'quantity': 500,
    'manufacture_date': "2021-04-10T00:00",
    'expire_date': "2028-01-01T00:00"

}, {
    'id': 100,
    'sku': 'Lp-AP-MN-WH',
    'batch_ref': 'batch-002',
    'quantity': 400,
    'manufacture_date': "2021-02-10T00:00",
    'expire_date': "2040-01-01T00:00"
}]

shipment_list = [{
    # insert shipment value

}]
order_list = [{
    # insert order value manually

}]
order_detail_list = [{
    # insert order_detail manually

}]


@app.get("/")
async def hello_world(request):
    return text("hello,  Prabin How are you??")


@app.route("/shipment", methods=['GET', 'POST'])
def add_shipment(request):
    service.add_shipment(validated_data=abstract.AddShipment(
        item="laptop",
        quantity=10,
        purchase_date="2020-01-02",
        received_date="2020-01-09",
        address="kapan",
        contact="9837484949",
        sku_id="L-D-B-i7",
        batch_ref="01"

    ), uow=unit_of_work.ShipmentUnitOfWork)
    return HTTPResponse("sucessfully added")




@app.get("/batch")
async def get_batches(request):
    new_batch = list()
    for i in range(len(batch_list)):
        try:
            batch_with_id = batch_list[i]
            batch = Batch(**batch_with_id)
            batch.manufacture_date = default(batch.manufacture_date)
            batch.expire_date = default(batch.expire_date)
            new_batch.append(batch.dict())
        except Exception as e:
            return json(e)
    return json(new_batch)


@app.get("/batch/<id:int>")
async def get_batches_by_id(request, id: int):
    for i in range(len(batch_list)+1):
        try:
            if batch_list[i]['id'] == id:
                batch_with_id = batch_list[i]
                batch = Batch(**batch_with_id)
                batch.manufacture_date = default(batch.manufacture_date)
                batch.expire_date = default(batch.expire_date)
                return json(batch.dict())

        except Exception as e:
            return json(e)


@app.get("/sku")
async def get_sku(request):
    new_sku = list()
    for i in range(len(sku_list)):
        try:
            sku_with_id = sku_list[i]
            sku = Sku(**sku_with_id)
            sku.brand = default(sku.brand)
            sku.product = default(sku.product)
            new_sku.append(sku.dict())
        except Exception as e:
            return json(e)
    return json(new_sku)


@app.get("/sku/<id:int>")
async def get_sku_by_id(request, id: int):
    for i in range(len(sku_list)+1):
        try:
            if sku_list[i]['id'] == id:
                sku_with_id == sku_list
                sku = Sku(**sku_with_id)
                sku.brand = default(sku.brand)
                sku.product = default(sku.product)
                return json(sku.dict())
        except Exception as e:
            return json(e)


if __name__ == "__main__":
    app.run(auto_reload=True, debug=True, workers=4)
