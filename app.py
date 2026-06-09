from textual.app import App, ComposeResult
from textual.widgets import Digits
from textual.containers import Container

class MyApp(App):
    CSS_PATH = "styles.css"

    def __init__(self):
        super().__init__()
        self.remaining = 60
        self.blink_state = True

    def compose(self) -> ComposeResult:
        with Container(id="ct"):
            yield Digits(str(self.remaining), id="countdown")

    def on_mount(self) -> None:
        self.timer = self.set_interval(0.01, self.tick)

    def tick(self) -> None:
        display = self.query_one("#countdown", Digits)

        if self.remaining >= 0:
            self.remaining -= 0.01
            display.update(self.format_time(self.remaining))
        else:  
            display.visible = False
            self.timer.stop()
            
            self.timer2 = self.set_interval(0.08, self.blink)

    def blink(self) -> None:
        self.blink_state = not self.blink_state
        if self.blink_state:
            self.screen.styles.background = "white"
        else:
            self.screen.styles.background = "red"

    def format_time(self, seconds: float) -> str:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes:02d}:{secs:05.2f}"


if __name__ == "__main__":
    MyApp().run()