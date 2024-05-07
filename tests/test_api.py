import unittest
from fastapi.testclient import TestClient
from api.main import app

class TodoAPITestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client for the FastAPI application."""
        self.client = TestClient(app)

    def test_get_root(self):
        """Test the root endpoint."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the Todo API powered by FastAPI"})

    def test_list_todos(self):
        """Test the list to-dos endpoint."""
        response = self.client.get("/todos")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_todo(self):
        """Test creating a new to-do."""
        new_todo = {'title': 'New Todo', 'description': 'A new to-do description'}
        response = self.client.post("/todos", json=new_todo)
        self.assertEqual(response.status_code, 201)
        self.assertIn('title', response.json())
        self.assertEqual(response.json()['title'], 'New Todo')

    def test_get_todo(self):
        """Test retrieving a to-do by ID (assuming an existing one)."""
        response = self.client.get("/todos/1")
        if response.status_code == 200:
            self.assertEqual(response.json()['id'], "1")
        else:
            self.assertEqual(response.status_code, 404)

    def test_update_todo(self):
        """Test updating an existing to-do."""
        updates = {'title': 'Updated Todo', 'description': 'Updated description'}
        response = self.client.put("/todos/1", json=updates)
        if response.status_code == 200:
            self.assertEqual(response.json()['title'], 'Updated Todo')
        else:
            self.assertEqual(response.status_code, 404)

    def test_delete_todo(self):
        """Test deleting a to-do."""
        response = self.client.delete("/todos/1")
        if response.status_code == 204:
            # To-do was successfully deleted
            follow_up_response = self.client.get("/todos/1")
            self.assertEqual(follow_up_response.status_code, 404)
        else:
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
