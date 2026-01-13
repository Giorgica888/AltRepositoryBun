from importator import *

cana  = Product(name = "cana", price = 10, quantity = 2, description = "cana ultra mica, numai buna de pus pe masa")
farfurie = Product(name = "farfurie", price = 12, quantity =  230, description = "e doar o farfurie, nimic mai special")
bancomat = Product(name = "bancomat", price = 13, quantity = 4, description = "De unde avem asa ceva pe stoc???")
laptop = Product(name = "Laptop HP", price = 1222, quantity = 29, description = "se programeaza bine pe el")
plus_gigant = Product(name = "Ursulet", price = 120, quantity = 40, description = "E cat patul tau :)")

angajat1 = Employee(name = "Ionel", email = "Ionel@gmail.com", salary = 2900, adress = "chiajna")
angajat2 = Employee(name = "Tanti Nuti, sotia lui Ionel", email = "ngmail.com", salary = 2901, adress ="chiajna" )

userx = User(name= "jon", username = "jon16", phone = "236000", adress = "Undeva", email= "sdsds@gmail.com")
usery = User(name= "Kati", username = "katrina23", phone = "07888888888888", adress = "PrinBucuresti", email= "3232 not at gmail.com")
userz = User(name= "loc", username = "lacatus20", phone = "2313123123", adress = "America", email= "amrica@america.com")

products = [cana, farfurie, bancomat, laptop, plus_gigant]
employes = [angajat1, angajat2]
users = [userx, usery, userz]


#######################
for i in products: 
    userx.add_product(i)
usery.add_product(laptop)
userz.add_product(plus_gigant)
for i in userx.shopping_history:
    print(i, end = " ")
print()


#################
for i in users:
    print(i.total_spent())


##############
for i in users:
    print()
    i.display_info()

for i in employes:
    print()
    i.display_info()

#######################
angajat1.set_salary = 2300
print(angajat1.get_salary)

laptop.set_price = 200
print(laptop.get_price)

    
