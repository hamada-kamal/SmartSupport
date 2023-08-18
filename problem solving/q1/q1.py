'''
************************ exeplanations*****************
the function starts with a base case: if num is zero, it returns '0' as the hexadecimal representation.
the function initializes a variable hex_chars with the characters '0123456789ABCDEF', which represent
the hexadecimal digits.
the function enters a loop, where it repeatedly divides num by 16 and keeps track of the remainders.
the remainders are then used as indices to select the corresponding hexadecimal digit from hex_chars, 
which is appended to the left of the hex_num string.
finally, the function returns hex_num, which is the hexadecimal representation of num in lowercase.
'''

def num_to_hex(num):
    if num == 0:
        return '0'
    elif num < 0:
        num = (~num) + 1
    hex_chars = '0123456789ABCDEF'
    hex_num = ''

    while num > 0:
        
        remainder = num % 16
        hex_num = hex_chars[remainder] + hex_num
        num //= 16

    return hex_num.lower()
#test
print(num_to_hex(70))


