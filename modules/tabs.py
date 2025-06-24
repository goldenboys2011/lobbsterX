import os
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (
    QLineEdit,
    QTabWidget, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
)
from PyQt6.QtWebEngineCore import QWebEngineScript
from PyQt6.QtWebChannel import QWebChannel
from modules.resourcePath import resource_path
from modules.settingsBridge import SettingsBridge
from PyQt6.QtCore import QUrl
from urllib.parse import quote

def load_internal_html(page_name, utf8 = False):
    try:
        file_path = resource_path(os.path.join("internal/pages", f"{page_name}.html"))
        if utf8:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        else:
            with open(file_path, "r") as f:
                return f.read()
    except FileNotFoundError:
        return None


class BrowserTab(QWidget):
    def __init__(self, buss_url: str = "search.app"):
        super().__init__()
        self.devtools = None
        self.default_url = buss_url
        layout = QVBoxLayout(self)
        nav_bar = QHBoxLayout()

        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Enter URL")
        self.entry.returnPressed.connect(self.navigate)

        back_btn = QPushButton("⟵")
        back_btn.clicked.connect(self.go_back)
        fwd_btn = QPushButton("⟶")
        fwd_btn.clicked.connect(self.go_forward)

        nav_bar.addWidget(back_btn)
        nav_bar.addWidget(fwd_btn)
        nav_bar.addWidget(self.entry)

        self.view = QWebEngineView()
        script = QWebEngineScript()
        script.setName("OverrideAppName")
        script.setInjectionPoint(QWebEngineScript.InjectionPoint.DocumentReady)
        script.setRunsOnSubFrames(True)
        script.setWorldId(QWebEngineScript.ScriptWorldId.MainWorld)
        script.setSourceCode("""
        Object.defineProperty(navigator, 'appName', {
        get: function () { return 'LobbsterX'; }
        });
        """)
        self.view.page().profile().scripts().insert(script)
        self.view.urlChanged.connect(self.update_url_bar)
        self.view.titleChanged.connect(self.update_tab_title)

        layout.addLayout(nav_bar)
        layout.addWidget(self.view)

        self.load_buss_url(self.default_url)

        self.channel = QWebChannel()
        self.settingsBridge = SettingsBridge()
        self.channel.registerObject("settingsBridge", self.settingsBridge)
        self.view.page().setWebChannel(self.channel)
        
    def show_devtools(self):
        if self.devtools is None:
            self.devtools = QWebEngineView()
            self.view.page().setDevToolsPage(self.devtools.page())
            self.devtools.setWindowTitle("DevTools")
            self.devtools.resize(800, 600)
            self.devtools.show()

        self.devtools.show()
    
    def close_devtools(self):
        if self.devtools:
            self.devtools.close()
            self.view.page().setDevToolsPage(None)
            self.devtools = None

    def load_buss_url(self, buss_url):
        encoded = quote(buss_url)
        final_url = f"https://golden.is-a.dev/Webx-viewer-upgrade/embed?url={encoded}&bussinga=true&dns=https://dns.webxplus.org/"
        self.view.load(QUrl(final_url))
        self.entry.setText(f"buss://{buss_url}")

    def go_back(self):
        self.view.back()

    def go_forward(self):
        self.view.forward()

    def navigate(self):
        url = self.entry.text()

        if url.startswith("lobbster://"):
            page = url.removeprefix("lobbster://").lower()
            html = load_internal_html(page)
            if html:
                self.view.setHtml(html, QUrl(url))
            else:
                self.view.setHtml(f"""
                    <html>
                        <head><title>404 Not Found</title></head>
                        <body><h1>Page Not Found</h1><p>No such internal page: {page}</p></body>
                    </html>
                """, QUrl(url))
            return
        if url.startswith("localhost"):
            encoded = quote(url)
            final_url = f"https://golden.is-a.dev/Webx-viewer-upgrade/embed?url={encoded}&bussinga=true&dns=https://dns.webxplus.org/"
            self.view.load(QUrl(final_url))
            self.entry.setText(f"{url}")
            return
        if url.startswith("buss://"):
            raw = url[7:]
        else:
            raw = url
        self.load_buss_url(raw)

    def update_url_bar(self, qurl):
        pass

    def update_tab_title(self, title):
        parent = self.parent()
        if isinstance(parent, QWidget):
            grandparent = parent.parent()
            if isinstance(grandparent, QTabWidget):
                index = grandparent.indexOf(self)
                if index != -1:
                    grandparent.setTabText(index, title[:15])