from models.place import Place
from core.database import fetch_one, execute_query


def create_place(place_data):
    place_obj = Place(**place_data)

    if not place_obj.is_valid():  # التحقق من وجود البيانات
        return {"is_valid": False, "data": None, "errors": place_obj.get_errors()}
    # استعاء البيانات كالقموس
    place_dict = place_obj.to_dict()
    # البحث عن وجود المالك
    existing_user = fetch_one(
        "SELECT id, rule_owner FROM users WHERE id=?",
        (place_dict["user_id"],))
    # اذا لم يكون موجود يكون خطأ
    if existing_user is None:
        return {"is_valid": False, "errors": ["Owner not found."]}
    user_id, rule_owner = existing_user
    if not rule_owner:  # إذا كانت 0 (False) يعني مستخدم عادي
        return {"is_valid": False, "errors": ["Only owners can add places."]}
    # البحث عن وسائل الراحه
    existing_amenity = fetch_one(
        "SELECT id FROM amenity WHERE id=?",
        (place_dict["amenity_id"],))
    # اذا لم تكن موجوده خطأ
    if existing_amenity is None:
        return {"is_valid": False, "errors": ["Amenity not found."]}
    # هنا اعداد اضافة المكان بعد الانتهاء من التحقق
    insert_sql = """INSERT INTO place ( title, description, price, latitude,longitude, amenity_id, user_id)
    VALUES (?,?,?,?,?,?,?)"""
    values_to_insert = (place_dict["title"], place_dict["description"], place_dict["price"], place_dict["latitude"],
                        place_dict["longitude"], place_dict["amenity_id"], place_dict["user_id"])
    is_saved = execute_query(insert_sql, values_to_insert)
    # هنا تأكيد الاضافه او العكس
    if is_saved:
        return {"is_valid": True, "message": "place registered successfully."}
    return {"is_valid": False, "errors": ["Failed to save data. Please try again."]}


def update_place(place_id, place_data):
    # الداله تعدل البيانات حقت المكان
    # ناخذ البيانات من الكلاس لكي يوفر علينا كتابتها
    place_obj = Place(**place_data)
    if not place_obj.is_valid():  # هنا اخذنا من داله التحقق لكي نختصر التحقق
        return {"is_valid": False, "errors": place_obj.get_errors()}

    # وهنا اخذنا القاموس حقنا لكي يوفر علينا الاكواد ويختصر الوقت
    place_dict = place_obj.to_dict()
    # هنا داله الاتسعلام  للتحقق من وجود المكان وانه للمالك
    ownership_check = fetch_one(
        "SELECT id FROM place WHERE id=? AND user_id=?",
        (place_id, place_dict["user_id"]))

    if ownership_check is None:
        return {"is_valid": False, "errors": ["Unauthorized: Place not found or you don't own it."]}
        # هنا اضافة اوامر الاتحديث مع داله sql
    update_sql = "UPDATE place SET title=?, description=?, price=?, latitude=?, longitude=? WHERE id=?"
    values = (place_dict["title"], place_dict["description"], place_dict["price"], place_dict["latitude"],
              place_dict["longitude"], place_id)
    is_updated = execute_query(update_sql, values)
    # التحقق من النجاح ثم الاضافه
    if is_updated:
        return {"is_valid": True, "message": "place updated successfully."}
    return {"is_valid": False, "errors": ["Failed to save data. Please try again."]}
