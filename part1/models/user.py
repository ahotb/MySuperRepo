
# التحقق من بيانات المستخدم
def validate_user_data(user_input):
    if not isinstance(user_input, dict):  # التأكد من ان البيانات جايه بشكل قاموس
        return {"is_valid": False, "data": None, "errors": ["The data entered must be in dictionary format."]}
    errors = []

    for field in ["username", "email", "password"]:
        # عشان ميسبب كراش ويكون مكان المفتاح الفارغ يحط Noen
        value = user_input.get(field)
        if value is None or not isinstance(value, str) or value.strip() == "":
            errors.append(f"Missing or empty {field}")
            continue
        if field == 'username' and not (3 <= len(value) <= 20):
            errors.append(f"Username must be between 3 and 20 characters")
            continue
        if field == "email" and ("@" not in value or "." not in value):
            errors.append(f"The {field} address is incorrect ")
            continue
        if field == "password" and len(value) < 8:
            errors.append(f"The {field} is wrong ")
            continue
    if not errors:
        return {"is_valid": True, "data": user_input, "errors": []}
    else:
        return {"is_valid": False, "data": None, "errors": errors}
