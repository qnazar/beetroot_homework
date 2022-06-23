import unittest
from unittest.mock import patch
import phonebook
import json


class TestPhonebook(unittest.TestCase):

    def setUp(self) -> None:
        with open('contacts.json', 'r') as f:
            self.data = json.load(f)

    new_user = ['Tom', 'Ford', '7878', 'LA']

    @patch('builtins.input', side_effect=new_user)
    def test_add_new(self, mock_inputs):
        result = phonebook.add_new(self.data)
        self.assertEqual(list(result.values()), self.new_user)
        self.assertIn(result, self.data['contacts'])

    @patch('builtins.input', side_effect='Y')
    def test_delete(self, mock_inputs):
        phonebook.delete('1111', self.data)
        self.assertFalse(phonebook.search_by_number('1111', self.data))

    @patch('builtins.input', side_effect=['l', 'Checking', 'e'])
    def test_update(self, mock_inputs):
        phonebook.update('1111', self.data)
        self.assertIn(phonebook.search_by_last_name('Checking', self.data), self.data['contacts'])
        self.assertNotIn(phonebook.search_by_last_name('Testenko', self.data), self.data['contacts'])

    def test_search_by_first_name(self):
        res = phonebook.search_by_first_name('Nazar', self.data)
        self.assertEqual(res['first name'], 'Nazar')

        res = phonebook.search_by_first_name('Klypych', self.data)
        self.assertFalse(res)

    def test_search_by_last_name(self):
        res = phonebook.search_by_last_name('Topolya', self.data)
        self.assertEqual(res['last name'], 'Topolya')

        res = phonebook.search_by_last_name('Taras', self.data)
        self.assertFalse(res)

    def test_search_by_full_name(self):
        with self.assertRaises(ValueError):
            phonebook.search_by_full_name('Nazar', self.data)
        # valid input
        res = phonebook.search_by_full_name('Test Testenko', self.data)
        self.assertEqual(res['first name'], 'Test')
        self.assertEqual(res['last name'], 'Testenko')
        # from different contacts
        res = phonebook.search_by_full_name('Test Klypych', self.data)
        self.assertFalse(res)
        # from different contacts vice versa
        res = phonebook.search_by_full_name('Nazar Testenko', self.data)
        self.assertFalse(res)
        # no first no last name
        res = phonebook.search_by_full_name('Carl Jhonson', self.data)
        self.assertFalse(res)

    def test_search_by_number(self):
        res = phonebook.search_by_number('1111', self.data)
        self.assertEqual(res['phone number'], '1111')

        res = phonebook.search_by_number('132', self.data)
        self.assertEqual(res['first name'], 'Nazar')

        res = phonebook.search_by_number('2568', self.data)
        self.assertFalse(res)

    def test_search_by_city(self):
        res = phonebook.search_by_city('Kyiv', self.data)
        self.assertEqual(res, 2)

        res = phonebook.search_by_city('Lviv', self.data)
        self.assertEqual(res, 1)

        res = phonebook.search_by_city('Sumy', self.data)
        self.assertEqual(res, 0)
