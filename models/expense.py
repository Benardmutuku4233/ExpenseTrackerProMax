class Expense:

    def __init__(
        self,
        title,
        amount,
        category,
        date,
        description
    ):

        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __repr__(self):

        return (
            f"Expense("
            f"title={self.title}, "
            f"amount={self.amount}, "
            f"category={self.category}, "
            f"date={self.date})"
        )
