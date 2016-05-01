__author__ = 'neilson.ramalho'
class Counter:
    __privateAttribute = 34

    def count(self, value):
        self.__privateAttribute = value
        print(self.__privateAttribute)

counter = Counter()
counter.count(23)
counter.count(21)
# print(counter.__privateAttribute)
print(counter._Counter__privateAttribute)

