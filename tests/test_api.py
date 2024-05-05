import unittest
import json
from api.app import create_app

class TodoAPITestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client for the API."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        # Setup a test database or data structure if required
        self.todos = [
            {"id": "1", "title": "Test Todo 1", "description": "Description of test todo 1"},
            {"id": "2", "title": "Test Todo 2", "description": "Description of test todo 2"}
        ]

    def test_get_todos(self):
        """Test retrieving all to-dos."""
        response = self.client.get('/api/todos')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_create_todo(self):
        """Test creating a new to-do."""
        new_todo = {'title': 'New Todo', 'description': 'New todo description'}
        response = self.client.post('/api/todos', json=new_todo)
        self.assertEqual(response.status_code, 201)
        self.assertIn('New Todo', response.data.decode('utf-8'))

    def test_get_todo(self):
        """Test retrieving a single to-do by ID."""
        response = self.client.get('/api/todos/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Todo 1', response.data.decode('utf-8'))

    def test_update_todo(self):
        """Test updating an existing to-do."""
        updates = {'title': 'Updated Todo', 'description': 'Updated description'}
        response = self.client.put('/api/todos/1', json=updates)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Todo', response.data.decode('utf-8'))

    def test_delete_todo(self):
        """Test deleting a to-do."""
        response = self.client.delete('/api/todos/1')
        self.assertEqual(response.status_code, 204)
        # Verify the to-do is removed
        follow_up_response = self.client.get('/api/todos/1')
        self.assertEqual(follow_up_response.status_code, 404)

    def tearDown(self):
        """Tear down any data added during tests."""
        pass

if __name__ == '__main__':
    unittest.main()
