require_relative '../lib/roman_to_int'

describe RomanToInt do
  
  describe "#parse" do

    {
      'I' => 1,
      'M' => 1000
    }.each do |roman, int|
      it "correctly parses #{roman} to #{int}" do
        RomanToInt.parse(roman).should == int
      end
    end
  end

  describe "#parse_file" do
    
  end

end

