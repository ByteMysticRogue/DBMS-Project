import pyodbc as odbc
from utils import get_cursor, generate_md5

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
    # Create table for publishers
    publisher_table = """
        CREATE TABLE publisher (
            publisher_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(50),
            address VARCHAR(100) NOT NULL
        );
    """

    # Create table for books
    book_table = """
        CREATE TABLE book (
            book_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price FLOAT NOT NULL,
            publisher_id INT FOREIGN KEY REFERENCES publisher(publisher_id) ON UPDATE CASCADE,
            author VARCHAR(100),
            status VARCHAR(50) DEFAULT 'In Stock' CHECK ( status IN ('In Stock', 'Out of Stock', 'Borrowed') ),
            date_of_publish DATE
        );
    """

    # Create table for book categories
    category_table = """
        CREATE TABLE category (
            category_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            book_id INT FOREIGN KEY REFERENCES book(book_id) ON UPDATE CASCADE,
            name VARCHAR(50) NOT NULL
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
            role VARCHAR(20) DEFAULT 'User' CHECK ( role IN ('Admin', 'User'))
        );
    """

    # Create table for subscriptions
    subscription_table = """
        CREATE TABLE subscription (
            subscription_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            member_id INT FOREIGN KEY REFERENCES member(member_id) ON UPDATE CASCADE,
            subscription_date DATE DEFAULT GETDATE(),
            expire_date DATE DEFAULT GETDATE(),
            status VARCHAR(50) DEFAULT 'Valid' CHECK ( status IN ('Valid', 'Suspend'))
        );
    """

    # Create table for transactions
    transaction_table = """
        CREATE TABLE transactions (
            transaction_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            member_id INT FOREIGN KEY REFERENCES member(member_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
            book_id INT FOREIGN KEY REFERENCES book(book_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
            category_id INT FOREIGN KEY REFERENCES category(category_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
            transaction_date DATE
        );
    """

    # Check if tables exist before creating them
    if not (check_table_exists('book') and
            check_table_exists('publisher') and
            check_table_exists('category') and
            check_table_exists('member') and
            check_table_exists('subscription') and
            check_table_exists('transactions')):
        # Run the creating_table function if any of the tables do not exist
        cursor.execute(publisher_table)
        cursor.execute(book_table)
        cursor.execute(category_table)
        cursor.execute(members_table)
        cursor.execute(subscription_table)
        cursor.execute(transaction_table)
        cursor.commit()
        print("Tables created.", flush=True)
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

    if not check_index_exists('publisher_name_idx'):
        cursor.execute("CREATE INDEX publisher_name_idx ON publisher(name)")
        print("Index publisher_name_idx created.")
    else:
        pass

    if not check_index_exists('category_name_idx'):
        cursor.execute("CREATE INDEX category_name_idx ON category(name)")
        print("Index category_name_idx created.")
    else:
        pass


def create_admin():
    # Check if an admin already exists
    check_admin_query = "SELECT COUNT(*) FROM member WHERE role = 'Admin';"
    cursor.execute(check_admin_query)
    admin_count = cursor.fetchone()[0]

    if admin_count == 0:
        # If no admin exists, create a new admin
        creating_admin_query = """
            INSERT INTO member (username, password, first_name, last_name, email, address, phone, role)
            VALUES ('admin', ?, 'Amir', 'Benny', 'amirbenny@gmail.com', 'iran', '+98921111111', 'Admin')
        """
        hashed_password = generate_md5("123456")
        cursor.execute(creating_admin_query, hashed_password)
        cursor.commit()
        print("Admin Created Successfully!")
    else:
        pass