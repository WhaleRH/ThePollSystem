import sys
from PyQt6.QtWidgets import QApplication
from voteCntlr import VoteController

def main() -> None:
    """
    Starting point for the voting application.
    Opens the application, sets up the controller,
    and starts the event loop.
    """
    app = QApplication(sys.argv)
    controller = VoteController()
    controller.view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
