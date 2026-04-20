from models.user import User  # هنا استدعاء دالة التحقق
# وهنا استدعاء دالتين التحقق من عدم التكرار وتنفيذ الاوامر
from core.database import execute_query, fetch_one
import hashlib  # هنا مكتبة التشفير لكلمة المرور


def register_user(user_data):
    #  إنشاء الكائن (يتم استدعاء _validate() تلقائياً داخل __init__)
    user_obj = User(**user_data)

    #  فحص الحالة فوراً عبر واجهة الكلاس
    if not user_obj.is_valid():
        return {"is_valid": False, "data": None, "errors": user_obj.get_errors()}

    #  جلب البيانات النظيفة كقاموس جاهز للمعالجة
    user_dict = user_obj.to_dict()

    #  تشفير كلمة المرور واستبدال النص الصريح
    hashed_password = hashlib.sha256(
        user_dict["password"].encode('utf-8')).hexdigest()
    user_dict["password"] = hashed_password

    #  فحص التكرار (منع تسجيل نفس المستخدم مرتين)
    existing = fetch_one(
        "SELECT id FROM users WHERE username=? OR email=?",
        (user_dict["username"], user_dict["email"])
    )
    if existing is not None:
        return {"is_valid": False, "errors": ["Username or email already exists."]}

    #  الحفظ الفعلي في القاعدة
    insert_sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
    values_to_insert = (user_dict["username"],
                        user_dict["email"], user_dict["password"])
    is_saved = execute_query(insert_sql, values_to_insert)

    #  الرد النهائي الموحد
    if is_saved:
        return {"is_valid": True, "message": "User registered successfully."}
    return {"is_valid": False, "errors": ["Failed to save data. Please try again."]}
