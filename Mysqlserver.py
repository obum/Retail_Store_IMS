from mysql.connector import connect, Error

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Stevengerad8!'
}

db_schema = {
    'db_name': 'Retail_store',
    'table_name': ['Products', 'Suppliers', 'Sales']
}

db_checker = f"""
    SELECT SCHEMA_NAME 
    FROM INFORMATION_SCHEMA.SCHEMATA 
    WHERE SCHEMA_NAME = %s;
"""


try:

    connection = connect(**db_config)

    if connection.is_connected():
        print(f'Connection Created Successfully: {connection.get_server_info()}')
        cursor = connection.cursor()
    
except Error as err:
    print(f'Error : {err.msg}')

else:
    # Create the database Retail_store
    try:
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_schema["db_name"]};')

    except Error as err:
        print(f'Database creation Error : {err.msg}')
    else:
        # Use the database Retail_store
        db_name = cursor.execute(db_checker, ('Retail_store',))
        print(db_name)
        # if  == 'Retail_store':
        #     print(f'{db_schema["db_name"]} created Successfully.')
        # cursor.execute(f'USE {db_schema["db_name"]};')
        # print(f'{db_schema["db_name"]} set for use.')
    

    
    # Create the database Retail_store and tables ['Products', 'Suppliers', 'Sales'] if they do not exists
    
