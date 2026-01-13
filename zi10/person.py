from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email, adress):
        self.name = name
        self.__email = email
        self.__adress = adress

    @property
    def get_email(self):
        return self.__email

    @get_email.setter
    def set_email(self, new_email):
        self.__email = new_email

    @property
    def get_adress(self):
        return self.__adress

    @get_adress.setter
    def set_adress(self, new_adress):
        self.__adress = new_adress 

    def check_email(self):
        return "@" in self.__email

    @abstractmethod
    def display_info(self):
        pass




