# ==========================================
# تست ارسال ایمیل با Gmail
# ==========================================


# کتابخانه ارتباط با سرور ایمیل
import smtplib


# ساخت ایمیل
from email.message import EmailMessage


# خواندن تنظیمات از فایل config
from config import (
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVER
)



# تابع اصلی برنامه
def main():

    try:

        # ساخت شیء ایمیل
        msg = EmailMessage()


        # عنوان ایمیل
        msg["Subject"] = (
            "Motion Detection AI Test"
        )


        # فرستنده
        msg["From"] = EMAIL_SENDER


        # گیرنده
        msg["To"] = EMAIL_RECEIVER


        # متن ایمیل
        msg.set_content(
            "Test email sent successfully."
        )


        # اتصال امن به سرور Gmail
        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:


            # ورود به حساب Gmail
            smtp.login(
                EMAIL_SENDER,
                EMAIL_PASSWORD
            )


            # ارسال ایمیل
            smtp.send_message(
                msg
            )


        # پیام موفقیت
        print(
            "Email sent successfully"
        )


    # مدیریت خطاها
    except Exception as error:


        print(
            "Email Error:",
            error
        )



# نقطه شروع برنامه
if __name__ == "__main__":

    main()