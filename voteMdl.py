class VoteModel:
    """
    Model class for managing vote data in a poll system.

    Attributes:
        john_vote (int): The number of votes for John.
        jane_vote (int): The number of votes for Jane.
    """

    def __init__(self) -> None:
        """
        Starts the VoteModel with zero votes for both candidates.
        """
        self.john_vote = 0
        self.jane_vote = 0

    def vote_john(self) -> None:
        """
        Increase the vote count for John by 1.
        """
        self.john_vote += 1

    def vote_jane(self) -> None:
        """
        Increase the vote count for Jane by 1.
        """
        self.jane_vote += 1

    def return_votes(self) -> tuple[int, int]:
        """
        Return the current vote counts for both candidates.

        Returns:
            tuple[int, int]: A tuple containing the vote counts for John and Jane.
        """
        return self.john_vote, self.jane_vote

    def return_total_votes(self) -> int:
        """
        Return the total number of votes cast for both candidates.

        Returns:
            int: The total vote count.
        """
        return self.john_vote + self.jane_vote
