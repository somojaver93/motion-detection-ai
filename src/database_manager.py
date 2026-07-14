# ==========================================
# Database Manager
# مدیریت دیتابیس SQLite
# ==========================================


# کتابخانه SQLite
import sqlite3

# زمان
from datetime import datetime


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

        # مسیر فایل دیتابیس
        self.database_file = (
            database_file
        )

        # ایجاد جدول‌ها
        self.create_tables()


    # --------------------------------------
    # ایجاد جدول‌ها
    # --------------------------------------
    def create_tables(

        self

    ):

        # اتصال به دیتابیس
        connection = sqlite3.connect(

            self.database_file

        )

        # ایجاد Cursor
        cursor = connection.cursor()


        # ایجاد جدول رویدادها
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


        # ذخیره تغییرات
        connection.commit()

        # بستن اتصال
        connection.close()


    # --------------------------------------
    # ثبت رویداد جدید
    # --------------------------------------
    def insert_event(

        self,
        screenshot_path,
        video_path=None

    ):

        # اتصال به دیتابیس
        connection = sqlite3.connect(

            self.database_file

        )

        # ایجاد Cursor
        cursor = connection.cursor()


        # زمان فعلی
        current_time = str(

            datetime.now()

        )


        # ثبت رکورد جدید
        cursor.execute(

            """
            INSERT INTO events
            (
                time,
                screenshot,
                video
            )
            VALUES
            (
                ?,
                ?,
                ?
            )
            """,

            (
                current_time,
                screenshot_path,
                video_path
            )

        )


        # ذخیره تغییرات
        connection.commit()

        # بستن اتصال
        connection.close()


    # --------------------------------------
    # دریافت همه رویدادها
    # --------------------------------------
    def get_events(

        self

    ):

        # اتصال به دیتابیس
        connection = sqlite3.connect(

            self.database_file

        )

        # ایجاد Cursor
        cursor = connection.cursor()


        # دریافت همه رکوردها
        cursor.execute(

            "SELECT * FROM events"

        )

        events = cursor.fetchall()


        # بستن اتصال
        connection.close()


        return events


    # --------------------------------------
    # تعداد کل رویدادها
    # --------------------------------------
    def count_events(

        self

    ):

        # اتصال به دیتابیس
        connection = sqlite3.connect(

            self.database_file

        )

        cursor = connection.cursor()


        # شمارش رکوردها
        cursor.execute(

            "SELECT COUNT(*) FROM events"

        )

        count = cursor.fetchone()[0]


        connection.close()

        return count


    # --------------------------------------
    # دریافت آخرین رویداد
    # --------------------------------------
    def get_last_event(

        self

    ):

        # اتصال به دیتابیس
        connection = sqlite3.connect(

            self.database_file

        )

        cursor = connection.cursor()


        # دریافت آخرین رکورد
        cursor.execute(

            """
            SELECT *
            FROM events
            ORDER BY id DESC
            LIMIT 1
            """

        )

        event = cursor.fetchone()


        connection.close()

        return event