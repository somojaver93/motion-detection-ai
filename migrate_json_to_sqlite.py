# ==========================================
# انتقال اطلاعات JSON به SQLite
# ==========================================


# خواندن فایل JSON
import json


# مسیر فایل‌ها
from config import (
    EVENT_FILE,
    DATABASE_FILE
)


# مدیریت دیتابیس
from src.database_manager import (
    DatabaseManager
)


# ==========================================
# ساخت شیء دیتابیس
# ==========================================

database = DatabaseManager(

    DATABASE_FILE

)


# ==========================================
# خواندن فایل JSON
# ==========================================

with open(

    EVENT_FILE,
    "r",
    encoding="utf-8"

) as file:

    events = json.load(

        file

    )


# ==========================================
# انتقال رکوردها
# ==========================================

for event in events:

    database.insert_event(

        event["screenshot"],

        event["video"]

    )



# ==========================================
# نمایش نتیجه
# ==========================================

print(

    "Migration Completed"

)

print(

    "Imported Events:",

    len(events)

)