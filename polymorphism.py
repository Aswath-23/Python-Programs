#run time poly
from pkg_resources import non_empty_lines


class Parent:

     def drive(self):
         print('Parent Driving')

class Child:
     def drive(self):
         print('Child Driving')

obj=None
name=input('Enter your name: ')
if name=='parent':
    obj=Parent()
else:
    obj=Child()

obj.drive()