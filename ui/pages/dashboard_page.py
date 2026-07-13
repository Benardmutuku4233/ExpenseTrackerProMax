from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox
)
from PySide6.QtCore import Qt

from ui.expense_table import ExpenseTable


class DashboardPage(QWidget):

    def __init__(self, database):
        super().__init__()

        self.database = database
        self.edit_callback = None

        self.build_ui()

    def create_card(self, title):

        frame = QFrame()

        frame.setStyleSheet("""
            QFrame{
                background:white;
                border:1px solid #d9d9d9;
                border-radius:10px;
                padding:12px;
            }
        """)

        layout = QVBoxLayout(frame)

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)

        value_label = QLabel("0")
        value_label.setAlignment(Qt.AlignCenter)

        value_label.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#1565C0;
        """)

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        return frame, value_label

    def build_ui(self):

        main_layout = QVBoxLayout(self)

        cards_layout = QHBoxLayout()

        card1, self.total_expenses = self.create_card("Total Expenses")
        card2, self.total_amount = self.create_card("Total Amount")
        card3, self.total_categories = self.create_card("Categories")

        cards_layout.addWidget(card1)
        cards_layout.addWidget(card2)
        cards_layout.addWidget(card3)

        main_layout.addLayout(cards_layout)

        self.table = ExpenseTable()

        self.table.edit_callback = self.edit_expense
        self.table.delete_callback = self.delete_expense

        main_layout.addWidget(self.table)

        self.refresh()

    def refresh(self):

        self.total_expenses.setText(
            str(self.database.get_total_expenses())
        )

        self.total_amount.setText(
            f"KSh {self.database.get_total_amount():,.2f}"
        )

        self.total_categories.setText(
            str(self.database.get_total_categories())
        )

        self.table.load_data(
            self.database.get_expenses()
        )

    def edit_expense(self, expense):

        if self.edit_callback:
            self.edit_callback(expense)

    def delete_expense(self, expense_id):

        reply = QMessageBox.question(
            self,
            "Delete Expense",
            "Are you sure you want to delete this expense?"
        )

        if reply == QMessageBox.Yes:

            self.database.delete_expense(expense_id)

            self.refresh()
