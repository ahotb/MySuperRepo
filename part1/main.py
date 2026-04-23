from data.initial_data import init_schema
from models.user import Owner
from services.user_service import register_user, login_user, get_all_users
from core.database import fetch_all
from services.amenity_service import create_amenity
from services.place_service import create_place
from services.review_service import create_review
if __name__ == "__main__":
    init_schema()

# إنشاء كائن مالك (اختبار منطقي فقط حالياً)
# owner_obj = Owner(username="Owner1", email="owner@test.com",
#                   password="123", user_id=1)

# print("🔹 Role Name:", owner_obj.get_role_name())
# print("🔹 Can update own place?", owner_obj.can_update_place(1))   # متوقع: True
# print("🔹 Can delete another place?",
#       owner_obj.can_delete_place(5))  # متوقع: False

print(get_all_users())
#     print("\n🔹 Test 1: Valid Review (Success):")
# print(create_review({
#     "comment": "A wonderful experience, I recommend visiting it!",
#     "rating": 5,
#     "place_id": 1,   # ← استبدله بمعرف مكان موجود
#     "user_id": 1     # ← استبدله بمعرف مستخدم موجود
# }))

# print("\n🔹 Test 2: Duplicate Review (Should FAIL):")
# # نفس البيانات تماماً لمحاكاة التكرار
# print(create_review({
#     "comment": "A wonderful experience, I recommend visiting it!",
#     "rating": 4,
#     "place_id": 1,
#     "user_id": 5
# }))

# print(get_all_users())
# تأكد أن user_id و amenity_id موجودين فعلاً في قاعدة بياناتك قبل التجربة
# print(create_place({
#     "title": "fali",
#     "description": "Wonderful and spacious apartments",
#     "price": 1500.0,
#     "latitude": 21.4225,
#     "longitude": 39.8262,
#     "amenity_id": 5,  # استبدله بمعرف وسيلة راحة موجودة
#     "user_id": 1      # استبدله بمعرف مالك موجود
# }))

# print(create_amenity(
#     {"name": "swiim", "description": "AC in outsied", "images": None}))
# print(create_amenity(
#     {"name": "", "description": "dec", "images": None}))  # خطأ
# valid_user = {
#     "username": "ailnl",
#     "email": "aisl@gml.co",
#     "password": "123456910"
# }
# print("🔹 Test 1: Valid Login (Success):")
# result = login_user("aisl@gml.co", "123456910")
# print(result)
# print("\n" + "#" * 50 + "\n")

# invalid_user = {
#     "username": "ailnl",
#     "email": "aisl@gml.co",
#     "password": "123456910"
# }
# print("🔹 Test 2: Wrong Password (Fail):")
# result_invalid = login_user("ailnl", "124545156910")
# print(result_invalid)
