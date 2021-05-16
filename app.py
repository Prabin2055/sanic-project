from sanic import Sanic
from sanic import response
from sanic.response import text, json
from datetime import date, datetime
from sanic.response import HTTPResponse
from service_layer import service, unit_of_work
from service_layer import abstract
from pydantic import HttpUrl


app = Sanic(__name__)


@app.get("/")
async def hello_world(request):
    return text("hello,  Prabin How are you??")


@app.route("/shipment", methods=['GET', 'POST'])
def add_shipment(request):
    service.add_shipment(validated_data=abstract.AddShipment(
        item="lenovo",
        quantity=10,
        purchase_date="2020-01-02",
        received_date="2020-01-09",
        address="kapan",
        contact="9837484949",
        sku_id="L-D-B-i7",
        batch_ref="01"

    ), uow=unit_of_work.ShipmentUnitOfWork)
    return HTTPResponse("sucessfully added")


@app.route("/update_shipment", methods=['GET', 'POST'])
def update_shipment(request):
    service.update_shipment(id_=1, validated_data=abstract.UpdateShipment(
        item="dell",
        quantity=50

    ))
    return HTTPResponse("successfully Updated")

# @app.get("/batch")
# async def get_batches(request):
#     new_batch = list()
#     for i in range(len(batch_list)):
#         try:
#             batch_with_id = batch_list[i]
#             batch = Batch(**batch_with_id)
#             batch.manufacture_date = default(batch.manufacture_date)
#             batch.expire_date = default(batch.expire_date)
#             new_batch.append(batch.dict())
#         except Exception as e:
#             return json(e)
#     return json(new_batch)


# @app.get("/batch/<id:int>")
# async def get_batches_by_id(request, id: int):
#     for i in range(len(batch_list)+1):
#         try:
#             if batch_list[i]['id'] == id:
#                 batch_with_id = batch_list[i]
#                 batch = Batch(**batch_with_id)
#                 batch.manufacture_date = default(batch.manufacture_date)
#                 batch.expire_date = default(batch.expire_date)
#                 return json(batch.dict())

#         except Exception as e:
#             return json(e)


# @app.get("/sku")
# async def get_sku(request):
#     new_sku = list()
#     for i in range(len(sku_list)):
#         try:
#             sku_with_id = sku_list[i]
#             sku = Sku(**sku_with_id)
#             sku.brand = default(sku.brand)
#             sku.product = default(sku.product)
#             new_sku.append(sku.dict())
#         except Exception as e:
#             return json(e)
#     return json(new_sku)


# @app.get("/sku/<id:int>")
# async def get_sku_by_id(request, id: int):
#     for i in range(len(sku_list)+1):
#         try:
#             if sku_list[i]['id'] == id:
#                 sku_with_id == sku_list
#                 sku = Sku(**sku_with_id)
#                 sku.brand = default(sku.brand)
#                 sku.product = default(sku.product)
#                 return json(sku.dict())
#         except Exception as e:
#             return json(e)


if __name__ == "__main__":
    app.run(auto_reload=True, debug=True, workers=4)
