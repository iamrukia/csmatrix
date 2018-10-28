"""
An 11-symbol message has been encrypted as follows. Each symbol is
represented by a number between 0 and 26 (A -> 0, B -> 1, ..., Z -> 25, space -> 26).
Each number is represented by a five-bit binary sequence ( 0 -> 00000, 1 -> 00001, ..., 26 -> 11010). Finally,
the resulting sequence of 55 bits is encrypted using a flawed version of the one-time pad:
the key is not 55 random bits but 11 copies of the same sequence of 5 random bits.
The cyphertext key is not 55 randoms bits but 11 copies of the same sequence of 5 random bits. The cyphertext is
10101 00100 10101 01011 11001 00011 01011 10101 00100 11001 11010
Try to find the plain text
"""
from chap1.GF2 import one
from chap1.GF2 import zero


# return single letter in str with given key
def get_original_char_with_key(trail_key, word):
    key_list = [int(x) for x in trail_key]
    word_char_list = [int(y) for y in word]

    new_key_list = [one if x == 1 else zero for x in key_list]
    new_word_char_list = [one if x == 1 else zero for x in word_char_list]

    result_list = [new_word_char_list[i] - new_key_list[i] for i in range(len(new_word_char_list))]
    new_result_list = [1 if x == one else 0 for x in result_list]
    return_result = ''.join(str(k) for k in new_result_list)
    return convert_to_string_from_binary(return_result)


# return the text with given trail_key (string)
def get_original_bits_with_key(trail_key, encrypted_text):
    result_text = ''
    for word in encrypted_text:
        result_text = result_text + get_original_char_with_key(trail_key, word)
    return result_text


# convert binary to string
def convert_to_string_from_binary(binary_text):
    char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    boundary = int(binary_text, 2)
    return char_list[boundary] if boundary <= 26 else '-'


def enumerate_all_possibilities():
    return ['{0:05b}'.format(x) for x in range(32)]


S = ['10101', '00100', '10101', '01011', '11001', '00011', '01011', '10101', '00100', '11001', '11010']

# print(get_original_bits_with_key('10101', S))
# eve is evil
for possible_key in enumerate_all_possibilities():
    print(get_original_bits_with_key(possible_key, S))
