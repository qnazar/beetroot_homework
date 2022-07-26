"""write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;
write a query to get the unique department ID from the employee table
write a query to get all employee details from the employee table ordered by first name, descending
write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
write a query to get the maximum and minimum salary from the employees table
write a query to get a monthly salary (round 2 decimal places) of each and every employee"""
import sqlite3
import contextlib


@contextlib.contextmanager
def get_connection(db):
    conn = sqlite3.connect(db)
    try:
        yield conn
    finally:
        conn.close()
        if cursor:
            cursor.close


with get_connection('example_db.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT first_name as [First Name], last_name as [Last Name] FROM employees")
    data = cursor.fetchone()
    print(data)
    print()

    unique_dep_id_query = "SELECT DISTINCT department_id FROM employees"
    cursor.execute(unique_dep_id_query)
    data = cursor.fetchall()
    print(data)
    print()

    get_all_details_query = "SELECT * FROM employees ORDER BY first_name DESC"
    cursor.execute(get_all_details_query)
    data = cursor.fetchmany(size=5)
    for d in data:
        print(d)
    print()

    pf_query = "SELECT first_name, last_name, salary, (salary*0.12) as PF FROM employees"
    cursor.execute(pf_query)
    data = cursor.fetchmany(size=5)
    for d in data:
        print(d)
    print()

    min_max_query = "SELECT MIN(salary), MAX(salary) FROM employees"
    cursor.execute(min_max_query)
    data = cursor.fetchall()
    print(data)
    print()

    round_query = "SELECT first_name, last_name, ROUND(salary-salary*0.12, 2) as monthly_salary FROM employees"
    cursor.execute(round_query)
    data = cursor.fetchmany(size=5)
    for d in data:
        print(d)
