import unittest
from app import app, add_task, get_tasks, tasks

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app in testing mode
        app.config["TESTING"] = True
        self.client = app.test_client()  # Create a test client
        tasks.clear()  # Clear the tasks list before each test

    def test_add_task_function(self):
        add_task("Buy groceries")
        self.assertIn("Buy groceries", get_tasks())

        add_task("Clean the house")
        self.assertIn("Clean the house", get_tasks())

    def test_get_tasks_function(self):
        add_task("Buy groceries")
        add_task("Clean the house")
        self.assertEqual(get_tasks(), ["Buy groceries", "Clean the house"])

    def test_add_task_route(self):
        # Test adding the first task via POST request
        response = self.client.post("/add-task", data={"task": "Buy groceries"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Ensure the task appears in the HTML response
        self.assertIn(b"Buy groceries", response.data)

        # Test adding another task
        response = self.client.post("/add-task", data={"task": "Clean the house"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Ensure both tasks appear in the HTML response
        self.assertIn(b"Buy groceries", response.data)
        self.assertIn(b"Clean the house", response.data)

if __name__ == "__main__":
    unittest.main()
