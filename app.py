# ==========================================
# Flask Dashboard
# داشبورد تحت وب پروژه
# ==========================================


# فریم‌ورک Flask
from flask import (

    Flask,
    render_template

)

# فایل تنظیمات پروژه
from config import DATABASE_FILE

# مدیریت آمار
from src.statistics_manager import (
    StatisticsManager
)


# ==========================================
# ساخت برنامه Flask
# ==========================================

app = Flask(

    __name__

)


# ==========================================
# ساخت شیء آمار
# ==========================================

stats = StatisticsManager(

    DATABASE_FILE

)


# ==========================================
# صفحه اصلی
# ==========================================
@app.route("/")
def home():

    # تعداد کل رویدادها
    total_events = stats.total_events()

    # تعداد رویدادهای امروز
    today_events = stats.today_events()

    # تعداد رویدادهای هفته
    week_events = stats.week_events()

    # تعداد رویدادهای ماه
    month_events = stats.month_events()

    # آخرین رویداد
    last_event = stats.last_event()


    # ارسال اطلاعات به فایل HTML
    return render_template(

        "index.html",

        total_events=total_events,

        today_events=today_events,

        week_events=week_events,

        month_events=month_events,

        last_event=last_event

    )


# ==========================================
# اجرای برنامه
# ==========================================
if __name__ == "__main__":

    app.run(

        debug=True

    )