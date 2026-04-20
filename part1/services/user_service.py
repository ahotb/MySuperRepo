from models.user import validate_user_data  # هنا استدعاء دالة التحقق
# وهنا استدعاء دالتين التحقق من عدم التكرار وتنفيذ الاوامر
from core.database import execute_query, fetch_one
import hashlib  # هنا مكتبة التشفير لكلمة المرور


def register_user(user_data):
    # هنا نتحقق عبر الداله التي انشاناها ونخزنه في المتغير
    check_result = validate_user_data(user_data)
    # هنا نتحقق من البيانات في حال انها خطأ يتم ارجع الخطأ دون الاستمرار
    if not check_result["is_valid"]:
        return check_result
    # هنا بعد النجاح نختار من البيانات حقتنا كلمة المرور لتشفيرها
    password_plain = check_result["data"]["password"]
    # في هذا المتغير نستخدم مكتبة التشفير للتشفير
    hashed_password = hashlib.sha256(
        password_plain.encode('utf-8')).hexdigest()
    # هنا بعد التشفير نرجع كلمة المرور لمكانها
    check_result["data"]["password"] = hashed_password

    username = check_result["data"]["username"]
    email = check_result["data"]["email"]
    existing = fetch_one(
        "SELECT id FROM users WHERE username=? OR email=?", (username, email))
    # التحقق اذا كان موجود يعطيني خطأ
    if existing is not None:
        return {"is_valid": False, "errors": ["Username or email already exists."]}
    # تجهيز امر الاضافة بعد التحقق
    insert_sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
    # البيانات بعد التحقق وكلمة المرور المشفره تكون هنا لحفطها
    values_to_insert = (username, email, check_result["data"]["password"])
    is_saved = execute_query(insert_sql, values_to_insert)
    # هنا الحفظ وارسال البيانات
    if is_saved:
        return {"is_valid": True, "message": "User registered successfully."}
    return {"is_valid": False, "errors": ["Failed to save data. Please try again."]}
