import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("expense_tracker.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT,
                date TEXT,
                description TEXT
            )
        """)

        self.connection.commit()

    def add_expense(self, title, amount, category, date, description):

        cursor = self.connection.cursor()

        cursor.execute("""
            INSERT INTO expenses
            (title, amount, category, date, description)
            VALUES (?, ?, ?, ?, ?)
        """, (
            title,
            amount,
            category,
            date,
            description
        ))

        self.connection.commit()

    def get_expenses(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT
                id,
                title,
                amount,
                category,
                date,
                description
            FROM expenses
            ORDER BY id DESC
        """)

        return cursor.fetchall()

    def update_expense(
        self,
        expense_id,
        title,
        amount,
        category,
        date,
        description
    ):

        cursor = self.connection.cursor()

        cursor.execute("""
            UPDATE expenses

            SET
                title=?,
                amount=?,
                category=?,
                date=?,
                description=?

            WHERE id=?
        """, (
            title,
            amount,
            category,
            date,
            description,
            expense_id
        ))

        self.connection.commit()

    def delete_expense(self, expense_id):

        cursor = self.connection.cursor()

        cursor.execute("""
            DELETE FROM expenses
            WHERE id=?
        """, (expense_id,))

        self.connection.commit()

    def get_total_expenses(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM expenses
        """)

        return cursor.fetchone()[0]

    def get_total_amount(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT IFNULL(SUM(amount),0)
            FROM expenses
        """)

        return cursor.fetchone()[0]

    def get_total_categories(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT COUNT(DISTINCT category)
            FROM expenses
        """)

        return cursor.fetchone()[0]

    def get_category_summary(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT
                category,
                SUM(amount)
            FROM expenses
            GROUP BY category
            ORDER BY SUM(amount) DESC
        """)

        return cursor.fetchall()
