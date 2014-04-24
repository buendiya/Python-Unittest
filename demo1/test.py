#!/usr/bin/env python
#encoding: utf-8

import unittest
import module

class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def testsum(self):
        self.assertEqual(module.mysum(1, 2), 2, 'test sum fail')
        
        
    def testsub(self):
        self.assertEqual(module.mysub(2, 1), 1, 'test sub fail')   
        
        
if __name__ =='__main__':
    unittest.main()