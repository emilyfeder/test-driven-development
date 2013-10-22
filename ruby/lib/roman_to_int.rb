require 'debugger'
class RomanToInt

INT_VALUE = { "I" => 1, "V" => 5, "X" => 10, "L" => 50, "C" => 100, "D" => 500,
              "M" => 1000, "*" => 0}

  def self.parse(roman)
     roman = roman.upcase
     if not whole_string_valid(roman)
       return -1
     else
       return int_value(roman)
     end
  end

  def self.whole_string_valid(roman)
    # Checks the validity of the roman numeral using whole string operations without
    # doing the same kind of iteration as in int_value.
    roman.each_char do |c|
      return false if !INT_VALUE.has_key?(c)
    end

    if /IIII|XXXX|CCCC|MMMM/ =~ roman
      return false
    end

    if roman.count('V') > 1 || roman.count('L') > 1 || roman.count('D') > 1
      return false
    end

    # When using subtractive notation, the smaller value to be subtracted
    # should only be one order of magnitude smaller the the numeral it precedes.
    if /IL|IC|ID|IM|XD|XM/ =~ roman
      return false
    end

    # Subtractive notation containing I (i.e. IX) should only be found at the end
    # of the roman numeral string
    if /IX/.match(roman) && !/IX$/.match(roman)
      return false
    end

    # Half step numerals V, L, and D cannot be on the left side of subtractive notation
    if /VX|VL|VC|VD|VM|LC|LD|LM|DM/ =~ roman
      return false
    end

    return true
  end

  def self.int_value(roman)
    # Loops through the letters in the string to parse the integer value out of the
    # roman numeral. Returns -1 if roman numeral is invalid. Else returns its integer
    # value.

    # IMPORTANT: Assumes whole string checks have already been done! Cannot be used as
    # a standalone way of getting the int value.

    # Here we define a 'digit' in roman numerals. For example, two numerals
    # combined with subtractive such as 'IX' are taken to be one digit.

    # The string shifted ahead by 1 character with * appended to the end
    shifted_ahead = roman.slice(1, roman.size-1) << "*"
    # Running total of the integer value
    total = 0
    # Maintain value of last digit parsed for checking
    last_digit_total = nil
    banned = []
    i = 0
    while i < roman.size
      currnum = roman[i]
      nextnum = shifted_ahead[i]
      if banned.include?(currnum + nextnum)
        return -1
      end
      # If subtractive notation
      if /IV|IX|XL|XC|CD|CM/.match(currnum + nextnum)
        digit_total = INT_VALUE[nextnum] - INT_VALUE[currnum]
        # Since these characters have been used in subtractive notation, they now cannot
        # be used as a combination in the rest of the roman numeral string
        banned.push(currnum+nextnum)
        i+=1
      else
        digit_total = INT_VALUE[currnum]
      end
      # Digit values should decrease to the right
      if last_digit_total && digit_total > last_digit_total
        return -1
      end
      total += digit_total
      last_digit_total = digit_total
      i+=1
    end
    return total
  end

  def self.parse_file(input_fname, output_fname)
  end

end
