import unittest
from Lesson_21.task1.Open import Open


class TestOpen(unittest.TestCase):
    filepath = 'Lesson_21.task2.test.txt'

    def test_create_logger(self):
        self.assertTrue(Open.logger)

    def test_enter(self):
        with Open(self.filepath, 'w') as f:
            self.assertFalse(f.closed)
            f.write('test')
            self.assertIn('test', 'test.txt')
        with Open(self.filepath) as f:
            data = f.read()
            self.assertEqual(data, 'test')
        with self.assertRaises(FileNotFoundError):
            with Open('not_exist.txt') as f:
                pass

    def test_exit(self):
        with Open(self.filepath, 'w') as f:
            pass
        self.assertTrue(f.closed)

    def test_get_counter(self):
        self.assertEqual(Open.get_counter(), 4)
        with Open(self.filepath, 'w') as f:
            pass
        self.assertEqual(Open.get_counter(), 5)


if __name__ == '__main__':
    unittest.main()
