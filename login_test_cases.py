# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:11:46 2024

@author: praveen006
"""

def logincheck(uname,pwd):
    if(uname=='admin' and pwd=='admin123'):
        return 'success'
    if(uname!='admin' and pwd=='admin123'):
        return 'fail'
    if(uname=='admin' and pwd!='admin123'):
        return 'fail'
    if(uname!='admin' and pwd!='admin123'):
        return 'fail'
     
    
import unittest

class loginclass(unittest.TestCase):
    def test1(self):
        result = logincheck('admin','admin123')
        self.assertEqual(result,'success')
    def test2(self):
        result = logincheck('adminn','admin123')
        self.assertEqual(result,'fail')
    def test3(self):
        result = logincheck('admin','admin1234')
        self.assertEqual(result,'fail')
    def test4(self):
        result = logincheck('admiin','admin1234')
        self.assertEqual(result,'fail')
        

if __name__ == '__main__':
    unittest.main()