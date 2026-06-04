import sqlite3


# Create database and table
def create_table():

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        type TEXT,
        date TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()


# Add transaction
def add_transaction(amount, category, type, date, description):

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions
    (amount, category, type, date, description)
    VALUES (?, ?, ?, ?, ?)
    """, (amount, category, type, date, description))

    conn.commit()
    conn.close()


# View all transactions
def view_transactions():

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")

    data = cursor.fetchall()

    conn.close()

    return data


# Delete transaction
def delete_transaction(transaction_id):

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM transactions
    WHERE id = ?
    """, (transaction_id,))

    conn.commit()
    conn.close()


# Update transaction
def update_transaction(transaction_id, amount,
                       category, type,
                       date, description):

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE transactions
    SET amount = ?,
        category = ?,
        type = ?,
        date = ?,
        description = ?
    WHERE id = ?
    """, (
        amount,
        category,
        type,
        date,
        description,
        transaction_id
    ))

    conn.commit()
    conn.close()


# Search by category
def search_by_category(category):

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM transactions
    WHERE category = ?
    """, (category,))

    data = cursor.fetchall()

    conn.close()

    return data