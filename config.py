# ==============================
# تنظیمات اصلی پروژه تشخیص حرکت
# ==============================


# عرض فریم‌های ورودی دوربین
FRAME_WIDTH = 640

# ارتفاع فریم‌های ورودی دوربین
FRAME_HEIGHT = 480


# حداقل مساحت جسم متحرک
# اگر جسمی کوچکتر از این باشد نادیده گرفته می‌شود
MIN_AREA = 3000


# شماره دوربین سیستم
# معمولاً دوربین اصلی = 0
CAMERA_INDEX = 0


# مسیر ذخیره ویدئوهای ضبط شده
OUTPUT_FOLDER = "recordings/"

# مسیر فایل ویدئو برای تست
VIDEO_PATH = "videos/test.mp4"

# مسیر ذخیره اسکرین‌شات‌ها
SCREENSHOT_FOLDER = "screenshots/"

# ==============================
# Email Settings
# ==============================

EMAIL_SENDER = "mojavers72@gmail.com"

EMAIL_PASSWORD = "papvipxntvaqdnms"

EMAIL_RECEIVER = "mojavers72@gmail.com"

# مسیر فایل ذخیره رویدادها
EVENT_FILE = "events/motion_events.json"