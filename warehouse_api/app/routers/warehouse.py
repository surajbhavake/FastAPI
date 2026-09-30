from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.warehouse import Warehouse
from app.schemas.warehouse import(
    WarehosueResponse,
    WarehouseCreate,
)


router = APIRouter(
    prefix="/warehouses",
    tags=['Warehouses'],
)