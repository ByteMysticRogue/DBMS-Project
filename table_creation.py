import pyodbc as odbc
from utils import get_cursor

cursor = get_cursor()

def check_table_exists(table_name):
    # Check if the table exists in the information schema
    query = f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{table_name}' AND table_type = 'BASE TABLE';"
    cursor.execute(query)
    return cursor.fetchone()[0] > 0


def check_index_exists(index_name):
    # Check if the index exists in the sys.indexes view
    query = f"SELECT COUNT(*) FROM sys.indexes WHERE name = '{index_name}';"
    cursor.execute(query)
    return cursor.fetchone()[0] > 0


def creating_table():
    # Create table for book categories
    category_table = """
        CREATE TABLE category (
            category_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );
    """

    # Create table for publishers
    publisher_table = """
        CREATE TABLE publisher (
            publisher_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );
    """

    # Create table for admin members
    admin_table = """
        CREATE TABLE admin (
            staff_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(50),
            address VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL CHECK ( LEN(phone) <= 20)
        );
    """

    # Create table for books
    book_table = """
        CREATE TABLE book (
            book_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            category_id INT FOREIGN KEY REFERENCES category(category_id) ON UPDATE CASCADE,
            name VARCHAR(100) NOT NULL,
            price FLOAT NOT NULL,
            publisher_id INT FOREIGN KEY REFERENCES publisher(publisher_id) ON UPDATE CASCADE,
            author VARCHAR(100),
            status VARCHAR(50) DEFAULT 'موجود' CHECK ( status IN ('موجود', 'ناموجود', 'اجاره شده') ),
            date_of_publish DATE
        );
    """

    # Create table for members
    members_table = """
        CREATE TABLE member (
            member_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(50),
            address VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL CHECK ( LEN(phone) <= 20),
            subscription_date DATE DEFAULT GETDATE(),
            expire_date DATE,
            status VARCHAR(50) DEFAULT 'مجاز' CHECK ( status IN ('مسدود', 'مجاز'))
        );
    """

    # Create table for transactions
    transaction_table = """
        CREATE TABLE transactions (
            transaction_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            member_id INT FOREIGN KEY REFERENCES member(member_id) ON UPDATE NO ACTION,
            book_id INT FOREIGN KEY REFERENCES book(book_id) ON UPDATE NO ACTION,
            category_id INT FOREIGN KEY REFERENCES category(category_id) ON UPDATE NO ACTION,
            staff_id INT FOREIGN KEY REFERENCES admin(staff_id) ON UPDATE NO ACTION,
            transaction_date DATE
        );
    """

    # Check if tables exist before creating them
    if not (check_table_exists('category') and
            check_table_exists('publisher') and
            check_table_exists('admin') and
            check_table_exists('book') and
            check_table_exists('member') and
            check_table_exists('transactions')):
        # Run the creating_table function if any of the tables do not exist
        cursor.execute(category_table)
        cursor.execute(publisher_table)
        cursor.execute(admin_table)
        cursor.execute(book_table)
        cursor.execute(members_table)
        cursor.execute(transaction_table)
        cursor.commit()
        print("Tables created.")
    else:
        pass


def creating_indexes():
    # Create indexes only if they don't exist
    if not check_index_exists('name_idx'):
        cursor.execute("CREATE INDEX name_idx ON book(name)")
        print("Index name_idx created.")
    else:
        pass

    if not check_index_exists('author_idx'):
        cursor.execute("CREATE INDEX author_idx ON book(author)")
        print("Index author_idx created.")
    else:
        pass

    if not check_index_exists('username_idx'):
        cursor.execute("CREATE INDEX username_idx ON member(username)")
        print("Index username_idx created.")
    else:
        pass

    if not check_index_exists('first_last_idx'):
        cursor.execute("CREATE INDEX first_last_idx ON member(last_name, first_name)")
        print("Index first_last_idx created.")
    else:
        pass

    if not check_index_exists('username_admin_idx'):
        cursor.execute("CREATE INDEX username_admin_idx ON admin(username)")
        print("Index username_admin_idx created.")
    else:
        pass

    if not check_index_exists('first_last_staff_idx'):
        cursor.execute("CREATE INDEX first_last_staff_idx ON admin(last_name, first_name)")
        print("Index first_last_idx created.")
    else:
        pass


creating_table()
creating_indexes()

cursor.commit()
cursor.close()