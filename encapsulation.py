# public - all classs can access
# private - used within main class only (__) is added to make it private , will not restrict developer should understand
# protected - used within parent and child class (-) is added to make it protected
# Hiding the info which should be hided

class School:
    def __init__(self):
        self.name = 'ABC'
        self._place = 'coimbatore'
        self.__revenue= 10000



s = School()
print(s.name)
print(s._place)
print(s.__revenue)