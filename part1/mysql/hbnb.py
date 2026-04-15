# هذا احدى مكتبات قاعدة البيانات ويوجد غيرها
import sqlite3
# انشاء اتصال او انشاء قاعدة بيانات
# في حال عدم وجود القاعده بالاسم يتم انشاء وحده جديده
conn = sqlite3.connect('hbnb.db')
# انشاء واعطاء صلاحيات للكتابه بلغة sql
# cursor يعتبر كقناه بين القاعدة والاوامر التي تكتب لاحق
cursor = conn.cursor()
# هنا انشانا اول جدول في القاعده بهذا الطريقه
# الجدول الاول للمستخدم
cursor.execute(
    'CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT, rule_owner  BOOLEAN DEFAULT 0, rule_admin  BOOLEAN DEFAULT 0)')
# الجدول الرابع لوسائل الراحه للاماكن المضافة ل اي مكان يضاف في الموقع
cursor.execute(
    'CREATE TABLE amenity(id INTEGER PRIMARY KEY, description TEXT, images TEXT)')
# الجدول الثاني للمكان
cursor.execute(
    'CREATE TABLE place(id INTEGER PRIMARY KEY, title TEXT, description TEXT, price INTEGER NOT NULL, location INTEGER NOT NULL, Amenity_id INTEGER, user_id INTEGER)')
# الجدول الثالث للتقييم
cursor.execute(
    'CREATE TABLE review(id INTEGER PRIMARY KEY, comment TEXT, rating INTEGER  NOT NULL CHECK (rating BETWEEN 1 AND 5), place_id INTEGER, user_id INTEGER)')

# يفضل استخدامها مع الاستعلامات بكافة طرقها
#  اعطاء تحديث الاوامر وتنفيذها على قاعده البيانات
# conn.commit()
# بعد الانشاء يتم اغلاق القاعده عشان م يكون في تسيرب للبيانات
conn.close()
