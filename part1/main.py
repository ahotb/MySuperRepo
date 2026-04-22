from data.initial_data import init_schema
from services.user_service import register_user, login_user, get_all_users
from core.database import fetch_all
from services.amenity_service import create_amenity
from services.place_service import create_place

if __name__ == "__main__":
    init_schema()

    # print(get_all_users())
# تأكد أن user_id و amenity_id موجودين فعلاً في قاعدة بياناتك قبل التجربة
print(create_place({
    "title": "fali",
    "description": "Wonderful and spacious apartments",
    "price": 1500.0,
    "latitude": 21.4225,
    "longitude": 39.8262,
    "amenity_id": 5,  # استبدله بمعرف وسيلة راحة موجودة
    "user_id": 1      # استبدله بمعرف مالك موجود
}))

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
