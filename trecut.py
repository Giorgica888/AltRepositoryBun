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


class Order(ABC):
    def calculate_total(self):
        pass

    def send_confirmation(self):
        pass

class OnlineOrder(Order):
    def __init__(self, products : list):
        #checking the list
        self.products = products


    def calculate_total(self):
        sum = 0
        for i in self.products:
            sum += i
        print(sum)

    def send_confirmation(self, value : float):
        print(f"Invoice : {value} |||| With products: \n {self.products} Those are on they'r way to you :)")

class InStoreOrder(Order):
    def __init__(self, products : list):
        #checking the list
        self.products = products
        self.total_sum = 0


    def calculate_total(self):
        sum = 0
        for i in self.products:
            sum += i
        self.total_sum = sum
        print(self.total_sum)

    def send_confirmation(self):
        print(f"Shop SRL")
        sum = 0
        for i in self.products:
            print(i)
        print(f"Total : {self.total_sum}")
        self.total_sum = 0


    

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

    geaca = OnlineOrder([2, 3, 4])
    geaca.calculate_total()

    order2 = InStoreOrder([4, 2, 4])
    order2.calculate_total()
    order2.send_confirmation()



