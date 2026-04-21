from models.amenity import Amenity
from core.database import fetch_one, execute_query


def create_amenity(amenity_data):
    # هنا ننشئ اتصال مع الكلاس ثم المتغيرات
    amenity_obj = Amenity(**amenity_data)

    if not amenity_obj.is_valid():  # نتحقق ان البيانات القادمه صحيحه في حال العكس نرسل الخطأ
        return {"is_valid": False, "data": None, "errors": amenity_obj.get_errors()}

    amenity = amenity_obj.to_dict()  # اخذ البيانات الراجعه وتخزينها في متغير
    existing = fetch_one(
        "SELECT id, name FROM amenity WHERE name=?", (amenity["name"],))
    if existing is not None:  # هنا نتاكد ان البيانات غير موجوده
        return {"is_valid": False, "errors": ["Amenity name already exists."]}

    insert_sql = "INSERT INTO amenity (name,description, images) VALUES (?,?,?)"
    values = (amenity["name"], amenity["description"], amenity["images"])
    # بعد تجهيز امر الادخال وحددنا الاماكن نستخدم دالة الادخال
    is_saved = execute_query(insert_sql, values)
    if is_saved:
        return {"is_valid": True, "message": "Amenity created successfully."}
    else:
        return {"is_valid": False, "errors": ["Failed to save amenity."]}
