from models.review import Review
from core.database import fetch_one, execute_query


def create_review(review_data):
    review_obj = Review(**review_data)

    if not review_obj.is_valid():
        return {"is_valid": False, "data": None, "errors": review_obj.get_errors()}
    review_dict = review_obj.to_dict()
    # البحث عن المستخدم اذا كان موجود
    existing_user = fetch_one(
        "SELECT id FROM users WHERE id=?",
        (review_dict["user_id"],))
    # اذا لم يكون موجود يكون خطأ
    if existing_user is None:
        return {"is_valid": False, "errors": ["User Not Found."]}
    # التأكد ان المكان متوفر
    existing_place = fetch_one(
        "SELECT id FROM place WHERE id=?", (review_dict["place_id"],))
    if existing_place is None:
        return {"is_valid": False, "errors": ["Place Not Found"]}
    # التاكد بان المستخدم لم يقيم نفس المكان سابقً
    existing_review = fetch_one("SELECT id FROM review WHERE user_id=? AND place_id=?", (
        review_dict["user_id"], review_dict["place_id"]))
    if existing_review is not None:
        return {"is_valid": False, "errors": ["You already reviewed this place."]}
    # بعد التاكد يتم اضافة التعليق والحفظ
    insert_sql = "INSERT INTO review (comment, rating, place_id, user_id)  VALUES (?,?,?,?)"
    values = (review_dict["comment"], review_dict["rating"],
              review_dict["place_id"], review_dict["user_id"])
    is_saved = execute_query(insert_sql, values)
    if is_saved:
        return {"is_valid": True, "message": "Review added successfully."}
    return {"is_valid": False, "errors": ["Failed to save review."]}
