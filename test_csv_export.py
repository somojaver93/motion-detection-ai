# ==========================================
# تست خروجی CSV
# ==========================================


from config import DATABASE_FILE

from src.csv_exporter import (
    CSVExporter
)


exporter = CSVExporter(

    DATABASE_FILE

)


exporter.export(

    "events_report.csv"

)