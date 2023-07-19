from locust import HttpUser, task, between
from faker import Faker
import json
import random
from utils import selected_customer_id, selected_random_statut_id, selected_random_shipper_id, retrieve_last_orders_id

# Create an instance of the Faker class
fake = Faker()

# Define a Locust user to add orders
class MyUser(HttpUser):
    # Wait time between requests
    wait_time = between(1, 3)
    # Define a task to add orders
    @task
    def add_orders_task(self):
        # Retrieve the list of possible status names
        statut_id = selected_random_statut_id()
        # Select a random customer id
        customer_id = selected_customer_id()
        # Select a random shipper id
        shipper_id = selected_random_shipper_id()
        try:
            # Define the orders data attributes
            orders_data = {
                "orders_date": fake.date(),
                "orders_statut_id": statut_id,
                "orders_customer_id": customer_id
            }
            json_orders_data = json.dumps(orders_data)
            print(json_orders_data)
            # Send the request to add the orders quantity data
            self.client.put("/orders/", json=orders_data)
            # retrieve the last orders id
            last_orders_id = retrieve_last_orders_id()
            # Define the orders quantity data attributes, using the orders_id from the response
            orders_quantity_data = {
                "orders_quantity_quantity": random.randint(1, 10),
                "orders_quantity_orders_id": last_orders_id,
                "orders_quantity_product_id": random.randint(1, 30)
            }
            json_orders_quantity_data = json.dumps(orders_quantity_data)
            print(json_orders_quantity_data)
            # Send the request to add the orders quantity data
            self.client.put("/orders_quantity/", json=orders_quantity_data)
        except Exception as e:
            print(f"Exception during request: {str(e)}")

