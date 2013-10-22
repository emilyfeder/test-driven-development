require_relative '../lib/roman_to_int'

DATA_DIR = File.dirname(File.absolute_path(__FILE__))
TEST_PATH = File.join(DATA_DIR, 'test_file.txt')
TEST_RESULTS_PATH = File.join(DATA_DIR, 'test_results.txt')
EXPECTED_PATH = File.join(DATA_DIR, 'expected_results.txt')

def actual_results
  File.read(TEST_RESULTS_PATH).split("\n")
end

def expected_results
  File.read(EXPECTED_PATH).split("\n")
end

describe RomanToInt do
  
  describe ".parse" do

    {
      'I' => 1,
      'V' => 5,
      'X' => 10,
      'L' => 50,
      'C' => 100,
      'D' => 500,
      'M' => 1000,
      'II' => 2,
      'XX' => 20,
      'CC' => 200,
      'MM' => 2000,
      'IV' => 4,
      'IX' => 9,
      'XC' => 90,
      'CD' => 400,
      'CM' => 900,
      'VI' => 6,
      'VIII' => 8,
      'LI' => 51,
      'LX' => 60,
      'CI' => 101,
      'CX' => 110,
      'CL' => 150,
      'CLX' => 160,
      'DI' => 501,
      'DX' => 510,
      'DC' => 600,
      'MI' => 1001,
      'MX' => 1010,
      'MC' => 1100,
      'MD' => 1500,
      'viII' => 8,
      'XXIX' => 29,
      'DCCCXIV' => 814,
      'MDCXI' => 1611,
      'MMDXCIX' => 2599,
      'XXXIII' => 33,
      'CMVIII' => 908,
      'XXXIX' => 39,
      'XCIX' => 99,
      'CCCXLIX' => 349,
      'MCMLV' => 1955,
      'mmmd' => 3500,
      'MMMCM' => 3900
    }.each do |roman, int|
      it "correctly parses #{roman} to #{int}" do
        RomanToInt.parse(roman).should == int
      end
    end

    [ 
      'IM',
      'IC',
      'IL',
      'LM',
      'XM',
      'IIII',
      'VV',
      'DD',
      'XICDL',
      'DLD',
      'LC',
      'MLC',
      'MCCCIC',
      'MCXXC',
      'CLIIX',
      'CIXI',
      'CIIV'
    ].each do |roman|
      it "determines #{roman} is invalid" do
        RomanToInt.parse(roman).should == -1
      end
    end
  end

  describe ".whole_string_valid" do
    [
      'ABCD', # string should only contain valid characters
      'XXKV',
      '-1ii',
      'ZZMM',
      'MMMM', # No more than 3 of the same numerals in a row
      'CCCC',
      'CXXXX',
      'LIIII',
      'LIC', # Invalid cases of subtractive notation
      'MID',
      'XM',
      'MMMIM',
      'VLI', # Half step numerals cannot be on the left side of subtractive notation
      'MLC',
      'DM',
      'VV', # Each half step numeral cannot be repeated more than once in a string
      'CLLV',
      'MMDD',
      'MDMD',
      'LIXL',
      'CIXI', # IX in the middle of the string
      
      
    ].each do |roman|
      it "determines #{roman} is invalid" do
        RomanToInt.whole_string_valid(roman).should be_false
      end
    end

    
    [
      'XXXIX',
      'MMCCCXC',
      'XXXIV',
      'MIV',
      'DCCC',
      'MDCI',
      'DII',
    ].each do |roman|
      it "determines #{roman} is valid" do
        RomanToInt.whole_string_valid(roman).should be_true
      end
    end

  end

  describe ".int_value" do
    {
      'I' => 1,
      'XL' => 40,
      'VI' => 6,
      'MMDC' => 2600,
      'III' => 3,
      'XIV' => 14,
      'CXIV' => 114,
    }.each do |roman, int|
      it "correctly parses #{roman} to #{int}" do
        RomanToInt.int_value(roman).should == int
      end
    end
    
    [
      'CIXIX',
      'CIXL',
      'MMIXX',
      'VIX',
      'XCXC'
    ].each do |roman|
      it "cannot parse invalid #{roman}" do
        RomanToInt.int_value(roman).should == -1
      end
    end
      

  end



  describe ".parse_file" do

    before :all do
      if File.exists?(TEST_RESULTS_PATH)
        File.delete(TEST_RESULTS_PATH)
      end
      RomanToInt.parse_file(TEST_PATH, TEST_RESULTS_PATH)
    end

    it "results file is expected size" do
      actual_results.size.should == expected_results.size
    end

    it "parses every line as a roman numeral and outputs the integer or an error code" do
      actual_results.should == expected_results
    end
    
  end

end

