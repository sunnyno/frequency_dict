# -*- coding: utf-8 -*-
import unittest
import info
import dictionary
import codecs
import os


class Test(unittest.TestCase):

    maxDiff = None


    def test_config(self):
        self.assertTrue(info.make_cofig())

    def test_dictionary(self):
        test_file_src = 'test.txt'
        test_file_exp_res = 'test_result_exp.xml'
        test_file_res = 'test_result.xml'
        dictionary.check_dict(test_file_res, test_file_src)

        file = codecs.open(test_file_exp_res, encoding='utf-8', mode='r')
        exp = file.read().encode('utf-8')
        file1 = codecs.open(test_file_res, encoding='utf-8', mode='r')
        real = file1.read().encode('utf-8')
        self.assertEquals(exp,real+'\n')

    def test_get_urls(self):
        doc = 'test_docs.xml'
        urls = ['http://nashakazka.org.ua/pages/bidniy_vovk.html', 'http://www.president.gov.ua/documents/19268.html']
        main_urls = info.get_urls(doc)
        self.assertEqual(urls,main_urls)

    def test_get_url(self):
        path=os.path.dirname(os.path.abspath(__file__))+"/"
        file_test ="file://" + path +"kazka.html"
        f = open('test_info.txt', 'a')
        file = codecs.open('test_kazka.txt', encoding='utf-8', mode='r')
        exp = file.read().encode('utf-8')
        info.get_url(file_test, f)
        f = codecs.open('test_info.txt', encoding='utf-8', mode='r')
        real = f.read().encode('utf-8')
        self.assertEquals(real, exp)


if __name__ == '__main__':
    unittest.main()
