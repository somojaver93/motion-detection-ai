# ==========================================
# تست دریافت همه رویدادها
# ==========================================

from config import DATABASE_FILE

from src.database_manager import (
    DatabaseManager
)


database = DatabaseManager(

    DATABASE_FILE

)


events = database.get_all_events()


print(

    "Total Events:",

    len(events)

)


for event in events:

    print(

        event

    )