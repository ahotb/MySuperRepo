
class Amenity:
    def __init__(self, id=None, name=None, description=None, images=None):
        self.id = id
        self.name = name
        self.description = description
        self.images = images
        self.errors = []
        self._validate()

    def _validate(self):
        if not self.name or not isinstance(self.name, str) or self.name.strip() == "":
            self.errors.append("Missing or empty name")
        if not self.description or not isinstance(self.description, str) or self.description.strip() == "":
            self.errors.append("Missing or empty description")

    def is_valid(self):
        return len(self.errors) == 0

    def get_errors(self):
        """ترجع قائمة الأخطاء للـ Service عشان يعرضها"""
        return self.errors

    def to_dict(self):
        """تحويل بيانات الكائن لقاموس جاهز للإرسال أو الحفظ"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "images": self.images
        }
