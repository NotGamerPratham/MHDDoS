from locust import HttpUser, task, between

class TestWebsite(HttpUser):
    wait_time = between(1, 2)  # simulate real user delay

    @task
    def load_home(self):
        self.client.get("/")