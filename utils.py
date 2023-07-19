import random
from mysql_connector import get_mysql_connection

# Get MySQL connection
conn = get_mysql_connection()

# Execute a SQL query to count the number of rows in the customer table and select a random id among them
def selected_customer_id():
    with conn.cursor() as cur:
        try:
            cur.execute("USE E_COMMERCE;")
            cur.execute("SELECT COUNT(*) FROM customer")
            num_rows = cur.fetchone()[0]
            customer_id = random.randint(1, num_rows)
        except Exception as e:
            print(f"Exception during request: {str(e)}")
    # Return a random id
    return customer_id

# Execute a SQL query to which retrieve status and create a list of them
def selected_random_statut_id():
    with conn.cursor() as cur:
        try:
            cur.execute("USE E_COMMERCE;")
            cur.execute("SELECT COUNT(*) FROM statut")
            num_rows = cur.fetchone()[0]
            statut_id = random.randint(1, num_rows)
        except Exception as e:
            print(f"Exception during request: {str(e)}")
    return statut_id

# Execute a SQL query to which retrieve status and create a list of them
def selected_random_shipper_id():
    with conn.cursor() as cur:
        try:
            cur.execute("USE E_COMMERCE;")
            cur.execute("SELECT COUNT(*) FROM shipper")
            num_rows = cur.fetchone()[0]
            shipper_id = random.randint(1, num_rows)
        except Exception as e:
            print(f"Exception during request: {str(e)}")
    return shipper_id

# Execute a SQL query to which retrieve status and create a list of them
def retrieve_last_orders_id():
    # Get MySQL connection
    conn = get_mysql_connection()
    with conn.cursor() as cur:
        try:
            cur.execute("USE E_COMMERCE;")
            cur.execute("SELECT orders_id FROM orders ORDER BY orders_id DESC LIMIT 1")
            row = cur.fetchone()
            if row is not None:
                last_orders_id = row[0]  
            else:
                last_orders_id = 1
        except Exception as e:
            print(f"Exception during request: {str(e)}")
    return last_orders_id