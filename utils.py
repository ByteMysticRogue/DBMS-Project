import hashlib
import pyodbc as odbc
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