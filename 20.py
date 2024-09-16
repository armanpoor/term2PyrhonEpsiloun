import tkinter as tk
import requests
import json
from tkinter import messagebox

# کلید API
api_key = "610236741ad896925e95e43ff0cbd0c2"

# تابعی برای گرفتن اطلاعات آب و هوا
def get_weather():
    city_name = city_entry.get()  # دریافت نام شهر از ورودی کاربر
    country_code = "IR"  # می‌توانید این بخش را هم به ورودی تبدیل کنید
    
    # ساخت URL درخواست
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units=metric"

    try:
        # ارسال درخواست به API
        response = requests.get(url)
        response.raise_for_status()  # برای چک کردن خطاهای HTTP
        
        # پردازش داده‌های پاسخ
        desire_dict = response.json()
        temp = desire_dict["main"]["temp"]
        humidity = desire_dict["main"]["humidity"]
        
        # نمایش نتیجه در رابط کاربری
        result_label.config(text=f"دما: {temp}°C\nرطوبت: {humidity}%")
    
    except requests.exceptions.HTTPError:
        messagebox.showerror("خطا", "شهر وارد شده یافت نشد!")
    except Exception as e:
        messagebox.showerror("خطا", f"خطایی رخ داد: {str(e)}")

# ساخت پنجره اصلی
root = tk.Tk()
root.title("برنامه نمایش دما و رطوبت شهر")
root.geometry("300x200")

# برچسب و ورودی برای گرفتن نام شهر
city_label = tk.Label(root, text="نام شهر را وارد کنید:")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(root)
city_entry.grid(row=1, column=0, padx=10, pady=10)

# دکمه برای گرفتن اطلاعات آب و هوا
get_weather_btn = tk.Button(root, text="دریافت اطلاعات", command=get_weather)
get_weather_btn.grid(row=2, column=0, padx=10, pady=10)

# برچسب برای نمایش نتیجه
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, padx=10, pady=10)

# اجرای پنجره
root.mainloop()
