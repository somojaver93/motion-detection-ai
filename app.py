# ==========================================
# Flask Dashboard
# داشبورد تحت وب پروژه
# ==========================================


# فریم‌ورک Flask
from flask import (

     Flask,
    render_template,
    send_from_directory,
    request,
    redirect,
    send_file

)

# فایل تنظیمات پروژه
from config import DATABASE_FILE

# مدیریت آمار
from src.statistics_manager import (
    StatisticsManager
)

# مدیریت دیتابیس
from src.database_manager import (
    DatabaseManager
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
# اتصال به دیتابیس
# ==========================================

database = DatabaseManager(

    DATABASE_FILE

)


# ==========================================
# نمایش فایل‌های Screenshot
# ==========================================
@app.route(

    "/screenshots/<path:filename>"

)
def screenshot_file(

    filename

):

    return send_from_directory(

        "screenshots",

        filename

    )

# ==========================================
# نمایش فایل‌های Video
# ==========================================
@app.route(

    "/recordings/<path:filename>"

)
def recording_file(

    filename

):

    return send_from_directory(

        "recordings",

        filename

    )

# ==========================================
# جستجو بر اساس ID
# ==========================================
@app.route(

    "/search"

)
def search():

    # دریافت ID از URL
    event_id = request.args.get(

        "event_id"

    )

    event = None

    # اگر مقداری وارد شده باشد
    if event_id:

        event = database.get_event_by_id(

            int(event_id)

        )

    return render_template(

        "search.html",

        event=event

    )


# ==========================================
# جستجو بر اساس تاریخ
# ==========================================
@app.route(

    "/search_date"

)
def search_date():

    # دریافت تاریخ از فرم
    target_date = request.args.get(

        "target_date"

    )

    events = []

    # اگر تاریخ وارد شده باشد
    if target_date:

        events = database.get_events_by_date(

            target_date

        )

    return render_template(

        "search_date.html",

        events=events

    )


# ==========================================
# حذف رویداد
# ==========================================
@app.route(

    "/delete/<int:event_id>"

)
def delete_event(

    event_id

):

    # حذف رویداد از دیتابیس
    database.delete_event(

        event_id

    )

    # بازگشت به صفحه اصلی
    return redirect(

        "/"

    )


# ==========================================
# دانلود فایل CSV
# ==========================================
@app.route(

    "/export_csv"

)
def export_csv():

    # مسیر فایل گزارش
    csv_file = "events_report.csv"

    # ارسال فایل برای دانلود
    return send_file(

        csv_file,

        as_attachment=True

    )


# ==========================================
# جستجو بین دو تاریخ
# ==========================================
@app.route(

    "/search_between_dates"

)
def search_between_dates():

    # دریافت تاریخ شروع
    start_date = request.args.get(

        "start_date"

    )

    # دریافت تاریخ پایان
    end_date = request.args.get(

        "end_date"

    )

    events = []

    # اگر هر دو تاریخ وارد شده باشند
    if start_date and end_date:

        events = database.get_events_between_dates(

            start_date,
            end_date

        )

    return render_template(

        "search_between_dates.html",

        events=events

    )

# ==========================================
# صفحه اصلی داشبورد
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

    # دریافت همه رویدادها
    events = database.get_all_events()

    # ارسال اطلاعات به فایل HTML
    return render_template(

        "index.html",

        total_events=total_events,

        today_events=today_events,

        week_events=week_events,

        month_events=month_events,

        last_event=last_event,

        events=events

    )


# ==========================================
# اجرای برنامه
# ==========================================
if __name__ == "__main__":

    app.run(

        debug=True

    )