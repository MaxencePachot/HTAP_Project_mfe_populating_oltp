from fastapi import FastAPI, HTTPException
from models import Orders, Orders_quantity
from mysql_connector import get_mysql_connection

# Initialize app
app = FastAPI()

# Get MySQL connection
conn = get_mysql_connection()

# Define route to add a new Order
@app.put("/orders/")
async def add_orders(orders_json: dict):
    # Parse request body and create Order instance
    orders = Orders.parse_obj(orders_json)
    # Insert new Order data into database
    with conn.cursor() as cur:
        try:
            cur.execute("USE E_COMMERCE;")
            cur.execute("""
                INSERT INTO orders (orders_date, orders_statut_id, orders_customer_id)
                VALUES (%s, %s, %s)
                """, (orders.orders_date, orders.orders_statut_id, orders.orders_customer_id))
            conn.commit()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    # Return success message
    return {"message": "Order added successfully"}

# Define route to add a new Order
@app.put("/orders_quantity/")
async def add_orders_quantity(orders_quantity_json: dict):
    # Parse request body and create Orders_quantity instance
    orders_quantity = Orders_quantity.parse_obj(orders_quantity_json)
    # Insert new Order data into database
    with conn.cursor() as cur:
        try:
            cur.execute("USE E_COMMERCE;")
            cur.execute("""
                INSERT INTO orders_quantity (orders_quantity_quantity, orders_quantity_orders_id, orders_quantity_product_id)
                VALUES (%s, %s, %s)
                """, (orders_quantity.orders_quantity_quantity, orders_quantity.orders_quantity_orders_id, orders_quantity.orders_quantity_product_id))
            conn.commit()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    # Return success message
    return {"message": "Order quantity added successfully"}
