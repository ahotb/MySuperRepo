from data.initial_data import init_schema
from services.user_service import register_user

if __name__ == "__main__":
    init_schema()

    # 1. بيانات المستخدم الأساسي (تبقى نظيفة بدون role)
    valid_user = {
        "username": "ailnl",
        "email": "aisl@gml.co",
        "password": "123456910"
    }
    result = register_user(valid_user)
    print(result)
    print("\n" + "#" * 50 + "\n")

    # 3. بيانات خاطئة للاختبار
    invalid_user = {
        "username": "abood",
        "email": "ail@gmco",
        "password": "12345678910"
    }
    print("🔹Error")
    result_invalid = register_user(invalid_user)
    print(result_invalid)
