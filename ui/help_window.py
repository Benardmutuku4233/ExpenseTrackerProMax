from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)


class HelpWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Expense Tracker Pro Max - User Guide"
        )

        self.resize(
            600,
            500
        )

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel(
            "Expense Tracker Pro Max User Guide"
        )

        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        layout.addWidget(
            title
        )

        guide = QTextEdit()

        guide.setReadOnly(
            True
        )

        guide.setText(
            """
Welcome to Expense Tracker Pro Max.


ADDING EXPENSES
----------------
1. Open Expenses page.
2. Enter title.
3. Enter amount.
4. Select category.
5. Add description.
6. Click Save Expense.


EDITING EXPENSES
----------------
1. Open Dashboard.
2. Click Edit beside an expense.
3. Modify details.
4. Save changes.


DELETING EXPENSES
----------------
1. Click Delete beside an expense.
2. Confirm deletion.


REPORTS
----------------
Use Reports page to view:
- Category analysis
- Monthly spending
- Expense trends


Thank you for using Expense Tracker Pro Max.
"""
        )

        layout.addWidget(
            guide
        )

        close_button = QPushButton(
            "Close"
        )

        close_button.clicked.connect(
            self.close
        )

        layout.addWidget(
            close_button
        )
