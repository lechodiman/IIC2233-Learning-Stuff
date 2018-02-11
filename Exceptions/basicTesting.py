import unittest


def some_function(*args, **kwargs):
    return 'TEST'


class MyTest(unittest.TestCase):

    def setUp(self):
        print('Setting up')

    def tearDown(self):
        print('Tearing down')

    # @unittest.expectedFailure
    def test_function(self):
        print('Testing function')
        self.assertEqual(some_function(), 'TEST')


suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
unittest.TextTestRunner().run(suite)
