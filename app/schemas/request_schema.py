from datetime import date
from pydantic import BaseModel
from typing import Optional

from app.schemas.pharmacy_schema import PharmacyOut
from app.schemas.product_schema import ProductOut
from app.schemas.request_state_schema import RequestStateOut
from app.schemas.user_schema import UserOut

class RequestOut(BaseModel):
    id: int
    invoice_id: int
    purchase_date: date
    product_quantity: int
    invoice_image: str # base64 encoded
    request_state: str
    pharmacy: PharmacyOut
    user: UserOut
    product: ProductOut
    class Config:
        from_attributes = True
    
class RequestIn(BaseModel):
    invoice_id: int
    purchase_date: date
    product_quantity: int
    invoice_image: str # base64 encoded
    pharmacy_id: int
    user_id: int
    product_id: int

class RequestStateUpdate(BaseModel):
    request_state: str
    
class SimpleRequest(BaseModel):
    id: int
    invoice_id: int
    product_name: str
    request_state: str
    client_name: str
    purchase_date: date