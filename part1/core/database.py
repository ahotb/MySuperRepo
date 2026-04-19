import sqlite3
import os  # Operating System  استدعاء مكتبه
# للتعامل مع المسارات المجلدات او الملفات على وندز وماك ولنكس

""" تستقبل متغير وفي حال عدم وجود متغير ستكون القيمه فارغه
ووضعنا شرط اذا كانت فارغه انشاء في مجلد وحددنا الاسم في البدايه ويفتح اسم القاعده التي تحددت ثانياً """


def get_db_connection(db_path=None):
    if db_path is None:
        db_path = os.path.join("data", "hbnb.db")
# os.path.join هذا لضمان ان المسار يعمل بشكل صحيح على اي جهاز

# هنا انشاء الاتصال المحدد مسبقاً  db_path
    con = sqlite3.connect(db_path, check_same_thread=False)
    # check_same_thread=False هذا الامر يسمح باكثر من اتصال بنفس الوقت وتكون عملية التنظم البياتات على الباك-اند لتسريع عمل الموقع
    con.execute("PRAGMA foreign_keys = ON;")
    # هنا نخبر قاعدة البيانات بان تفعل الترابط بين الجداول لن مكتبة sqlite تخلي مغلق تلقائين

    return con
# هنا نرجع الاتصال


"""  (INSERT/UPDATE/DELETE) هنا الداله تاخذ متغيرين الاول يكون الاوامر التي ستنفذ
 الثاني ياخذ المعاملات التي ستضاف في الجدول ويكون في Tuple لكي لايسمح بتغير لاحقً  """


def execute_query(sql_query, params=()):
    """ هنا انشانا الاتصال عبر الداله السابقه
    وقمنا بانشاء قناة تحكم بالقاعده عشان يكون لنا وصول كامل """
    con = get_db_connection()
    cur = con.cursor()

    """ هنا استخدمنا بلوك try عشان نتحكم بالاخطا في حال حدوثها ولا يصقط البرنامج علينا
    """
    try:
        cur.execute(sql_query, params)
        con.commit()  # للتاكيد التحديث
        return True
    except Exception as e:
        print(f"Error: {e}")
        con.rollback()  # هنا في حال حدوث الخطأ يقوم بارجاع الجدول للسابق ويحمي البيانات من التلف
        return False
    finally:
        cur.close()
        con.close()


def fetch_all(sql_query, params=()):
    con = get_db_connection()
    cur = con.cursor()

    try:
        cur.execute(sql_query, params)
        data = cur.fetchall()  # جلب جميع الصفوف الناتجة عن الاستعلام وحفظها في قائمة
        return data  # ارجاع البيانات
    except Exception as e:
        print(f"NOT Found data: {e}")
        return []
    finally:
        cur.close()
        con.close()


def fetch_one(sql_query, params=()):

    con = get_db_connection()
    cur = con.cursor()

    try:
        cur.execute(sql_query, params)
        data = cur.fetchone()  # جلب اول صف  من الصفوف الناتجة عن الاستعلام وحفظها في متغير
        return data  # ارجاع البيانات
    except Exception as e:
        print(f"NOT Found data: {e}")
        return None
    finally:
        cur.close()
        con.close()
