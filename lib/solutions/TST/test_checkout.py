from lib.solutions.CHK.checkout_solution import checkout




class TestSum():
    """

    These are my tests, they were copied from the terminal: they all pass

    """

    def test_all_options(self):
        assert checkout('') == 0
        assert checkout('A') == 50
        assert checkout('B') == 30
        assert checkout('C') == 20
        assert checkout('D') == 15
        assert checkout('a') == -1
        assert checkout('-') == -1
        assert checkout('ABCa') == -1
        assert checkout('AxA') == -1
        assert checkout('ABCD') == 115
        assert checkout('A') == 50
        assert checkout('AA') == 100
        assert checkout('AAA') == 130
        assert checkout('AAAA') == 130+50
        assert checkout('AAAAAA') == 260
        assert checkout('B') == 30
        assert checkout('BB') == 45
        assert checkout('BBB') == 75
        assert checkout('BBBB') == 90
        assert checkout('ABCDABCD') == 2*(50 + 20 + 15) + 45
        assert checkout('BABDDCAC') == 45 + 2*15 + 2*50 + 2*20
        assert checkout('AAABB') == 130+45
        assert checkout('ABCDCBAABCABBAAA') == 505        
