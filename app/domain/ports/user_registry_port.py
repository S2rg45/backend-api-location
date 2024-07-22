

from app.adapters.internal.sqlite_base import SQLiteBase
from app.adapters.security.utils_token import SettingsToken


class UserRepository():
    def __init__(self):
        self.squilete = SQLiteBase("users.db")
        self.squilete.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT)")
        self.settings = SettingsToken()

    #validacion de la existencia del usuario
    def get_data_user(self, data):
        query = 'SELECT * FROM users WHERE email = "{}" OR username = "{}"'.format(data.get("email"), data.get("username"))
        self.squilete.execute(query)
        data = self.squilete.fetchone()
        return data
        
    #crear nuevo usuario
    def create_new_user(self, data):
        password = self.settings.hashed_password(data.get("password"))
        query = 'INSERT INTO users (username, email, password) VALUES ("{}","{}","{}")'.format(data.get("username"), data.get("email"), password)
        self.squilete.execute(query)
        self.squilete.commit()
        return 