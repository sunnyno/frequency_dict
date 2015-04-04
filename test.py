import unittest
import info
import dictionary


class Test(unittest.TestCase):

    def test_config(self):
        self.assertTrue(info.make_cofig())

    def test_dict(self):
        dict = dictionary.create_dict()
        self.assertGreater(len(dict), 0)

    def test_find_words(self):
        words = dictionary.find_words()
        self.assertGreater(len(words), 0)

    def test_urls(self):
        urls = 5
        main_urls = info.get_urls()
        self.assertEqual(urls, len(main_urls))

    def test_time(self):
        self.assertGreater(dictionary.working_time(), 0)


if __name__ == '__main__':
    unittest.main()
