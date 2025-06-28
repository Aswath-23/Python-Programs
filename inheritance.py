class Grandparent:
    def swim(self):
        print("swimming")

class Parent:
    def dance(self):
        print("dancing")

class Child(Parent, Grandparent):
    def sing(self,speed):
        super().swim()
        super().dance()
        print("singing",speed)

par= Child()
par.sing(50)


# single level = parent->child
# multi level = grand->parent->child
# multiple = many to one , single class can access other many classes
# hierarchy = one to many, single class gives access to all
# super() = keyword used for calling function from one class to another