

class Place:
    def __init__(self, id=None, title=None, description=None, price=None, latitude=None, longitude=None, amenity_id=None, user_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_id = amenity_id
        self.user_id = user_id
        self.errors = []
        self._validate()

    def _validate(self):
        if not self.title or not isinstance(self.title, str) or self.title.strip() == "":
            # في حال وجود خطأ تظاف على القائمه حقت الاخطأ
            self.errors.append("Missing or empty title")
        if not self.description or not isinstance(self.description, str) or self.description.split() == "":
            self.errors.append("missing or empty description")
        if not isinstance(self.price, (float, int)) or self.price <= 0:
            self.errors.append("Price must be a number greater than 0")
        if not self.Latitude or not isinstance(self.Latitude, (float, int)) or not (-90 <= self.latitude <= 90):
            self.errors.append("Latitude must be between -90 and 90")
        if not self.Longitude or not isinstance(self.Longitude, (float, int)) or not (-180 <= self.Longitude <= 180):
            self.errors.append("Longitude must be between -180 and 180")

        if self.amenity_id is None:
            self.errors.append("Amenity ID is required")
        if self.user_id is None:
            self.errors.append("User ID (Owner) is required")

    def is_valid(self):
        return len(self.errors) == 0

    def get_errors(self):
        return self.errors

    def to_dict(self):
        return {"id": self.id,
                "title": self.title,
                "description": self.description,
                "price": self.price,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "amenity_id": self.amenity_id,
                "user_id ": self.user_id}
