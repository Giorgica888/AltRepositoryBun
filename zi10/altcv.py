class Data:
    def __float__(self):
        return 42.42 # not a float!


x = Data()
res = float(x) 

print(res)