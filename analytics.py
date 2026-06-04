import sqlite3

def total_income():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT SUM(amount) FROM transactions
    WHERE type = 'income'
    """)
    income = cursor.fetchone()[0] or 0

    conn.close()
    return income if income else 0

#total expense
def total_expense():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT SUM(amount) FROM transactions
    WHERE type = 'expense'
    """)
    expense = cursor.fetchone()[0] or 0

    conn.close()
    return expense if expense else 0


#Savings
def total_savings():
    income = total_income()
    expense = total_expense()
    return income - expense

#Spending by category
def spending_by_category():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT category, SUM(amount) FROM transactions
    WHERE type = 'expense'
    GROUP BY category
    """)
    data = cursor.fetchall()

    conn.close()
    return data

#Financial Health Score
def financial_health_score():
    income = total_income()
    expense = total_expense()
    
    if income == 0:
        return 0
    
    score = (income - expense) / income * 100
     
    if score >= 40:
        return "Excellent (9/10)"
    elif score >= 20:
        return "Good (7/10)"
    elif score >= 10:
        return "Average (5/10)"
    else:
        return "Poor (3/10)"

def Budget_alert(category, budget):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT SUM(amount) FROM transactions
    WHERE type = 'expense' AND category = ?
    """, (category,))
    
    total_spent = cursor.fetchone()[0] or 0

    conn.close()
    
    if total_spent > budget:
        return f"Alert: You have exceeded your budget for {category} by {total_spent - budget}!"
    else:
        return f"You are within your budget for {category}."



