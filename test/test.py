# from typing import Generic, TypeVar, Optional, List
# from pydantic import BaseModel, validator, ValidationError
# from pydantic.generics import GenericModel

# DataT = TypeVar('DataT')

# class Error(BaseModel):
#     code: int
#     message: str

# class DataModel(BaseModel):
#     number: List[int]
#     people: List[str]

# class Response(GenericModel, Generic[DataT]):
#     data: Optional[DataT]
#     error: Optional[Error]

#     @validator('error', always=True)
#     def check_consistency(cls, v, values):
#         if v is not None and values['data'] is not None:
#             raise ValueError('must not provide both data and error')
#         if v is None and values.get('data') is None:
#             raise ValueError('must provide data or errror')
#         return v

# data = DataModel(numbers=[1,2,3], people=[])
# error = Error(code=404, message='Not found')
# print(Response[int](data=1))


from sanic import Sanic, text
from auth import protected
from login import login


app = Sanic("AuthApp")
app.config.SECRET = "KEEP_IT_SECRET_KEEP_IT_SAFE"
app.blueprint(login)


@app.get("/secret")
@protected
async def secret(request):
    return text("To go fast, you must be fast")
