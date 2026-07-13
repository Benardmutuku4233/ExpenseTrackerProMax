from PySide6.QtWidgets import QWidget, QHBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class ExpenseChart(QWidget):

    def __init__(self, database):

        super().__init__()

        self.database = database

        self.layout = QHBoxLayout(self)

        self.bar_figure = Figure(
            figsize=(5, 4)
        )

        self.bar_canvas = FigureCanvasQTAgg(
            self.bar_figure
        )

        self.pie_figure = Figure(
            figsize=(5, 4)
        )

        self.pie_canvas = FigureCanvasQTAgg(
            self.pie_figure
        )

        self.layout.addWidget(
            self.bar_canvas
        )

        self.layout.addWidget(
            self.pie_canvas
        )

        self.refresh_chart()

    def refresh_chart(self):

        self.draw_bar_chart()

        self.draw_pie_chart()

    def draw_bar_chart(self):

        self.bar_figure.clear()

        ax = self.bar_figure.add_subplot(
            111
        )

        data = self.database.get_category_summary()

        if not data:

            ax.text(
                0.5,
                0.5,
                "No Data",
                ha="center",
                va="center"
            )

            self.bar_canvas.draw()

            return

        categories = [
            item[0]
            for item in data
        ]

        amounts = [
            item[1]
            for item in data
        ]

        ax.bar(
            categories,
            amounts
        )

        ax.set_title(
            "Expenses By Category"
        )

        ax.set_ylabel(
            "Amount (KSh)"
        )

        ax.tick_params(
            axis="x",
            rotation=45
        )

        self.bar_figure.tight_layout()

        self.bar_canvas.draw()

    def draw_pie_chart(self):

        self.pie_figure.clear()

        ax = self.pie_figure.add_subplot(
            111
        )

        data = self.database.get_category_summary()

        if not data:

            ax.text(
                0.5,
                0.5,
                "No Data",
                ha="center",
                va="center"
            )

            self.pie_canvas.draw()

            return

        categories = [
            item[0]
            for item in data
        ]

        amounts = [
            item[1]
            for item in data
        ]

        ax.pie(
            amounts,
            labels=categories,
            autopct="%1.1f%%"
        )

        ax.set_title(
            "Spending Distribution"
        )

        self.pie_canvas.draw()
