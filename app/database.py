import duckdb

def connect_db():
    conn = duckdb.connect("data/scraped_data.db")
    return conn

def create_tables(conn):
    # Create the necessary tables for storing the scraped data
    pass
