import numbers

class Product:
    def __init__(self, name : str, price : float, quantity : int, description : str):
        self.name = name
        self._price = price
        self.quantity = quantity
        self.__description = description
        self.__warn()

    def __str__(self):
        return f"{self.name}"

    @property
    def get_price(self):
        return self._price

    @get_price.setter
    def set_price(self, new_price):
        if isinstance(new_price, int) and new_price >= 0: 
            self._price = new_price
        else:
            print("you cant set this price")
    @property
    def get_description(self):
        return self.__description

    @get_description.setter
    def set_description(self, new_description : str):
        if isinstance(new_description, str):
            self.__description = new_description
        else:
            print(f"Unapropriate description")

    def check_quantity(self):
        return self.quantity >= 10
    
    def __warn(self): #A PATRA LINIE (de aici) PARANTEZA INCHISA
        if not(isinstance(self.get_price, numbers.Real)\
            and isinstance(self.quantity, int)\
            and isinstance(self.name, str) \
            and isinstance(self.get_description, str)) \
            or self.get_price < 0\
            or self.quantity < 0:
            print(f"Este o eroare la introducerea obiectului {self.name} \n Locatia : {hex(id(self))}")
    
