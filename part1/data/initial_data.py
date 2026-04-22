# هذا احدى مكتبات قاعدة البيانات ويوجد غيرها
import sqlite3
import os


def init_schema():
    # ضمان أن القاعدة تتكون داخل مجلد data بغض النظر عن مكان تشغيل السكريبت
    db_path = os.path.join("data", "hbnb.db")

    # انشاء اتصال او انشاء قاعدة بيانات
    # في حال عدم وجود القاعده بالاسم يتم انشاء وحده جديده
    conn = sqlite3.connect(db_path)
# انشاء واعطاء صلاحيات للكتابه بلغة sql
# cursor يعتبر كقناه بين القاعدة والاوامر التي تكتب لاحق
    cursor = conn.cursor()
    # لتفعيل ربط العلاقات
    cursor.execute("PRAGMA foreign_keys = ON;")
# هنا انشانا اول جدول في القاعده بهذا الطريقه
# الجدول الاول للمستخدم
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
			   username TEXT NOT NULL UNIQUE,
			   email TEXT NOT NULL UNIQUE,
			   password TEXT NOT NULL,
			   rule_owner  BOOLEAN DEFAULT 0 NOT NULL,
			   rule_admin  BOOLEAN DEFAULT 0 NOT NULL)""")
# الجدول الرابع لوسائل الراحه للاماكن المضافة ل اي مكان يضاف في الموقع
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS amenity(id INTEGER PRIMARY KEY AUTOINCREMENT,
			   name TEXT NOT NULL UNIQUE,
				description TEXT NOT NULL,
			   images TEXT)""")
# الجدول الثاني للمكان
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS place(id INTEGER PRIMARY KEY AUTOINCREMENT,
			   title TEXT NOT NULL,
			   description TEXT NOT NULL,
			   price REAL NOT NULL CHECK (price > 0),
			   latitude REAL,
               longitude REAL,
			   amenity_id INTEGER NOT NULL,
			   user_id INTEGER NOT NULL)""")
# الجدول الثالث للتقييم
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS review(id INTEGER PRIMARY KEY AUTOINCREMENT,
			   comment TEXT NOT NULL,
			   rating INTEGER  NOT NULL CHECK (rating BETWEEN 1 AND 5),
			   place_id INTEGER NOT NULL,
			   user_id INTEGER NOT NULL)""")

# يفضل استخدامها مع الاستعلامات بكافة طرقها
#  اعطاء تحديث الاوامر وتنفيذها على قاعده البيانات
    conn.commit()
# بعد الانشاء يتم اغلاق القاعده عشان م يكون في تسيرب للبيانات
    conn.close()
