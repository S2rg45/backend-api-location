
import uuid

from datetime import datetime, timezone

from app.domain.commands.delete_product_command import DeleteProduct
from app.domain.ports.product_port import ProductRepository

class DeleteProductHandler:
    def __init__(self, product: DeleteProduct):
        self.product = product

    def execute(self):
        repository = ProductRepository()
        product = repository.read(self.product["id"])
        print("PRODUCT_EXECUTE", product)
        if not product:
            raise Exception("Product not found")
        id = repository.delete(product[0])
        return id