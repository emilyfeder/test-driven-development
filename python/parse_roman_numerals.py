import re
import pdb
INT_VALUE = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "*":0}  

def parse_roman_numeral_file(input_fname, output_fname):
    """Given a filename, translate roman numerals to their integer
    values and output a file where each line has the same integer
    value as the respective line of roman numerals in the input file."""
    inputf = open(input_fname, 'r')
    outputf = open(output_fname, 'w')
    for line in inputf.readlines():
        result_int = roman_numeral_to_int(line.strip())
        if result_int > 0:
            outputf.write(str(result_int))
        else:
            outputf.write('****')
        outputf.write('\n')
    inputf.close()
    outputf.close()
    return 0

def roman_numeral_to_int(roman):
    """Given a string representation of a roman numeral, output the
    equivalent integer value. Return a negative number if input is
    invalid roman numeral.
    Max number which can be represented: 3899
    
    """
    roman = roman.upper()
    if not whole_string_valid(roman):
        return -1
    else:
        return int_value(roman)

def whole_string_valid(roman):
    """Checks the validity of the roman numeral using whole string operations without
    doing the same kind of iteration as in int_value."""

    # Should only contain valid ruman numeral characters of I,V,X,L,D,
    for char in roman:
        if char not in INT_VALUE:
            return False

    # I, X, C, M should not be found more than 3 times in a row
    if re.search('IIII|XXXX|CCCC|MMMM', roman):
        return False

    # V, L, D should not be found more than once
    if roman.count('V') > 1 or roman.count('L') > 1 or roman.count('D') > 1:
        return False

    # When using subtractive notation, the smaller value to be subtracted
    # should only be one order of magnitude smaller the the numeral it precedes.
    if re.search('IL|IC|ID|IM|XD|XM', roman):
        return False

    # Subtractive notation containing I (i.e. IX) can only be found at the end of the
    # roman numeral string
    if re.search('IX', roman) and not re.search('IX$', roman):
        return False

    # Half step numerals V, L, and D cannot be on the left side of subtractive notation.
    if re.search('VX|VL|VC|VD|VM|LC|LD|LM|DM', roman):
        return False

    return True

def int_value(roman):
    """Loops through the letters in the string to parse the integer value out of the
    roman numeral. Returns -1 if roman numeral is invalid. Else returns its integer
    value.

    IMPORTANT: Assumes whole string checks have already been done! Cannot be used as
    a standalone way of getting the int value.

    Here we define a 'digit' in roman numerals. For example, two numerals
    combined with subtractive such as 'IX' are taken to be one digit."""

    # the roman numeral string shifted ahead by one character
    shift_ahead = roman[1:] + "*"
    total = 0 # running total of the integer value
    last_digit_total = None # we want to maintain this for checking
    banned = []
    i = 0
    while i < len(roman):
        if (roman[i] + shift_ahead[i]) in banned:
            return -1
        # if subtractive notation
        if re.search('IV|IX|XL|XC|CD|CM', roman[i] + shift_ahead[i]):
            # Take this and next character as one digit
            digit_total = INT_VALUE[shift_ahead[i]] - INT_VALUE[roman[i]]
            # Since these characters have been used in subtractive notation, they now cannot
            # be used as a combination in the rest of the roman numeral string
            banned.append(roman[i] + shift_ahead[i])
            i += 1
        else:
            digit_total = INT_VALUE[roman[i]]
        if last_digit_total and digit_total > last_digit_total: # Digit values should decrease to the right
            return -1
        total += digit_total
        last_digit_total = digit_total
        i += 1

    return total

