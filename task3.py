# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(string):
    encode_string = ''
    count = 1
    if string != '':
        for i in range(1, len(string)):
            if string[i] == string[i-1]:
                count += 1
            else:
                if count > 1:
                    encode_string += str(count)+string[i-1]
                    count = 1
                else:
                    encode_string += string[i-1]
                    count = 1
        if count == 1:
            encode_string += string[-1]
        else:
            encode_string += str(count) + string[-1]
    return encode_string


def decode(string):
    decode_string = ''
    count = 1
    for i in range(len(string)):
        if string[i].isdigit():
            count = int(string[i])
        else:
            if count > 1:
                decode_string += count*string[i]
                count = 1
            else:
                decode_string += string[i]
                count = 1
    return decode_string


with open('input.txt', 'r') as file:
    string = file.read()

with open('output.txt', 'w') as file:
    file.write(f'Encode string -->\t{encode(string)}')
    file.write(f'\nDecode string -->\t{decode(encode(string))}')

print(f'\nInput string  -->\t{string}')
print(f'\nEncode string -->\t{encode(string)}')
print(f'\nDecode string -->\t{decode(encode(string))}')
