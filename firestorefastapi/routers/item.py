from typing import List

from fastapi import APIRouter, Body, HTTPException
from pydantic.types import UUID4

from firestorefastapi.schemas.item import Item, ItemCreate, ItemUpdate
from firestorefastapi.services.item import ItemService

router = APIRouter()
item_service = ItemService()


@router.post("/items", response_model=Item, tags=["item"])
def create_item(item_create: ItemCreate = Body(...)) -> Item:
    return item_service.create_item(item_create)


@router.get("/items/{id}", response_model=Item, tags=["item"])
def get_item(id: UUID4) -> Item:
    item = item_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    return item


@router.get("/items", response_model=List[Item], tags=["item"])
def list_items() -> List[Item]:
    items = item_service.list_items()
    if not items:
        raise HTTPException(status_code=404, detail="Items not found.")
    return items


@router.put("/items/{id}", response_model=Item, tags=["item"])
def update_item(id: UUID4, item_update: ItemUpdate = Body(...)) -> Item:
    item = item_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    return item_service.update_item(id, item_update)


@router.delete("/items/{id}", response_model=Item, tags=["item"])
def delete_item(id: UUID4) -> Item:
    item = item_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    return item_service.delete_item(id)
