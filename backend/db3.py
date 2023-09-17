# Import necessary libraries
import logging
import os
import random
import time
import uuid
from argparse import ArgumentParser, RawTextHelpFormatter

import psycopg2
from psycopg2.errors import SerializationFailure
import psycopg2.extras

# Global variable for the database URL
DBURL = "postgresql://calpal:yFHzmdos-iRrR0zr28PoXA@avian-yak-5481.g8z.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"

# Define a function to establish a database connection
def conn():
    try:
        # Attempt to connect to the database using the global connection string
        conn = psycopg2.connect(DBURL, 
                                application_name="$ docs_simplecrud_psycopg2", 
                                cursor_factory=psycopg2.extras.RealDictCursor)
        return conn
    except Exception as e:
        logging.fatal("database connection failed")
        logging.fatal(e)
        exit(1)

# Function to add an event to the table
def add_event_to_table(title, start, end):
    conn = psycopg2.connect(DBURL, 
                            application_name="$ docs_simplecrud_psycopg2", 
                            cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        with conn.cursor() as cur:
            cur.execute(
                'INSERT INTO events (title, start, "end") VALUES (%s, %s, %s)',
                (title, start, end)
            )
            conn.commit()
            logging.debug("add_event_to_table(): status message: %s", cur.statusmessage)
    except Exception as e:
        # Handle the exception related to the sequence already existing without printing the error message
        if "relation \"defaultdb.public.events_id_seq\" already exists" not in str(e):
            logging.error("Failed to add event to table: %s", e)
    finally:
        conn.close()


# Function to retrieve all records from the 'events' table
def get_events_from_table():
    conn = psycopg2.connect(DBURL, 
                            application_name="$ docs_simplecrud_psycopg2", 
                            cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM events')
            rows = cur.fetchall()
            return rows
    except Exception as e:
        logging.error("Failed to retrieve events from the table: %s", e)
    finally:
        conn.close()


# Function to delete all records from the 'events' table
def delete_all_records():
    conn = psycopg2.connect(DBURL, 
                            application_name="$ docs_simplecrud_psycopg2", 
                            cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM events')
            conn.commit()
            logging.debug("delete_all_records(): status message: %s", cur.statusmessage)
    except Exception as e:
        logging.error("Failed to delete all records: %s", e)
    finally:
        conn.close()

# Function to delete all records from the 'events' table
def drop_table_events():
    conn = psycopg2.connect(DBURL, 
                            application_name="$ docs_simplecrud_psycopg2", 
                            cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        with conn.cursor() as cur:
            cur.execute('DROP TABLE events')
            conn.commit()
            logging.debug("drop table events(): status message: %s", cur.statusmessage)
    except Exception as e:
        logging.error("Failed to drop all events table: %s", e)
    finally:
        conn.close()

def t_init():
    # Establish a database connection
    connection = conn()
    psycopg2.extras.register_uuid()

    # Create a table named "events" with columns "id," "title," "start," and "end"
    with connection.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id SERIAL PRIMARY KEY NOT NULL,
                title TEXT NOT NULL,
                start STRING NOT NULL,
                "end" STRING NOT NULL
            )
        """)
        logging.debug("create_events_table(): status message: %s", cur.statusmessage)
        connection.commit()

    # Insert a sample event into the "events" table
    # add_event_to_table("Sample Event", "2023-09-22 10:00:00", "2023-09-22 12:00:00")

    # Print the contents of the "events" table
    '''with conn.cursor() as cur:
        cur.execute("SELECT * FROM events")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    '''

    # Delete all records from the "events" table
    #delete_all_records(

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    t_init()
    # delete_all_records()
    # get_events_from_table()
    # drop_table_events()
