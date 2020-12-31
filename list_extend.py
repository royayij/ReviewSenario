from statistics import mean


class ExtendedList(list):
    def __init__(self, lst):
        self.lst = lst

    def __gt__(self, other):
        return mean(self.lst) > mean(other.lst)

    def __lt__(self, other):
        return mean(self.lst) < mean(other.lst)

    def __le__(self, other):
        return mean(self.lst) <= mean(other.lst)

    def __ge__(self, other):
        return mean(self.lst) >= mean(other.lst)

    def __eq__(self, other):
        return  mean(self.lst) == mean(other.lst)

    def __ne__(self, other):
        return mean(self.lst) != mean(other.lst)

    def __add__(self, other):
        lst_new = []
        lst_new.extend(self.lst)
        lst_new.extend(other.lst)
        return lst_new

    @staticmethod
    def next_val(ex_list):
        result = iter(ex_list)
        while True:
            try:
                data = next(result)
            except StopIteration:
                break
            else:
                try:
                    yield float(data)
                except ValueError:
                    break


class TypeList(ExtendedList):
    def __eq__(self, other):
        return self.lst[-1] == other.lst[-1]

    def __ne__(self, other):
        return self.lst[-1] != other.lst[-1]
