import time
import MySQLdb
from MySQLdb import OperationalError

DB_HOST = "wattcontrol_db"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "your_mysql_root_password"

def wait_for_db():
    while True:
        try:
            conn = MySQLdb.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                passwd=DB_PASSWORD
            )
            conn.close()
            print("Database is ready!")
            break
        except OperationalError:
            print("Database is not ready, waiting...")
            time.sleep(5)

if __name__ == "__main__":
    wait_for_db()