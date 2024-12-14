from voteMdl import VoteModel
from voteVw import VoteView

class VoteController:
    """
    Controller class for managing the interactions between the VoteModel and VoteView.

    Attributes:
        model (VoteModel): The model that manages vote data.
        view (VoteView): The view that displays the GUI for voting and results.
    """

    def __init__(self) -> None:
        """
        Initialize the VoteController, set up the model, view, and event connections.
        """
        self.model = VoteModel()
        self.view = VoteView()

        # Connect the buttons to their respective methods
        self.view.john_button.clicked.connect(self.voted_john)
        self.view.jane_button.clicked.connect(self.voted_jane)

        self.view.show()

    def voted_john(self) -> None:
        """
        Handle the event when the "John" button is clicked. Cast vote for John and update the view.
        """
        self.model.vote_john()
        john_votes, jane_votes = self.model.return_votes()
        total_votes = self.model.return_total_votes()
        self.view.vote_label.setText("Vote cast for John")
        self.view.update_results(john_votes, jane_votes, total_votes)

    def voted_jane(self) -> None:
        """
        Handle the event when the "Jane" button is clicked. Cast vote for Jane and update the view.
        """
        self.model.vote_jane()
        john_votes, jane_votes = self.model.return_votes()
        total_votes = self.model.return_total_votes()
        self.view.vote_label.setText("Vote cast for Jane")
        self.view.update_results(john_votes, jane_votes, total_votes)

    def show_results(self) -> None:
        """
        Display the current voting results by updating the view.
        """
        john_votes, jane_votes = self.model.return_votes()
        total_votes = self.model.return_total_votes()
        self.view.update_results(john_votes, jane_votes, total_votes)
