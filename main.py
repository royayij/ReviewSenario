import codecs
import csv
from urllib.request import urlopen

from import_data import insert_iris_list
from list_extend import ExtendedList


def main():
    url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
    stream = urlopen(url)
    csv_file = csv.reader(codecs.iterdecode(stream, 'utf-8'))
    iris_lst = []
    [iris_lst.append(ExtendedList(raw)) for raw in csv_file]

    for item in iris_lst:
        iris_value_list = []
        converted_iris_lst = ExtendedList.next_val(item)
        for element in converted_iris_lst:
            iris_value_list.append(element)
        if len(iris_value_list) == 0:
            continue
        else:
            iris_value_list = tuple(iris_value_list)

        insert_iris_list(iris_value_list)

    print('Done!')


if __name__ == '__main__':
    main()
