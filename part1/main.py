from services.user_service import register_user
from data.initial_data import init_schema
if __name__ == "__main__":
    init_schema()
    valid_user = {"username": "aill",
                  "email": "ail@gml.co",
                  "password": "12345678910"}
    invalid_user = {"username": "abood",
                    "email": "ail@gmco",
                    "password": "12345678910"}

    result_valid = register_user(valid_user)
    print(result_valid)
    print("#" * 50)
    result_invalid = register_user(invalid_user)
    print(result_invalid)
