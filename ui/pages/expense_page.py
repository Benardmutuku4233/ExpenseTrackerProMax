from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QComboBox,
    QMessageBox,
    QDateEdit
)

from PySide6.QtCore import QDate


class ExpensePage(QWidget):

    def __init__(self, database):
        super().__init__()

        self.database = database
        self.editing_id = None
        self.refresh_callback = None

        self.create_ui()

    def create_ui(self):

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Expense Title"))

        self.title_input = QLineEdit()
        layout.addWidget(self.title_input)

        layout.addWidget(QLabel("Amount"))

        self.amount_input = QLineEdit()
        layout.addWidget(self.amount_input)

        layout.addWidget(QLabel("Category"))

        self.category_input = QComboBox()
        self.category_input.addItems([
            "Food",
            "Transport",
            "Bills",
            "Shopping",
            "Entertainment",
            "Healthcare",
            "Education",
            "Other"
        ])
        layout.addWidget(self.category_input)

        layout.addWidget(QLabel("Date"))

        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        layout.addWidget(self.date_input)

        layout.addWidget(QLabel("Description"))

        self.description_input = QTextEdit()
        layout.addWidget(self.description_input)

        self.save_button = QPushButton("Save Expense")

        self.save_button.setStyleSheet("""
    QPushButton {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        padding: 10px 18px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #1D4ED8;
    }
""")
        self.save_button.clicked.connect(self.save_expense)

        layout.addWidget(self.save_button)
        layout.addStretch()

        self.setLayout(layout)

    def save_expense(self):

        title = self.title_input.text().strip()
        amount = self.amount_input.text().strip()

        if not title or not amount:
            QMessageBox.warning(
                self,
                "Missing Information",
                "Please enter Title and Amount."
            )
            return

        try:
            amount = float(amount)
        except ValueError:
            QMessageBox.warning(
                self,
                "Invalid Amount",
                "Amount must be a number."
            )
            return

        category = self.category_input.currentText()
        date = self.date_input.date().toString("yyyy-MM-dd")
        description = self.description_input.toPlainText()

        if self.editing_id is None:

            self.database.add_expense(
                title,
                amount,
                category,
                date,
                description
            )

            QMessageBox.information(
                self,
                "Success",
                "Expense added successfully."
            )

        else:

            self.database.update_expense(
                self.editing_id,
                title,
                amount,
                category,
                date,
                description
            )

            QMessageBox.information(
                self,
                "Success",
                "Expense updated successfully."
            )

            self.editing_id = None
            self.save_button.setText("Save Expense")

        self.clear_form()

        if self.refresh_callback:
            self.refresh_callback()

    def load_expense(self, expense):

        self.editing_id = expense[0]

        self.title_input.setText(expense[1])
        self.amount_input.setText(str(expense[2]))
        self.category_input.setCurrentText(expense[3])

        self.date_input.setDate(
            QDate.fromString(
                expense[4],
                "yyyy-MM-dd"
            )
        )

        self.description_input.setPlainText(expense[5])

        self.save_button.setText("Update Expense")

    def clear_form(self):

        self.title_input.clear()
        self.amount_input.clear()
        self.description_input.clear()

        self.category_input.setCurrentIndex(0)
        self.date_input.setDate(QDate.currentDate())
