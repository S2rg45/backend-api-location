
import uuid

from datetime import datetime, timezone

from app.domain.commands.create_product_command import ProductCreate
from app.domain.ports.product_port import ProductRepository


class CreateProductHandler:
    def __init__(self, product: ProductCreate) :
        self.product = product

    def execute(self):
        new_product = {
            "id": str(uuid.uuid4()),
            "name": self.product["name"],
            "description": self.product["description"],
            "price": self.product["price"],
            "in_stock": self.product["in_stock"],
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        print("NEW PRODUCT", new_product)
        create_product = ProductRepository()
        id = create_product.create(new_product)
        return id

        