from abc import ABC, abstractmethod

class OnlineProduct(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def display_details(self):
        pass

class DigitalProduct(OnlineProduct):

    def __init__(self, name, price, file_size):
        self.name = name
        self.price = price
        self.file_size = file_size

    def calculate_discount(self):
        return self.price * 0.10  # 10% reducere la produsele digitale

    def display_details(self):
        print(f"Digital Product: {self.name}, Price: ${self.price}, File Size: {self.file_size}MB")

class PhysicalProduct(OnlineProduct):

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def calculate_discount(self):
        return self.price * 0.05  # 5% reducere la produsele fizice

    def display_details(self):
        print(f"Physical Product: {self.name}, Price: ${self.price}, Weight: {self.weight}kg")

class SubscriptionProduct(OnlineProduct):
    def __init__(self, name, price, duration):
        self.name = name
        self.duration = duration
        self.discount = 15/100
        self.price = price

    def calculate_discount(self):
        return self.price - self.price * self.discount

    def display_details(self):
        print(f"{self.name} costs {self.calculate_discount()} with {self.discount} discount.\n Subscription duration : {self.duration}")

    

if __name__ == "__main__":

    ebook = DigitalProduct("E-book on Python", 20, 15)

    laptop = PhysicalProduct("Gaming Laptop", 1500, 2.5)
    ebook.display_details()

    laptop.display_details()
    print(f"Discount for {ebook.name}: ${ebook.calculate_discount()}")

    print(f"Discount for {laptop.name}: ${laptop.calculate_discount()}")

    gym = SubscriptionProduct("subscription", 50, 30)

    gym.display_details()
    print(gym.calculate_discount())



