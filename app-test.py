import unittest
import os
import tempfile
#import app
from app import app
import json
from decimal import Decimal

class FlaskrTestCase(unittest.TestCase):

    def mandtest1(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='ABCDABA')),     content_type='application/json').data.strip()), str(793.6))
    def mandtest2(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='CCCCCCC')),     content_type='application/json').data.strip()), str(6.0))
    def mandtest3(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='ABCD')),     content_type='application/json').data.strip()), str(632.8))
        
    def test1(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='A')),     content_type='application/json').data.strip()), str(30.5))
    def test2(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='AA')),    content_type='application/json').data.strip()), str(61.0))
    def test3(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='AAA')),   content_type='application/json').data.strip()), str(90.0))
    def test4(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='AAAA')),   content_type='application/json').data.strip()), str(90.0+30.5))
    def test5(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='B')),     content_type='application/json').data.strip()), str(101.3))
    def test6(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='BB')),    content_type='application/json').data.strip()), str(202.6))
    def test7(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='C')),    content_type='application/json').data.strip()), str(1.0))
    def test8(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='CCCCC')),    content_type='application/json').data.strip()), str(1.0*5))
    def test9(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='CCCCCC')),    content_type='application/json').data.strip()), str(5.0))
    def test10(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='CCCCCCC')),    content_type='application/json').data.strip()), str(5.0+1.0))
    def test11(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='D')),    content_type='application/json').data.strip()), str(500.0))
    def test12(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='DD')),    content_type='application/json').data.strip()), str(500.0*2))
    def test13(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='F')),    content_type='application/json').data.strip()), str(17.0))
    def test14(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='FFFFFFFF')),    content_type='application/json').data.strip()), str(17.0*8))
    def test15(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='FFFFFFFFF')),    content_type='application/json').data.strip()), str(135.0))
    def test16(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='FFFFFFFFFF')),    content_type='application/json').data.strip()), str(135.0+17.0))
        
    def test17(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='')),    content_type='application/json').data.strip()), str(0.0))
    def test18(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='!abcdfSE')),    content_type='application/json').data.strip()), str(0.0))
    def test19(self):
        tester = app.test_client(self)
        self.assertEqual(str(tester.post('/', data=json.dumps(dict(r='D'*1000)),    content_type='application/json').data.strip()), str(500.0*1000))

if __name__ == '__main__':
    unittest.main()