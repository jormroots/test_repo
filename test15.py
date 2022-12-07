import unittest

class test(unittest.TestCase):

    def test1(self):
        data1 = ['15']
        ''.join(data1) == '15'
        self.assertEqual(''.join(data1), '15')
    def test2(self):
        data2 = ['37']
        ''.join(data2) == '37'
        self.assertEqual(''.join(data2), '37')
    def test3(self):
        data3 = ['7']
        ''.join(data3) == '7'
        self.assertEqual(''.join(data3), '7')
    def test4(self):
        data4 = ['30']
        ''.join(data4) == '30'
        self.assertEqual(''.join(data4), '30')
    def test5(self):
        data5 = ['teises']
        ''.join(data5) == 'teises'
        self.assertEqual(''.join(data5), 'teises')
    def test6(self):
        data6 = ['3']
        ''.join(data6) == '3'
        self.assertEqual(''.join(data6), '3')
    def test7(self):
        data7 = ['12']
        ''.join(data7) == '12'
        self.assertEqual(''.join(data7), '12')
    def test8(self):
        data8 = ['Viljandi']
        ''.join(data8) == 'Viljandi'
        self.assertEqual(''.join(data8), 'Viljandi')
    def test9(self):
        data9 = ['037']
        ''.join(data9) == '037'
        self.assertEqual(''.join(data9), '037')
    def test10(self):
        data10 = ['20']
        ''.join(data10) == '20'
        self.assertEqual(''.join(data10), '20')

if __name__ == '__main__':
    unittest.main()