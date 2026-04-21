from models.user import User, Owner, Admin  # هنا استدعاء كلاس المستخدم
# وهنا استدعاء دالتين التحقق من عدم التكرار وتنفيذ الاوامر
from core.database import execute_query, fetch_one
import hashlib  # هنا مكتبة التشفير لكلمة المرور


def register_user(user_data, role="user"):
    #  إنشاء الكائن (يتم استدعاء _validate() تلقائياً داخل __init__)
    if role == "owner":
        user_obj = Owner(**user_data)
    elif role == "admin":
        user_obj = Admin(**user_data)
    else:
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
    # إذا كان Owner نجعل rule_owner = 1، والباقي 0
    rule_owner = 1 if role == "owner" else 0
    # إذا كان Admin نجعل rule_admin = 1، والباقي 0
    rule_admin = 1 if role == "admin" else 0

    # 6. الحفظ (إضافة rule_owner و rule_admin للجدول الموجود)
    insert_sql = "INSERT INTO users (username, email, password, rule_owner, rule_admin) VALUES (?, ?, ?, ?, ?)"
    values_to_insert = (user_dict["username"], user_dict["email"],
                        user_dict["password"], rule_owner, rule_admin)
    is_saved = execute_query(insert_sql, values_to_insert)

    #  الرد النهائي الموحد
    if is_saved:
        return {"is_valid": True, "message": "User registered successfully."}
    return {"is_valid": False, "errors": ["Failed to save data. Please try again."]}

# تسجيل الدخول


def login_user(email, password):
    data = fetch_one(
        # التأكد ان المستخدم موجود
        "SELECT id, username, password, rule_owner, rule_admin FROM users WHERE email = ?", (email,))

    if data is None:
        return {"is_valid": False, "errors": ["Email or password is incorrect."]}

    # تحديد الفهرس للكلمة المرور لكي تتم المقارنه مع الهاش السابق
    stored_password = data[2]
    input_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if stored_password != input_hash:
        return {"is_valid": False, "errors": ["Email or password is incorrect."]}

    user_id = data[0]
    username = data[1]
    rule_owner = data[3]
    rule_admin = data[4]
    if rule_admin == 1:
        role = "admin"
    elif rule_owner == 1:
        role = "owner"
    else:
        role = "user"

    return {"is_valid": True, "message": "Login successful.", "user": {"id": user_id,
                                                                       "username": username,
                                                                       "email": email,
                                                                       "role": role}}
