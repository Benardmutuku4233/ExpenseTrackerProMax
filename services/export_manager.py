import pandas as pd


class ExportManager:

    def __init__(self, database):
        self.database = database

    def export_excel(self, filename):

        expenses = self.database.get_expenses()

        df = pd.DataFrame(
            expenses,
            columns=[
                "ID",
                "Title",
                "Amount",
                "Category",
                "Date",
                "Description"
            ]
        )

        df.to_excel(
            filename,
            index=False
        )

        return True
