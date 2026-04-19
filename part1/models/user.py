

def validate_user_data(user_input):
    if not isinstance(user_input, dict):
        return user_input
    errors = []

    for field in ["username", "email", "password"]:
        # عشان ميسبب كراش ويكون مكان المفتاح الفارغ يحط Noen
        value = user_input.get(field)
        if value is None or not isinstance(value, str) or value.strip() == "":
            errors.append(f"Missing or empty {field}")
            continue
        if field == 'username' and not (3 <= len(value) <= 20):
            errors.append(f"{field} is short ")
            continue
        if field == "email" and ("@" not in value or "." not in value):
            errors.append(f"The {field} address is incorrect ")
            continue
        if field == "password" and len(value) < 8:
            errors.append(f"The {field} is wrong ")
            continue
    return errors
