from typing import List
from uuid import UUID

from firestorefastapi.database import db
from firestorefastapi.schemas.item import Item, ItemCreate, ItemUpdate


class ItemDAO:
    collection_name = "items"

    def create(self, item_create: ItemCreate) -> Item:
        data = item_create.dict()
        data["id"] = str(data["id"])
        doc_ref = db.collection(self.collection_name).document(str(item_create.id))
        doc_ref.set(data)
        return self.get(item_create.id)

    def get(self, id: UUID) -> Item:
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc = doc_ref.get()
        if doc.exists:
            return Item(**doc.to_dict())
        return

    def list(self) -> List[Item]:
        items_ref = db.collection(self.collection_name).stream()
        return [
            Item(**doc.to_dict())
            for doc in items_ref
        ]

    def update(self, id: UUID, item_update: ItemUpdate) -> Item:
        data = item_update.dict()
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: UUID) -> None:
        db.collection(self.collection_name).document(str(id)).delete()
