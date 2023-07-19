from pydantic import BaseModel

# Create a Pydantic model to represent Orders data
class Orders(BaseModel):
    orders_date: str
    orders_statut_id: int
    orders_customer_id: int

# Create a Pydantic model to represent Orders data
class Orders_quantity(BaseModel):
    orders_quantity_quantity: int
    orders_quantity_orders_id: int
    orders_quantity_product_id: int
