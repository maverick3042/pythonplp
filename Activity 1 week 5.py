class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def take_photo(self):
        return f"Taking a photo with {self.brand} {self.model}."

class SuperSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_quality):
        super().__init__(brand, model, storage)
        self.camera_quality = camera_quality

    def take_photo(self):
        return f"Taking a high-quality photo with {self.camera_quality} MP camera on {self.brand} {self.model}."
