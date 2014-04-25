#!/usr/bin/env python
#encoding: utf-8
""" http://blog.csdn.net/five3/article/details/7104466 """


import unittest
import module

class test1(unittest.TestCase):
    
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
        
#!/usr/bin/env python
#encoding: utf-8


class test2(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        self.tclass = module.myclass()   ##实例化了被测试模块中的类
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def testsum(self):
        self.assertEqual(self.tclass.sum(1, 2), 2)
        
        

if __name__ =='__main__':
    unittest.main()