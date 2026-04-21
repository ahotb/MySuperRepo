from data.initial_data import init_schema
from services.user_service import register_user, login_user
from core.database import fetch_all

if __name__ == "__main__":
    init_schema()

    valid_user = {
        "username": "ailnl",
        "email": "aisl@gml.co",
        "password": "123456910"
    }
    print("🔹 Test 1: Valid Login (Success):")
    result = login_user("aisl@gml.co", "123456910")
    print(result)
    print("\n" + "#" * 50 + "\n")

    invalid_user = {
        "username": "ailnl",
        "email": "aisl@gml.co",
        "password": "123456910"
    }
    print("🔹 Test 2: Wrong Password (Fail):")
    result_invalid = login_user("ailnl", "124545156910")
    print(result_invalid)
