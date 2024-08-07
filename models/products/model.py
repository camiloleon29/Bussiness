import enum

import pydantic


class ProductTypes(enum.Enum):
    LOAN = "PRESTAMO"


class ProductType(pydantic.BaseModel):
    product_type: str
    description: str


class Product(pydantic.BaseModel):
    product_id: str
    product_type: ProductType


AVAILABLE_PRODUCT_TYPES = {
    ProductTypes.LOAN: ProductType(product_type=ProductTypes.LOAN.value,
                                   description="Producto financiero en el que un prestatario recibe dinero con la "
                                               "obligación de devolverlo con intereses durante un período "
                                               "especificado.")
}