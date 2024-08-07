import datetime
import enum
import math
from typing import List

import pydantic


class ColombianDocumentType(enum.Enum):
    CEDULA = enum.auto()
    CEDULA_EXTRANJERIA = enum.auto()
    PPT = enum.auto()
    PASAPORTE = enum.auto()


class Document(pydantic.BaseModel):
    name: str
    document_type: ColombianDocumentType
    document_number: str



class Client(pydantic.BaseModel):
    id_client: str
    document: Document
    creation_date: datetime.date
    products: List[Product]