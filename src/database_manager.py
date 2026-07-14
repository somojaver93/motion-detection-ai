# ==========================================
# Database Manager
# مدیریت دیتابیس SQLite
# ==========================================


# کتابخانه SQLite
import sqlite3


# ==========================================
# کلاس مدیریت دیتابیس
# ==========================================
class DatabaseManager:


    # --------------------------------------
    # سازنده کلاس
    # --------------------------------------
    def __init__(

        self,
        database_file

    ):

        # مسیر دیتابیس
        self.database_file = (
            database_file
        )

        # ساخت جدول‌ها
        self.create_tables()


    # --------------------------------------
    # ایجاد جدول‌ها
    # --------------------------------------
    def create_tables(

        self

    ):

        connection = sqlite3.connect(

            self.database_file

        )

        cursor = connection.cursor()


        cursor.execute(

            """
            CREATE TABLE IF NOT EXISTS events (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                time TEXT,

                screenshot TEXT,

                video TEXT

            )
            """

        )

        connection.commit()

        connection.close()