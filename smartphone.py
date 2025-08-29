
# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"


# Child Class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # call parent constructor
        self.os = os
        self.storage = storage

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}...")

    def take_photo(self):
        print(f"📷 Taking a photo with {self.device_info()}")

    def phone_info(self):
        return f"{self.device_info()} | OS: {self.os}, Storage: {self.storage}GB"


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S23", "Android", 256)
    phone2 = Smartphone("Apple", "iPhone 15", "iOS", 512)

    print(phone1.phone_info())
    phone1.make_call("0712345678")
    phone2.take_photo()

