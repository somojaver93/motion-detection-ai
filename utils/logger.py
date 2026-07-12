import logging
import os

# ساخت پوشه logs
os.makedirs("logs", exist_ok=True)

# تنظیمات لاگ
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(
    "MotionDetectionLogger"
)