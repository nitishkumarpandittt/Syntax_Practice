# class Bag:
#     def __init__(self, name, material, zips, pockets):
#         self.name = name
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"{self.name}'s material is {self.material}, having zips and pocket {self.zips} and {self.pockets} respectively.")

# # objects 
# reebok = Bag("reebok", "leather", 3, 5)
# campus = Bag("campus", "nylon", 4, 4)

# # method calling
# reebok.show()
# campus.show()


class Animal:
    def show(self):
        print("Hello World")

    name = "Nitish"

    @classmethod
    def sh(cls):
        print(f"class method and name is {cls.name}")

    @staticmethod
    def showww():
        print(f"Hello India and name is {name}")
    a = 10

obj = Animal()

obj.showww()