import csv

orders_filename = 'orders.csv'
orders_quantity_filename = 'orders_quantity.csv'
output_filename = 'inserts.sql'

# Function to generate SQL INSERT statement
def generate_insert(table_name, values):
    column_names = ', '.join(values.keys())
    column_values = ', '.join(str(value) for value in values.values())
    return f"INSERT INTO {table_name} ({column_names}) VALUES ({column_values});\n"

# Read data from orders.csv
orders_data = []
with open(orders_filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        orders_data.append(row)

# Read data from orders_quantity.csv
orders_quantity_data = []
with open(orders_quantity_filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        orders_quantity_data.append(row)

# Generate INSERT statements and write to file
with open(output_filename, 'w') as file:
    # Generate INSERT statements for orders table
    for row in orders_data:
        insert_statement = generate_insert('orders', row)
        file.write(insert_statement)

    # Generate INSERT statements for orders_quantity table
    for row in orders_quantity_data:
        insert_statement = generate_insert('orders_quantity', row)
        file.write(insert_statement)

print(f"SQL INSERT statements have been generated and saved to {output_filename}.")
