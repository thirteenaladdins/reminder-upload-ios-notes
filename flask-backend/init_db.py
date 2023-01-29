from sqlalchemy import create_engine
from dotenv import load_dotenv
# Connect to the default database (usually "postgres")
# engine = create_engine('postgres://username:password@host:port/postgres')

# # Create the new database
# engine.execute("CREATE DATABASE notes")
load_dotenv()

import os
import psycopg2

# Connect to the Postgres server
conn = psycopg2.connect(
        host="localhost",
        # database="notes_db",
        user=os.getenv("DB_USERNAME"),
        password=os.getenv('DB_PASSWORD'))


conn.set_session(autocommit=True)

# Open a cursor
cur = conn.cursor()

# Execute the CREATE DATABASE statement
cur.execute("CREATE DATABASE notes_db")

cur.execute('DROP TABLE IF EXISTS note;')

# cur.execute('CREATE TABLE notes (id serial PRIMARY KEY,'
#                                  'name varchar (150) NOT NULL,'
#                                  'text text NOT NULL,'
#                                  'created_date timestamp DEFAULT CURRENT_TIMESTAMP,'
#                                  'last_modified_date timestamp DEFAULT CURRENT_TIMESTAMP);'
#                                  )



# Close the cursor and connection
cur.close()
conn.close()
