

import uuid

from datetime import datetime, timezone
from app.domain.ports.product_port import ProductRepository


class ListProductsHandler():
    def __init__(self):
        pass

    def execute(self):
        product = ProductRepository()
        product_list = product.read_all()
        return product_list

