
def decode(string):
    original = ''
    for i in range(0, len(string)):
        if string[i] == '1':
            original += '8'
        if string[i] == '2':
            original += '9'
        if string[i] == '3':
            original += '0'
        if string[i] == '4':
            original += '1'
        if string[i] == '5':
            original += '2'
        if string[i] == '6':
            original += '3'
        if string[i] == '7':
            original += '4'
        if string[i] == '8':
            original += '5'
        if string[i] == '9':
            original += '6'
        if string[i] == '0':
            original += '7'
    return original


 

