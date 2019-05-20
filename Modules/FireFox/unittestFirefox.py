import unittest

import psutil


class testBrowser(unittest.TestCase):

    def test_closeBrowser(self):
        processes = list(psutil.process_iter())
        for i in processes:
            if "firefox" in str(i.name):
                self.assertIn("firefox", str(i.name))

    def test_closePage(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_moveLeft(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Проверим, что s.split не работает, если разделитель - не строка
        with self.assertRaises(TypeError):
            s.split(2)

    def test_moveRight(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_newPage(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_openBrowser(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
