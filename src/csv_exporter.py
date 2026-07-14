# ==========================================
# CSV Exporter
# خروجی گرفتن از رویدادها به CSV
# ==========================================


# کار با فایل CSV
import csv

# مدیریت دیتابیس
from src.database_manager import (
    DatabaseManager
)


# ==========================================
# کلاس خروجی CSV
# ==========================================
class CSVExporter:


    # --------------------------------------
    # سازنده کلاس
    # --------------------------------------
    def __init__(

        self,
        database_file

    ):

        self.database = DatabaseManager(

            database_file

        )


    # --------------------------------------
    # ساخت فایل CSV
    # --------------------------------------
    def export(

        self,
        output_file

    ):

        # دریافت رویدادها
        events = self.database.get_events()


        # ساخت فایل CSV
        with open(

            output_file,

            "w",

            newline="",

            encoding="utf-8"

        ) as file:


            writer = csv.writer(

                file

            )


            # هدر فایل
            writer.writerow(

                [

                    "ID",
                    "TIME",
                    "SCREENSHOT",
                    "VIDEO"

                ]

            )


            # نوشتن داده‌ها
            for event in events:

                writer.writerow(

                    event

                )


        print(

            "CSV Exported:",

            output_file

        )