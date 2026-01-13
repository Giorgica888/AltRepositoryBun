from person import Person
from product import Product
import numbers
class User(Person):
    def __init__(self, name, email, username, phone, adress):
        super().__init__(name, email, adress)
        self.phone = phone
        self.username = username
        self.shopping_history = []
        self.__warn()

    @property
    def get_phone(self):
        return self.phone

    @get_phone.setter
    def set_phone(self, new_phone):
        if isinstance(new_phone, str):
            self.phone = new_phone

    def add_product(self, product : Product):
        if isinstance(product, Product):
            self.shopping_history.append(product)
        else:
            print(f"wrong product introduced")

    def total_spent(self):
        sum = 0
        for i in self.shopping_history:
            sum += i.get_price
        return sum

    def display_info(self):
        print(f"Name : {self.name} | Email : {self.get_email} |  Username : {self.username}")
        print(f"Phone : {self.get_phone} | Adress {self.get_adress}")

    
    def __warn(self):
       if not(
        isinstance(self.name, str)\
        and isinstance(self.username, str)\
        and isinstance(self.get_phone, str) \
        and isinstance(self.get_adress, str)\
        and isinstance(self.get_email, str)
       ):
            print(f"Este o eroare la introducerea obiectului {self.name} \n \
             Locatia : {hex(id(self))}")

            
    
        

    