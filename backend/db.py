# u: calpal
# p: yFHzmdos-iRrR0zr28PoXA

# curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/1cd7e22b-3c6c-438c-995f-c72b3a5a60de/cert'


# postgresql://calpal:yFHzmdos-iRrR0zr28PoXA@avian-yak-5481.g8z.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full

#!/usr/bin/env python3
"""
Test psycopg with CockroachDB.
"""

import logging
import os
import random
import time
import uuid
from argparse import ArgumentParser, RawTextHelpFormatter

import psycopg2
from psycopg2.errors import SerializationFailure
import psycopg2.extras


# def create_accounts(conn):
#     psycopg2.extras.register_uuid()
#     ids = []
#     id1 = uuid.uuid4()
#     id2 = uuid.uuid4()
#     with conn.cursor() as cur:
#         cur.execute(
#             "CREATE TABLE IF NOT EXISTS accounts (id UUID PRIMARY KEY, balance INT)"
#         )
#         cur.execute(
#             "UPSERT INTO accounts (id, balance) VALUES (%s, 1000), (%s, 250)", (id1, id2))
#         logging.debug("create_accounts(): status message: %s",
#                       cur.statusmessage)
#     conn.commit()
#     ids.append(id1)
#     ids.append(id2)
#     return ids


# def delete_accounts(conn):
#     with conn.cursor() as cur:
#         cur.execute("DELETE FROM accounts")
#         logging.debug("delete_accounts(): status message: %s",
#                       cur.statusmessage)
#     conn.commit()


# def print_balances(conn):
#     with conn.cursor() as cur:
#         cur.execute("SELECT id, balance FROM accounts")
#         logging.debug("print_balances(): status message: %s",
#                       cur.statusmessage)
#         rows = cur.fetchall()
#         conn.commit()
#         print(f"Balances at {time.asctime()}:")
#         for row in rows:
#             print("account id: {0}  balance: ${1:2d}".format(row['id'], row['balance']))


# def transfer_funds(conn, frm, to, amount):
#     with conn.cursor() as cur:

#         # Check the current balance.
#         cur.execute("SELECT balance FROM accounts WHERE id = %s", (frm,))
#         from_balance = cur.fetchone()['balance']
#         if from_balance < amount:
#             raise RuntimeError(
#                 f"insufficient funds in {frm}: have {from_balance}, need {amount}"
#             )

#         # Perform the transfer.
#         cur.execute(
#             "UPDATE accounts SET balance = balance - %s WHERE id = %s", (
#                 amount, frm)
#         )
#         cur.execute(
#             "UPDATE accounts SET balance = balance + %s WHERE id = %s", (
#                 amount, to)
#         )

#     conn.commit()
#     logging.debug("transfer_funds(): status message: %s", cur.statusmessage)


# def run_transaction(conn, op, max_retries=3):
#     """
#     Execute the operation *op(conn)* retrying serialization failure.

#     If the database returns an error asking to retry the transaction, retry it
#     *max_retries* times before giving up (and propagate it).
#     """
#     # leaving this block the transaction will commit or rollback
#     # (if leaving with an exception)
#     with conn:
#         for retry in range(1, max_retries + 1):
#             try:
#                 op(conn)

#                 # If we reach this point, we were able to commit, so we break
#                 # from the retry loop.
#                 return

#             except SerializationFailure as e:
#                 # This is a retry error, so we roll back the current
#                 # transaction and sleep for a bit before retrying. The
#                 # sleep time increases for each failed transaction.
#                 logging.debug("got error: %s", e)
#                 conn.rollback()
#                 logging.debug("EXECUTE SERIALIZATION_FAILURE BRANCH")
#                 sleep_ms = (2**retry) * 0.1 * (random.random() + 0.5)
#                 logging.debug("Sleeping %s seconds", sleep_ms)
#                 time.sleep(sleep_ms)

#             except psycopg2.Error as e:
#                 logging.debug("got error: %s", e)
#                 logging.debug("EXECUTE NON-SERIALIZATION_FAILURE BRANCH")
#                 raise e

#         raise ValueError(
#             f"transaction did not succeed after {max_retries} retries")


def conn():
    DBURL = "postgresql://calpal:yFHzmdos-iRrR0zr28PoXA@avian-yak-5481.g8z.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"

    # logging.basicConfig(level=logging.DEBUG if opt.verbose else logging.INFO)
    try:
        # Attempt to connect to cluster with connection string provided to
        # script. By default, this script uses the value saved to the
        # DATABASE_URL environment variable.
        # For information on supported connection string formats, see
        # https://www.cockroachlabs.com/docs/stable/connect-to-the-database.html.
        conn = psycopg2.connect(DBURL, 
                                application_name="$ docs_simplecrud_psycopg2", 
                                cursor_factory=psycopg2.extras.RealDictCursor)
        return conn
    except Exception as e:
        logging.fatal("database connection failed")
        logging.fatal(e)
        exit(1)


if __name__ == "__main__":

    conn = conn()
    psycopg2.extras.register_uuid()

    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS test (id UUID PRIMARY KEY, value INT)")
        id1 = uuid.uuid4()
        id2 = uuid.uuid4()
        cur.execute("UPSERT INTO test (id, value) VALUES (%s, 1000), (%s, 250)", (id1, id2))
        logging.debug("create_accounts(): status message: %s", cur.statusmessage)
        conn.commit()
    
    with conn.cursor() as cur:
        cur.execute("SELECT id, value FROM test")
        logging.debug("print_values(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        print(f"Balances at {time.asctime()}:")
        for row in rows:
            print("thing id: {0}  thing value: ${1:2d}".format(row['id'], row['value']))

    # ids = create_accounts(conn)
    # print_balances(conn)

    # amount = 100
    # toId = ids.pop()
    # fromId = ids.pop()

    # try:
    #     run_transaction(conn, lambda conn: transfer_funds(
    #         conn, fromId, toId, amount))

    # except ValueError as ve:
    #     # Below, we print the error and continue on so this example is easy to
    #     # run (and run, and run...).  In real code you should handle this error
    #     # and any others thrown by the database interaction.
    #     logging.debug("run_transaction(conn, op) failed: %s", ve)
    #     pass

    # print_balances(conn)

    # delete_accounts(conn)

    # Close communication with the database.
    conn.close()

