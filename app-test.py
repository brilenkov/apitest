#import unittest
import unittest
from app import app
import json

testTable = {
"ABCDABA"   :   793.6,
"CCCCCCC"   :   6.0,
"ABCD"      :   632.8,
"A"         :   30.5,
"AA"        :   30.5*2,
"AAA"       :   90.0,
"AAAA"      :   90.0+30.5,
"B"         :   101.3,
"BB"        :   101.3*2,
"C"         :   1.0,
"CCCCC"     :   1.0*5,
"CCCCCC"    :   5.0,
"CCCCCCC"   :   5.0+1.0,
"D"         :   500.0,
"DD"        :   500.0*2,
"F"         :   17.0,
"FFFFFFFF"  :   17.0*8,
"FFFFFFFFF" :   135.0,
"FFFFFFFFFF":   135.0+17.0,
""          :   0.0,
"!abcdfSE"  :   0.0,
'D'*1000    :   500.0*1000
}

class TestCase1(unittest.TestCase):
    #Test via json post to '/' page
    def test_step_1(self):
        tester = app.test_client(self)
        for k,v in testTable.iteritems():
            self.assertEqual(str(tester.post('/', data=json.dumps(dict(r=k)),     content_type='application/json').data.strip()), str(v))

    #Test via get query on '/api' page
    def test_step_2(self):
        tester = app.test_client(self)
        for k,v in testTable.iteritems():
            self.assertEqual(str(tester.get('/api?q='+k).data.strip()), str(v))

if __name__ == '__main__':
    unittest.main()
