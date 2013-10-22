## To Run This Program
(Actually, to run the tests)

#### Python

    python python/test_roman_numerals.py
    
To run them with color coding, you can install pyrg using pip:

    pip install pyrg

Then edit the config file at ~/.pyrgrc to contain:

    [color]
    ok = green
    fail = yellow
    error = red
    function = cyan

Now you can run the tests with pyrg:

    pyrg -v python/test_roman_numerals.py

