from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHeaderView
)


class ExpenseTable(QTableWidget):

    def __init__(self):
        super().__init__()

        self.edit_callback = None
        self.delete_callback = None

        self.setup_table()

    def setup_table(self):

        self.setColumnCount(8)

        self.setHorizontalHeaderLabels([
            "ID",
            "Title",
            "Amount",
            "Category",
            "Date",
            "Description",
            "Edit",
            "Delete"
        ])

        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.setAlternatingRowColors(True)

    def load_data(self, expenses):

        self.setRowCount(0)

        for row, expense in enumerate(expenses):

            self.insertRow(row)

            for column in range(6):

                self.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(expense[column]))
                )

            edit_button = QPushButton("Edit")

            edit_button.clicked.connect(
                lambda checked=False, e=expense:
                self.edit_expense(e)
            )

            self.setCellWidget(
                row,
                6,
                edit_button
            )

            delete_button = QPushButton("Delete")

            delete_button.clicked.connect(
                lambda checked=False, i=expense[0]:
                self.delete(i)
            )

            self.setCellWidget(
                row,
                7,
                delete_button
            )

    def edit_expense(self, expense):

        if self.edit_callback:
            self.edit_callback(expense)

    def delete(self, expense_id):

        if self.delete_callback:
            self.delete_callback(expense_id)
