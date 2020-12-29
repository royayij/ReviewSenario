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


class TypeList(ExtendedList):
    def __eq__(self, other):
        return True if self[-1] == other[-1] else False

    def __ne__(self, other):
        return True if self[-1] != other[-1] else False



