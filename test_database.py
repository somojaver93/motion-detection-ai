# ==========================================
# تست دیتابیس
# ==========================================


from config import DATABASE_FILE

from src.database_manager import (
    DatabaseManager
)


database = DatabaseManager(

    DATABASE_FILE

)

print(

    "Database Created Successfully"
)