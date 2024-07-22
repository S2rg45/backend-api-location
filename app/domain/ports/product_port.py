

from app.adapters.internal.sqlite_base import SQLiteBase


class ProductRepository(SQLiteBase):
    def __init__(self):
        self.squilete = SQLiteBase("products.db")
        self.squilete.execute("CREATE TABLE IF NOT EXISTS products (id TEXT PRIMARY KEY, name TEXT, description TEXT, price FLOAT, in_stock BOOLEAN, created_at TEXT)")
    

    def create(self, product):
        query = 'INSERT INTO products (id, name, description, price, in_stock, created_at) VALUES ("{}","{}","{}",{},{},"{}")'.format(product["id"], product["name"], product["description"], product["price"], product["in_stock"], product["created_at"])
        self.squilete.execute(query)
        self.squilete.commit()
        return {"id": product["id"]}


    def read(self, product_id):
        query = 'SELECT * FROM products WHERE id = "{}"'.format(product_id)
        self.squilete.execute(query)
        return self.squilete.fetchone()


    def read_all(self):
        query = "SELECT * FROM products"
        self.squilete.execute(query)
        data = self.squilete.fetchall()
        return {"products": data}


    def update(self, product):
        query = 'UPDATE products SET name = "{}", description = "{}", price = {}, in_stock = {} WHERE id = "{}" '.format(product["name"], product["description"], product["price"], product["in_stock"], product["id"])
        self.squilete.execute(query)
        self.squilete.commit()
        return {"id": product["id"]}


    def delete(self, product_id):
        query = 'DELETE FROM products WHERE id = "{}"'.format(product_id)
        self.squilete.execute(query)
        self.squilete.commit()
        return {"id": str(product_id)}
