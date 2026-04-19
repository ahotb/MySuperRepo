
# التحقق من بيانات المستخدم
def validate_user_data(user_input):
    if not isinstance(user_input, dict):  # التأكد من ان البيانات جايه بشكل قاموس
        return {"is_valid": False, "data": None, "errors": ["The data entered must be in dictionary format."]}
    errors = []  # هئية مكان الاخطأ
    # حلقه تكرارية على الحقول التي نحتاج التأكد منها
    for field in ["username", "email", "password"]:
        # عشان ميسبب كراش ويكون مكان المفتاح الفارغ يحط Noen
        value = user_input.get(field)
        # هنا التأكد من البيانات انها غير  فارغه وانها نص ولايوجد فيه فراغات
        if value is None or not isinstance(value, str) or value.strip() == "":
            # في حال وجود خطأ تظاف على القائمه حقت الاخطأ
            errors.append(f"Missing or empty {field}")
            continue  # هنا نقول له لاتغلق البرنامج بل اكمل
        # هنا اذا تساوى مع اسم المستخدم يتحقق طول الاسم يتراوح من 3 الي 20 حرف
        if field == 'username' and not (3 <= len(value) <= 20):
            errors.append(f"{field} must be between 3 and 20 characters")
            continue
        # هنا التحقق من وجود علامات الايميل او يعيطه خطأ في حال عدم توفرها
        if field == "email" and ("@" not in value or "." not in value):
            errors.append(f"The {field} address is incorrect ")
            continue
        # يتأكد ان الرقم السري ليس اصغر من 8 احرف
        if field == "password" and len(value) < 8:
            errors.append(f"{field} must be at least 8 characters long ")
            continue
    if not errors:  # في حال البيانات صحيحه يرسلها بالشكل هذا
        return {"is_valid": True, "data": user_input, "errors": []}
    else:  # هنا العكس
        return {"is_valid": False, "data": None, "errors": errors}
