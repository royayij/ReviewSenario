from statistics import mean


class ExtendedList(list):
    def __gt__(self, other):
        return True if mean(self) > mean(other) else False

    def __lt__(self, other):
        return True if mean(self) < mean(other) else False

    def __le__(self, other):
        return True if mean(self) <= mean(other) else False

    def __ge__(self, other):
        return True if mean(self) >= mean(other) else False

    def __eq__(self, other):
        return True if mean(self) == mean(other) else False

    def __ne__(self, other):
        return True if mean(self) != mean(other) else False

    def __add__(self, other):
        other.extend(self)
        return other


e = ExtendedList((1, 2, 3))
b = ExtendedList((3, 4, 5))
print(b + e)
