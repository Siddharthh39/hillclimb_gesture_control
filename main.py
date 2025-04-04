import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class GameModeSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Game Mode Selector")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        
        self.label = QLabel("Choose Game Mode:")
        layout.addWidget(self.label)
        
        self.hillclimb_btn = QPushButton("Hill Climb Racing")
        self.hillclimb_btn.clicked.connect(self.run_hillclimb)
        layout.addWidget(self.hillclimb_btn)
        
        self.hollowknight_btn = QPushButton("Hollow Knight")
        self.hollowknight_btn.clicked.connect(self.run_hollowknight)
        layout.addWidget(self.hollowknight_btn)
        
        self.gba_btn = QPushButton("GBA Emulator")
        self.gba_btn.clicked.connect(self.run_gba)
        layout.addWidget(self.gba_btn)
        
        self.setLayout(layout)

    def run_hillclimb(self):
        import hillclimb_mode
        hillclimb_mode.run()

    def run_hollowknight(self):
        import hollowKnight
        hollowKnight.run()

    def run_gba(self):
        import gba_mode
        gba_mode.run()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameModeSelector()
    window.show()
    sys.exit(app.exec())