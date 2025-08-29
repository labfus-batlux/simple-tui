# simple_tui/app.py
from importlib.resources import files
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal

class SimpleTUI(App):
    CSS_PATH = files(__package__) / "simple_tui.css"
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Horizontal(
            Static("Left Pane", id="left"),
            Static("Middle Pane", id="middle"),
            Static("Right Pane", id="right"),
        )

def main():
    SimpleTUI().run()

