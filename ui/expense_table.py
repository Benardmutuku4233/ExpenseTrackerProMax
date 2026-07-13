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

        self.verticalHeader().setDefaultSectionSize(
            45
        )

        self.setAlternatingRowColors(True)

        self.setStyleSheet("""
            
            QTableWidget {
                background-color:white;
                color:#0F172A;
                alternate-background-color:#EFF6FF;
            }


            QTableWidget::item:hover {
                background-color:transparent;
            }


            QTableWidget::item:selected {
                background-color:transparent;
                color:#0F172A;
            }


            QHeaderView::section {

                background-color:#0B2A4A;

                color:white;

                padding:8px;

                font-weight:bold;

            }

        """)

    def load_data(self, expenses):

        self.setRowCount(0)

        for row, expense in enumerate(expenses):

            self.insertRow(row)

            expense_id = expense[0]

            for column in range(6):

                item = QTableWidgetItem(
                    str(expense[column])
                )

                self.setItem(
                    row,
                    column,
                    item
                )

            edit_button = QPushButton(
                "Edit"
            )

            edit_button.setFixedHeight(
                32
            )

            edit_button.setStyleSheet("""
                
                QPushButton {

                    background-color:#2563EB;

                    color:white;

                    border-radius:6px;

                    padding:5px 12px;

                    font-weight:bold;

                }


                QPushButton:hover {

                    background-color:#1D4ED8;

                }

            """)

            edit_button.clicked.connect(
                lambda checked=False, e=expense:
                self.edit_expense(e)
            )

            self.setCellWidget(
                row,
                6,
                edit_button
            )

            delete_button = QPushButton(
                "Delete"
            )

            delete_button.setFixedHeight(
                32
            )

            delete_button.setStyleSheet("""
                
                QPushButton {

                    background-color:#DC2626;

                    color:white;

                    border-radius:6px;

                    padding:5px 12px;

                    font-weight:bold;

                }


                QPushButton:hover {

                    background-color:#B91C1C;

                }

            """)

            delete_button.clicked.connect(
                lambda checked=False, i=expense_id:
                self.delete(i)
            )

            self.setCellWidget(
                row,
                7,
                delete_button
            )

    def edit_expense(self, expense):

        if self.edit_callback:

            self.edit_callback(
                expense
            )

    def delete(self, expense_id):

        if self.delete_callback:

            self.delete_callback(
                expense_id
            )
