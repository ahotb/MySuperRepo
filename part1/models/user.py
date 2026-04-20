
class User:
    def __init__(self, username=None, email=None, password=None, role="user", user_id=None):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.errors = []
        self._validate()

    def _validate(self):

        # هنا التأكد من البيانات انها غير  فارغه وانها نص ولايوجد فيه فراغات
        if not self.username or not isinstance(self.username, str) or self.username.strip() == "":
            # في حال وجود خطأ تظاف على القائمه حقت الاخطأ
            self.errors.append("Missing or empty username")
        elif (3 <= len(self.username.split()) <= 20):
            self.errors.append("username must be between 3 and 20 characters")
        #  فحص البريد الإلكتروني
        if not self.email or not isinstance(self.email, str) or not self.email.strip():
            self.errors.append("Missing or empty email")
        elif "@" not in self.email or "." not in self.email:
            self.errors.append("The email address is incorrect")

        #  فحص كلمة المرور
        if not self.password or not isinstance(self.password, str) or not self.password.strip():
            self.errors.append("Missing or empty password")
        elif len(self.password) < 8:
            self.errors.append(
                "Password must be at least 8 characters long")

    def is_valid(self):
        """ترجع True إذا ما فيه أخطاء، False إذا فيه"""
        return len(self.errors) == 0

    def get_errors(self):
        """ترجع قائمة الأخطاء للـ Service عشان يعرضها"""
        return self.errors

    def to_dict(self):
        """تحويل بيانات الكائن لقاموس جاهز للإرسال أو الحفظ"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "role": self.role
        }


class Owner(User):
    pass


class Admin(User):
    pass
