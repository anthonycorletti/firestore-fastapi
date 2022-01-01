from typing import List

from v1.daos.item import ItemDAO
from v1.schemas.item import Item, ItemCreate, ItemUpdate

item_dao = ItemDAO()


class ItemService:
    def create_item(self, item_create: ItemCreate) -> Item:
        return item_dao.create(item_create)

    def get_item(self, id: str) -> Item:
        return item_dao.get(id)

    def list_items(self) -> List[Item]:
        return item_dao.list()

    def update_item(self, id: str, item_update: ItemUpdate) -> Item:
        return item_dao.update(id, item_update)

    def delete_item(self, id: str) -> None:
        return item_dao.delete(id)
