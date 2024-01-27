import hashlib
import re
import pyodbc as odbc
import os

def get_cursor():
    data_source = 'SQL-ODBC'
    connection = odbc.connect(f'DSN={data_source};')
    return connection.cursor()

cursor = get_cursor()
def generate_md5(password_str):
    # Create an MD5 hash object
    md5 = hashlib.md5()

    # Update the hash object with the password bytes
    md5.update(password_str.encode('utf-8'))

    # Get the hexadecimal representation of the digest
    hashed_password = md5.hexdigest()

    return hashed_password

def email_validation(email_str):

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if (re.fullmatch(regex, email_str)):
        return True
    else:
        return False

def phone_number_validation(phone_str):

    regex = r'^(0|0098|\+98)9(0[1-5]|[1 3]\d|2[0-2]|98)\d{7}$'

    if (re.fullmatch(regex, phone_str)):
        return True
    else:
        return False


def insert_data_to_tables(file_name):
    try:
        with open(file_name, 'r') as sql_file:
            sql_script = sql_file.read()

            lines = sql_script.split(";")

            table_name = file_name.removesuffix(".sql")
            query = f"SELECT COUNT(*) FROM {table_name};"
            cursor.execute(query)
            table_count = cursor.fetchone()[0]

            if table_count == 0:
                for line in lines:
                    cursor.execute(line)
                cursor.commit()
            else:
                pass
    except Exception as e:
        print(f"Error executing SQL script: {str(e)}")


def process_sql_files():
    for file in os.listdir():
        if file.endswith('.sql'):
            insert_data_to_tables(file)