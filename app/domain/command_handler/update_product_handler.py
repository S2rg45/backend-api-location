

from app.domain.commands.update_product_command import UpdateProduct
from app.domain.ports.product_port import ProductRepository

class UpdateProductHandler:
    def __init__(self, product: UpdateProduct):
        self.product = product

    def execute(self) :
        update_product = ProductRepository()
        id = update_product.update(self.product)
        return id