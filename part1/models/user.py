
# التحقق من بيانات المستخدم
def validate_user_data(user_input):
    if not isinstance(user_input, dict):  # التأكد من ان البيانات جايه بشكل قاموس
        return {"is_valid": False, "data": None, "errors": ["The data entered must be in dictionary format."]}
    errors = [] # هئية مكان الاخطأ 
    # حلقه تكرارية على الحقول التي نحتاج التأكد منها 
    for field in ["username", "email", "password"]:
        # عشان ميسبب كراش ويكون مكان المفتاح الفارغ يحط Noen
        value = user_input.get(field)
		# هنا التأكد من البيانات انها غير  فارغه وانها نص ولايوجد فيه فراغات 
        if value is None or not isinstance(value, str) or value.strip() == "":
            errors.append(f"Missing or empty {field}") # في حال وجود خطأ تظاف على القائمه حقت الاخطأ
            continue # هنا نقول له لاتغلق البرنامج بل اكمل 
        if field == 'username' and not (3 <= len(value) <= 20): # هنا اذا تساوى مع اسم المستخدم يتحقق طول الاسم يتراوح من 3 الي 20 حرف
            errors.append(f"Username must be between 3 and 20 characters")
            continue
        if field == "email" and ("@" not in value or "." not in value): # هنا التحقق من وجود علامات الايميل او يعيطه خطأ في حال عدم توفرها
            errors.append(f"The {field} address is incorrect ")
            continue
        if field == "password" and len(value) < 8: # يتأكد ان الرقم السري ليس اصغر من 8 احرف
            errors.append(f"The {field} is wrong ")
            continue
    if not errors: # في حال البيانات صحيحه يرسلها بالشكل هذا 
        return {"is_valid": True, "data": user_input, "errors": []}
    else: # هنا العكس
        return {"is_valid": False, "data": None, "errors": errors}
