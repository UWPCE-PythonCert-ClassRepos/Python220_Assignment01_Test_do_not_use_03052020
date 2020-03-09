from unittest import TestCase
from unittest.mock import Mock, patch
import main
import users
import user_status

class MainTest(TestCase):
    def setUp(self):
        self.user_collection = main.init_user_collection()
        self.status_collection = main.init_status_collection()

    def test_init_user_collection(self):
        test_collection = main.init_user_collection()
        self.assertEqual(test_collection.database, {})

    def test_init_status_collection(self):
        test_collection = main.init_status_collection()
        self.assertEqual(test_collection.database, {})

    def test_load_users(self):
        self.assertEqual(main.load_users('accounts.csv', self.user_collection), True)

    def test_save_users(self):
        main.load_users('accounts.csv', self.user_collection)
        self.assertEqual(main.save_users('accounts_saved.csv', self.user_collection), True)

    def test_load_status_updates(self):
        self.assertEqual(main.load_status_updates('status_updates.csv', self.status_collection), True)

    def test_save_status_updates(self):
        main.load_status_updates('status_updates.csv', self.status_collection)
        self.assertEqual(main.save_status_updates('status_updates_saved.csv', self.status_collection), True)

    def test_add_user(self):
        self.assertEqual(main.add_user('ldconejo', 'ldconejo@conejo.com', 'Luis', 'Conejo', self.user_collection), True)

    def test_add_user_duplicated(self):
        main.add_user('ldconejo', 'ldconejo@conejo.com', 'Luis', 'Conejo', self.user_collection)
        self.assertEqual(main.add_user('ldconejo', 'ldconejo@conejo.com', 'Luis', 'Conejo', self.user_collection), False)

    def test_update_user(self):
        main.add_user('ldconejo', 'ldconejo@conejo.com', 'Luis', 'Conejo', self.user_collection)
        self.assertEqual(main.update_user('ldconejo', 'ldconejo@university.edu', 'Lewis', 'Kaninchen', self.user_collection), True)

    def test_update_user_not_found(self):
        self.assertEqual(main.update_user('ldconejo', 'ldconejo@university.edu', 'Lewis', 'Kaninchen', self.user_collection), False)

    def test_delete_user(self):
        main.add_user('ldconejo', 'ldconejo@conejo.com', 'Luis', 'Conejo', self.user_collection)
        self.assertEqual(main.delete_user('ldconejo', self.user_collection), True)

    def test_delete_user_not_found(self):
        self.assertEqual(main.delete_user('ldconejo', self.user_collection), False)

    def test_search_user(self):
        test_user = users.Users('ldconejo', 'ldconejo@conejo.com', 'Luis', 'Conejo')
        main.add_user('ldconejo', 'ldconejo@conejo.com', 'Luis', 'Conejo', self.user_collection)
        result = main.search_user('ldconejo', self.user_collection)
        self.assertEqual(result.user_id, test_user.user_id)
        self.assertEqual(result.email, test_user.email)
        self.assertEqual(result.user_name, test_user.user_name)
        self.assertEqual(result.user_last_name, test_user.user_last_name)

    def test_search_user_not_found(self):
        result = main.search_user('ldconejo', self.user_collection)
        self.assertEqual(result.user_id, None)

    def test_add_status(self):
        self.assertEqual(main.add_status('ldconejo_001', 'ldconejo', 'Just testing my code', self.status_collection), True)

    def test_add_status_duplicated(self):
        main.add_status('ldconejo_001', 'ldconejo', 'Just testing my code', self.status_collection)
        self.assertEqual(main.add_status('ldconejo_001', 'ldconejo', 'Just testing my code', self.status_collection), False)

    def test_update_status(self):
        main.add_status('ldconejo_001', 'ldconejo', 'Just testing my code', self.status_collection)
        self.assertEqual(main.update_status('ldconejo_001', 'ldconejo', 'Code still works!', self.status_collection), True)

    def test_update_status_not_found(self):
        self.assertEqual(main.update_status('ldconejo_001', 'ldconejo', 'Code still works!', self.status_collection), False)

    def test_delete_status(self):
        main.add_status('ldconejo_001', 'ldconejo', 'Just testing my code', self.status_collection)
        self.assertEqual(main.delete_status('ldconejo_001', self.status_collection), True)

    def test_delete_status_not_found(self):
        self.assertEqual(main.delete_status('ldconejo_001', self.status_collection), False)

    def test_search_status(self):
        main.add_status('ldconejo_001', 'ldconejo', 'Just testing my code', self.status_collection)
        result = main.search_status('ldconejo_001', self.status_collection)
        self.assertEqual(result.status_id, 'ldconejo_001')

    def test_search_status_not_found(self):
        result = main.search_status('ldconejo_001', self.status_collection)
        self.assertEqual(result.status_id, None)