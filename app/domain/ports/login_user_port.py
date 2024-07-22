

# from adapters.internal.sqlite_base import SQLiteBase
# from adapters.security.utils_token import SettingsToken


# class LoginRegistry():
#     def __init__(self):
#         super().__init__("backend-product/app/adapters/internal/user.db")
#         self.sqllite = SQLiteBase()
#         self.settings = SettingsToken()

    
#      #validacion de la existencia del usuario
#     def login_with_data(self, data):
#         try:
#             email = {"email": data.get("email")}
#             user = self.sqllite.execute("SELECT * FROM users WHERE email = ?", (email))
#             if user:
#                 return True
#             return False
#         except Exception as e:
#             print(e)
#             return False
        
#     # #create token user
#     # def create_token(self, data, data_db):
#     #     try:
#     #         password = self.settings_token.verify_password(data.get("password"), data_db.get("password"))
#     #         print("password", password)
#     #         if not password:
#     #             return False
#     #         data_create_token = {
#     #             "username": data_db.get("username"),
#     #             "email": data_db.get("email"),
#     #             "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#     #         }
#     #         return {"token": self.settings_token.create_access_token(data_create_token)}
#     #     except Exception as e:
#     #         print(e)
#     #         return False
        
        
