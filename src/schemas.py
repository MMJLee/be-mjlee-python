from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class StatementSchema(BaseModel):
    description: str
    truth: bool
    backstory: str
    used: bool

    class Config:
        orm_mode = True


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestStatement(BaseModel):
    parameter: StatementSchema = Field(...)
