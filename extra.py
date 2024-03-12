def jstr(var):
    string = ''
    if type(var) is dict:
        for key, value in var.items():
            string += f'{str(key)}: {str(value)}\n'
    elif type(var) is list:
        for value in var:
            string += str(value) + '\n'
    return string


if __name__ == '__main__':
    dictionary = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
    }
    print('Testin: '+str(type(dictionary)))
    print('Input: ' + str(dictionary))
    print('Output: \n'+jstr(dictionary))
    lists = ['list value 1', 'list value 2', 3, 4]
    print('Testin: '+str(type(lists)))
    print('Input: ' + str(lists))
    print('Output: \n'+jstr(lists))
        

