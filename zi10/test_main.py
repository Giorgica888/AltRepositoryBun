from person import Person
from employee import Emplyee
from product import Product
# timy = Person("timi", "timie@timie.com", "somewhere")
# timy.set_email = "222@gmail.com"
# timy.set_adress = "not here"
# print(timy.get_email)
# print(timy.get_adress)
# print(timy.check_email())

angajat = Emplyee("john", "dsd@gmail.com", 2000, "kalorie")

angajat.incease_salary(10)
print(angajat.get_salary)
angajat.display_info()

