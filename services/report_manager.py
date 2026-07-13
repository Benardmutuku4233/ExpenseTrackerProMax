from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet


class ReportManager:

    def __init__(self, database):
        self.database = database

    def export_pdf(self, filename):

        expenses = self.database.get_expenses()

        document = SimpleDocTemplate(filename)

        elements = []

        styles = getSampleStyleSheet()

        title = Paragraph(
            "Expense Tracker Report",
            styles["Title"]
        )

        elements.append(title)

        data = [
            [
                "ID",
                "Title",
                "Amount",
                "Category",
                "Date"
            ]
        ]

        for expense in expenses:

            data.append([
                expense[0],
                expense[1],
                expense[2],
                expense[3],
                expense[4]
            ])

        table = Table(data)

        table.setStyle(
            TableStyle([
                ("GRID", (0, 0), (-1, -1), 1, None),
            ])
        )

        elements.append(table)

        document.build(elements)
