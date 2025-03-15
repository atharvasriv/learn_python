import numpy_file as np


def main():
    def calculator_python():
        # Addition and Subtraction
        addition = 5 + 5
        subtraction = 5 - 5
        print(addition, subtraction)
        # Multiplication and Division
        multiplication = 5 * 5
        division = 5 / 5
        print(multiplication, division)
        # Exponentiation and Modulo
        exponentiation = 5 ** 5
        modulo = 5 % 5
        print(exponentiation, modulo)

    def calculate_bmi():
        height = 1.58
        weight = 53.4
        bmi = weight/height ** 2

        print(bmi)

    def data_types():
        string_str = 'this is a string'
        integer_int = 5
        boolean_bool = True
        float_float = 1.89
        print(string_str, integer_int, boolean_bool, float_float)

    def lists():
        some_data = [['data', 1.2],
                     ['more data', 1],
                     ['even more data', True],
                     ['too much data', 'data']]
        some_data[3] = ['too much data', 'data but changed']
        some_data_ext = some_data + [['oh look, even more data', 'data']]
        del(some_data[3])
        y_referenced_list = some_data
        y_other_list = list(some_data)
        index_for_some_data = some_data.index(['more data', 1])
        count_for_some_data = some_data.count(['data', 1.2])
        print(y_referenced_list)
        print(y_other_list)
        print(index_for_some_data)
        print(count_for_some_data)
        print(some_data)
        print(some_data[0])
        print(some_data[0:2])
        print(some_data_ext)

    def functions():
        string = 'yes'
        type(string)

    def methods():
        print('some methods in lists() (index_for_some_data and count_for_some_data)')
        string = 'stir'
        print(string)
        string_capitalized = string.capitalize()
        print(string_capitalized)
        string_changed = string.replace('ir', 'irring')
        print(string_changed)

    calculator_python()
    calculate_bmi()
    data_types()
    lists()
    functions()
    methods()


main()
