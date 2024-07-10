import sys
import asyncio
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.timer_running = False
        self.task = None

    def init_ui(self):
        self.setWindowTitle("Async Timer Example")
        layout = QVBoxLayout()

        self.label = QLabel("Timer: 0 seconds")
        layout.addWidget(self.label)

        self.start_button = QPushButton("Start Timer")
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.task = asyncio.create_task(self.run_timer())

    async def run_timer(self):
        seconds = 0
        while self.timer_running:
            self.label.setText(f"Timer: {seconds} seconds")
            await asyncio.sleep(1)
            seconds += 1

    def stop_timer(self):
        self.timer_running = False

    def closeEvent(self, event):
        # if self.task:
        #     self.task.cancel()
        loop = asyncio.get_event_loop()
        loop.stop()
        super().closeEvent(event)


async def main():
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()

    try:
        while True:
            await asyncio.sleep(0.01)  # Allow Qt event loop to process events
            app.processEvents()
    except asyncio.CancelledError:
        timer_app.stop_timer()
        app.quit()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        pass
