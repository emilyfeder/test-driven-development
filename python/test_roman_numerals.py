"""
Test parsing integers from strings of roman numberals.
"""

import unittest
import os
import pdb
import parse_roman_numerals as prn

DATA_DIR = os.path.join(os.getenv('HOME'), 'Projects/test-driven-development')
TEST_PATH = os.path.join(DATA_DIR, 'test_file.txt')
TEST_RESULTS_PATH = os.path.join(DATA_DIR, 'test_results.txt')
EXPECTED_PATH = os.path.join(DATA_DIR, 'expected_results.txt')

class TestWholeParse(unittest.TestCase):
    
    def test_I(self): 
        self.assertEqual(1, prn.roman_numeral_to_int('I'))

    def test_V(self):
        self.assertEqual(5, prn.roman_numeral_to_int('V'))

    def test_X(self):
        self.assertEqual(10, prn.roman_numeral_to_int('X'))
    
    def test_L(self):
        self.assertEqual(50, prn.roman_numeral_to_int('L'))

    def test_C(self):
        self.assertEqual(100, prn.roman_numeral_to_int('C'))

    def test_D(self):
        self.assertEqual(500, prn.roman_numeral_to_int('D'))

    def test_M(self):
        self.assertEqual(1000, prn.roman_numeral_to_int('M'))

    def test_II(self):
        self.assertEqual(2, prn.roman_numeral_to_int('II'))

    def test_XX(self):
        self.assertEqual(20, prn.roman_numeral_to_int('XX'))

    def test_CC(self):
        self.assertEqual(200, prn.roman_numeral_to_int('CC'))

    def test_MM(self):
        self.assertEqual(2000, prn.roman_numeral_to_int('MM'))

    def test_IV(self):
        self.assertEqual(4, prn.roman_numeral_to_int('IV'))

    def test_IX(self):
        self.assertEqual(9, prn.roman_numeral_to_int('IX'))

    def test_XC(self):
        self.assertEqual(90, prn.roman_numeral_to_int('XC'))

    def test_CD(self):
        self.assertEqual(400, prn.roman_numeral_to_int('CD'))

    def test_CM(self):
        self.assertEqual(900, prn.roman_numeral_to_int('CM'))

    def test_VI(self):
        self.assertEqual(6, prn.roman_numeral_to_int('VI'))

    def test_LI(self):
        self.assertEqual(51, prn.roman_numeral_to_int('LI'))

    def test_LX(self):
        self.assertEqual(60, prn.roman_numeral_to_int('LX'))

    def test_CI(self):
        self.assertEqual(101, prn.roman_numeral_to_int('CI'))

    def test_CX(self):
        self.assertEqual(110, prn.roman_numeral_to_int('CX'))

    def test_CL(self):
        self.assertEqual(150, prn.roman_numeral_to_int('CL'))

    def test_CLX(self):
        self.assertEqual(160, prn.roman_numeral_to_int('CLX'))

    def test_DI(self):
        self.assertEqual(501, prn.roman_numeral_to_int('DI'))

    def test_DX(self):
        self.assertEqual(510, prn.roman_numeral_to_int('DX'))

    def test_DC(self):
        self.assertEqual(600, prn.roman_numeral_to_int('DC'))

    def test_MI(self):
        self.assertEqual(1001, prn.roman_numeral_to_int('MI'))

    def test_MX(self):
        self.assertEqual(1010, prn.roman_numeral_to_int('MX'))

    def test_MC(self):
        self.assertEqual(1100, prn.roman_numeral_to_int('MC'))

    def test_MD(self):
        self.assertEqual(1500, prn.roman_numeral_to_int('MD'))

    def test_viII(self):
        self.assertEqual(8, prn.roman_numeral_to_int('viII'))

    def test_XXIX(self):
        self.assertEqual(29, prn.roman_numeral_to_int('XXIX'))

    def test_DCCCXXIV(self):
        self.assertEqual(824, prn.roman_numeral_to_int('DCCCXXIV'))

    def test_MDCXI(self):
        self.assertEqual(1611, prn.roman_numeral_to_int('MDCXI'))

    def test_MMDXCIX(self):
        self.assertEqual(2599, prn.roman_numeral_to_int('MMDXCIX'))

    def test_XXXIII(self):
        self.assertEqual(33, prn.roman_numeral_to_int('XXXIII'))

    def test_CMVIII(self):
        self.assertEqual(908, prn.roman_numeral_to_int('CMVIII'))

    def test_XXXIX(self):
        self.assertEqual(39, prn.roman_numeral_to_int('XXXIX'))

    def test_XCIX(self):
        self.assertEqual(99, prn.roman_numeral_to_int('XCIX'))

    def test_CCCXLIX(self):
        self.assertEqual(349, prn.roman_numeral_to_int('CCCXLIX'))

    def test_MCMLV(self):
        self.assertEqual(1955, prn.roman_numeral_to_int('MCMLV'))

    def test_mmmd(self):
        self.assertEqual(3500, prn.roman_numeral_to_int('mmmd'))

    def test_MMMCM(self):
        self.assertEqual(3900, prn.roman_numeral_to_int('MMMCM'))

        
        # Invalid roman numerals
    def test_invalid_IM(self):
        self.assertLess(prn.roman_numeral_to_int('IM'), 0)

    def test_invalid_IC(self):
        self.assertLess(prn.roman_numeral_to_int('IC'), 0)

    def test_invalid_IL(self):
        self.assertLess(prn.roman_numeral_to_int('IL'), 0)

    def test_invalid_LM(self):
        self.assertLess(prn.roman_numeral_to_int('LM'), 0)

    def test_invalid_XM(self):
        self.assertLess(prn.roman_numeral_to_int('XM'), 0)

    def test_invalid_IIII(self):
        self.assertLess(prn.roman_numeral_to_int('IIII'), 0)

    def test_invalid_VV(self):
        self.assertLess(prn.roman_numeral_to_int('VV'), 0)

    def test_invalid_DD(self):
        self.assertLess(prn.roman_numeral_to_int('DD'), 0)

    def test_invalid_XICDL(self):
        self.assertLess(prn.roman_numeral_to_int('XICDL'), 0)

    def test_invalid_DLD(self):
        self.assertLess(prn.roman_numeral_to_int('DLD'), 0)

    def test_invalid_LC(self):
        self.assertLess(prn.roman_numeral_to_int('LC'), 0)

    def test_invalid_MLC(self):
        self.assertLess(prn.roman_numeral_to_int('MLC'), 0)

    def test_invalid_MCCCIC(self):
        self.assertLess(prn.roman_numeral_to_int('MCCCIC'), 0)

    def test_invalid_MCXXC(self):
        self.assertLess(prn.roman_numeral_to_int('MCXXC'), 0)

    def test_invalid_CLIIX(self):
        self.assertLess(prn.roman_numeral_to_int('CLIIX'), 0)

    def test_invalid_CIXI(self):
        self.assertLess(prn.roman_numeral_to_int('CIXI'), 0)

    def test_invalid_CIIV(self):
        self.assertLess(prn.roman_numeral_to_int('CIIV'), 0)

class TestWholeStringValid(unittest.TestCase):
    # Write tests for whole_string_valid(roman)

    # The string should contain only valid characters
    def test_invalid_ABCD(self):
        self.assertFalse(prn.whole_string_valid('ABCD'))
    def test_invalid_XXKV(self):
        self.assertFalse(prn.whole_string_valid('XXKV'))
    def test_invalid_dash1ii(self):
        self.assertFalse(prn.whole_string_valid('-1ii'))
    def test_invalid_ZZMM(self):
        self.assertFalse(prn.whole_string_valid('ZZMM'))

    
    # No more than 3 of the same numerals in a row
    def test_invalid_MMMM(self):
        self.assertFalse(prn.whole_string_valid('MMMM'))

    def test_invalid_CCCC(self):
        self.assertFalse(prn.whole_string_valid('CCCC'))

    def test_invalid_XXXIX(self):
        self.assertTrue(prn.whole_string_valid('XXXIX'))

    def test_invalid_CXXXX(self):
        self.assertFalse(prn.whole_string_valid('CXXXX'))

    def test_invalid_MMCCCXC(self):
        self.assertTrue(prn.whole_string_valid('MMCCCXC'))

    def test_invalid_LIIII(self):
        self.assertFalse(prn.whole_string_valid('LIIII'))

    # Tests invalid cases of substractive notation
    def test_invalid_LIC(self):
        self.assertFalse(prn.whole_string_valid('LIC'))

    def test_invalid_MID(self):
        self.assertFalse(prn.whole_string_valid('MID'))

    def test_invalid_XM(self):
        self.assertFalse(prn.whole_string_valid('XM'))

    def test_invalid_MMMIM(self):
        self.assertFalse(prn.whole_string_valid('MMMIM'))

    # Half step numerals cannot be on the left side of subtractive notation
    def test_invalid_VLI(self):
        self.assertFalse(prn.whole_string_valid('VLI'))

    def test_invalid_MLC(self):
        self.assertFalse(prn.whole_string_valid('MLC'))

    def test_invalid_DM(self):
        self.assertFalse(prn.whole_string_valid('DM'))

    # Checks for no double half step numerals
    def test_invalid_VV(self):
        self.assertFalse(prn.whole_string_valid('VV'))

    def test_invalid_CLLV(self):
        self.assertFalse(prn.whole_string_valid('CLLV'))

    def test_invalid_MMDD(self):
        self.assertFalse(prn.whole_string_valid('MMDD'))

    # Test that some valid strings pass
    def test_XXXIV(self):
        self.assertTrue(prn.whole_string_valid('XXXIV'))

    def test_MIV(self):
        self.assertTrue(prn.whole_string_valid('MIV'))

    def test_DCCC(self):
        self.assertTrue(prn.whole_string_valid('DCCC'))

    def test_MDCI(self):
        self.assertTrue(prn.whole_string_valid('MDCI'))

    def test_DII(self):
        self.assertTrue(prn.whole_string_valid('DII'))

# Write tests for int_value(roman)
class TestIntValue(unittest.TestCase):
    # Most of the cases are tested in the general parse test above.
    # This will do only a few checks

    def test_I(self):
        self.assertEqual(1, prn.int_value('I'))
     
    def test_XL(self):
        self.assertEqual(40, prn.int_value('XL'))   
 
    def test_VI(self):
        self.assertEqual(6, prn.int_value('VI'))

    def test_MMDC(self):
        self.assertEqual(2600, prn.int_value('MMDC'))

    def test_III(self):
        self.assertEqual(3, prn.int_value('III'))

    def test_XIV(self):
        self.assertEqual(14, prn.int_value('XIV'))

    def test_CXIV(self):
        self.assertEqual(114, prn.int_value('CXIV'))

    def test_CIXIX(self):
        self.assertEqual(-1, prn.int_value('CIXIX'))

    def test_CIXL(self):
        self.assertEqual(-1, prn.int_value('CIXL'))

    def test_invalid_MMIXX(self):
        self.assertEqual(-1, prn.int_value('MMIXX'))

    def test_invalid_VIX(self):
        self.assertEqual(-1, prn.int_value('VIX'))

    def test_invalid_XCXC(self):
        self.assertEqual(-1, prn.int_value('XCXC'))
        

class TestFileReadingAndWriting(unittest.TestCase):
    
    def runTest(self):
        if os.path.exists(TEST_RESULTS_PATH):
            os.remove(TEST_RESULTS_PATH) 

        prn.parse_roman_numeral_file(TEST_PATH, TEST_RESULTS_PATH)

        results = open(TEST_RESULTS_PATH, 'r')
        expected_results = open(EXPECTED_PATH, 'r')
        self.assertNotEqual(len(results.readlines()), 0)
        for result, expected in zip(results.readlines(), expected_results.readlines()):
            self.assertEqual(result, expected, "Test Result: %s != Expected Result %s" % (result, expected))

        results.close()
        expected_results.close()

if __name__ == '__main__':
    unittest.main(verbosity=1)

