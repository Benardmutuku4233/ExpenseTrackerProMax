from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox
)

from ui.expense_table import ExpenseTable


class DashboardPage(QWidget):

    def __init__(self, database):

        super().__init__()

        self.database = database

        self.edit_callback = None

        self.build_ui()

    def card(self, title):

        frame = QFrame()

        frame.setObjectName(
            "summaryCard"
        )

        layout = QVBoxLayout(frame)

        title_label = QLabel(title)

        title_label.setStyleSheet("""
            color:#475569;
            font-size:14px;
            font-weight:bold;
        """)

        layout.addWidget(
            title_label
        )

        value = QLabel("0")

        value.setStyleSheet("""
            color:#0F172A;
            font-size:22px;
            font-weight:bold;
        """)

        layout.addWidget(
            value
        )

        return frame, value

    def build_ui(self):

        main = QVBoxLayout(self)

        cards = QHBoxLayout()

        c1, self.total_expenses = self.card(
            "Total Expenses"
        )

        c2, self.total_amount = self.card(
            "Total Amount"
        )

        c3, self.total_categories = self.card(
            "Categories"
        )

        cards.addWidget(c1)

        cards.addWidget(c2)

        cards.addWidget(c3)

        main.addLayout(
            cards
        )

        self.table = ExpenseTable()

        self.table.edit_callback = (
            self.edit_expense
        )

        self.table.delete_callback = (
            self.delete_expense
        )

        main.addWidget(
            self.table
        )

        self.refresh()

    def refresh(self):

        self.total_expenses.setText(
            str(
                self.database.get_total_expenses()
            )
        )

        self.total_amount.setText(
            f"KSh {self.database.get_total_amount():,.2f}"
        )

        self.total_categories.setText(
            str(
                self.database.get_total_categories()
            )
        )

        self.table.load_data(
            self.database.get_expenses()
        )

    def edit_expense(self, expense):

        if self.edit_callback:

            self.edit_callback(
                expense
            )

    def delete_expense(self, expense_id):

        answer = QMessageBox.question(
            self,
            "Delete",
            "Delete this expense?"
        )

        if answer == QMessageBox.Yes:

            self.database.delete_expense(
                expense_id
            )

            self.refresh()
