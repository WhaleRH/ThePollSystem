from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class VoteView(QWidget):
    """
    A GUI for a simple poll system that allows users to vote for candidates and show results.

    Attributes:
        layout (QVBoxLayout): The main layout of the widget.
        vote_label (QLabel): Label prompting users to select a candidate.
        john_button (QPushButton): Button to cast a vote for John.
        jane_button (QPushButton): Button to cast a vote for Jane.
        result_label (QLabel): Label to display vote counts.
        figure (Figure): Matplotlib figure for chart display.
        canvas (FigureCanvas): Canvas for rendering the Matplotlib figure.
    """

    def __init__(self) -> None:
        """
        Start the VoteView widget, setting up the UI components.
        """
        super().__init__()
        self.setWindowTitle("Poll System")
        self.setGeometry(200, 200, 400, 400)

        self.layout = QVBoxLayout()

        self.vote_label = QLabel("Select which candidate to vote for", self)
        self.layout.addWidget(self.vote_label)

        self.john_button = QPushButton("John", self)
        self.layout.addWidget(self.john_button)

        self.jane_button = QPushButton("Jane", self)
        self.layout.addWidget(self.jane_button)

        self.result_label = QLabel("", self)
        self.layout.addWidget(self.result_label)

        # Set up Matplotlib figure and canvas for display
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def update_results(self, john_votes: int, jane_votes: int, total_votes: int) -> None:
        """
        Update the results display and charts with the current vote counts.

        Args:
            john_votes (int): Number of votes for John.
            jane_votes (int): Number of votes for Jane.
            total_votes (int): Total number of votes cast.
        """
        self.result_label.setText(f"John: {john_votes} | Jane: {jane_votes} | Total Votes: {total_votes}")

        self.figure.clear()

        self.figure.subplots_adjust(wspace=0.8)

        self.update_pie_chart(john_votes, jane_votes)
        self.update_bar_chart(john_votes, jane_votes)

        self.canvas.draw()

    def update_pie_chart(self, john_votes: int, jane_votes: int) -> None:
        """
        Update the pie chart to display the proportion of votes for each candidate.

        Args:
            john_votes (int): Number of votes for John.
            jane_votes (int): Number of votes for Jane.
        """
        ax = self.figure.add_subplot(121)
        ax.clear()
        labels = ["John", "Jane"]
        sizes = [john_votes, jane_votes]
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=["#ff0000", "#0000ff"])
        ax.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.

    def update_bar_chart(self, john_votes: int, jane_votes: int) -> None:
        """
        Update the bar chart to display the vote counts for each candidate.

        Args:
            john_votes (int): Number of votes for John.
            jane_votes (int): Number of votes for Jane.
        """
        ax = self.figure.add_subplot(122)
        ax.clear()
        labels = ["John", "Jane"]
        votes = [john_votes, jane_votes]
        ax.bar(labels, votes, color=["#ff0000", "#0000ff"])
        ax.set_title("Votes Cast")
