from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView  # Ensure this import is included
from PyQt6.QtWebChannel import QWebChannel
from settingsBridge import SettingsBridge
from tabs import load_internal_html

class PuterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mputer (batman?)")

        layout = QVBoxLayout()
        self.view = QWebEngineView()  # Initialize the web view

        self.channel = QWebChannel()
        self.settingsBridge = SettingsBridge()
        self.channel.registerObject("settingsBridge", self.settingsBridge)
        self.view.page().setWebChannel(self.channel)

        html = load_internal_html("mputer", True)

        if html:
            self.view.setHtml(html, QUrl("lobbster://mputer"))
        else:
            self.view.setHtml("""
                <html>
                    <head><title>404 Not Found</title></head>
                    <body><h1>Page Not Found</h1><p>No such internal page: mputer </p></body>
                </html>
            """, QUrl("lobbster://mputer"))

        layout.addWidget(self.view)  # Add the view to the layout
        self.setLayout(layout)       # Set the layout for the window
