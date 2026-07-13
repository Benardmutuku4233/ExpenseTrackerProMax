from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox,
    QScrollArea
)

from ui.expense_table import ExpenseTable
from ui.monthly_chart import MonthlyChart


class DashboardPage(QWidget):

    def __init__(self, database):

        super().__init__()

        self.database = database

        self.edit_callback = None

        self.build_ui()

    def card(self, title, icon, color):

        frame = QFrame()

        frame.setObjectName(
            "summaryCard"
        )

        frame.setFixedHeight(
            120
        )

        frame.setStyleSheet(f"""

            QFrame#summaryCard {{

                background-color:white;

                border-radius:15px;

                border-left:6px solid {color};

                padding:10px;

            }}

        """)

        layout = QVBoxLayout(frame)

        top = QHBoxLayout()

        icon_label = QLabel(icon)

        icon_label.setStyleSheet("""
            font-size:30px;
        """)

        title_label = QLabel(title)

        title_label.setStyleSheet("""
            color:#475569;
            font-size:14px;
            font-weight:bold;
        """)

        top.addWidget(
            icon_label
        )

        top.addWidget(
            title_label
        )

        top.addStretch()

        layout.addLayout(
            top
        )

        value = QLabel("0")

        value.setStyleSheet("""
            color:#0F172A;
            font-size:26px;
            font-weight:bold;
        """)

        layout.addWidget(
            value
        )

        return frame, value

    def build_ui(self):

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        container = QWidget()

        main = QVBoxLayout(
            container
        )

        cards = QHBoxLayout()

        c1, self.total_expenses = self.card(
            "Total Expenses",
            "📊",
            "#2563EB"
        )

        c2, self.total_amount = self.card(
            "Total Amount",
            "💰",
            "#16A34A"
        )

        c3, self.total_categories = self.card(
            "Categories",
            "📁",
            "#9333EA"
        )

        cards.addWidget(
            c1
        )

        cards.addWidget(
            c2
        )

        cards.addWidget(
            c3
        )

        main.addLayout(
            cards
        )

        self.month_chart = MonthlyChart(
            self.database
        )

        self.month_chart.setFixedHeight(
            280
        )

        main.addWidget(
            self.month_chart
        )

        self.table = ExpenseTable()

        self.table.edit_callback = (
            self.edit_expense
        )

        self.table.delete_callback = (
            self.delete_expense
        )

        self.table.setMinimumHeight(
            400
        )

        main.addWidget(
            self.table
        )

        main.addStretch()

        scroll.setWidget(
            container
        )

        layout = QVBoxLayout(
            self
        )

        layout.addWidget(
            scroll
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

        self.month_chart.refresh_chart()

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
