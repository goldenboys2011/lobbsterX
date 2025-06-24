from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QTabWidget,
    QToolBar,QPushButton
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
import sys
from PyQt6.QtWebChannel import QWebChannel
from mputer import PuterWindow
from settingsBridge import SettingsBridge
import themes
from tabs import BrowserTab

class Browser(QMainWindow):
    def __init__(self, initial_buss_url=None):
        super().__init__()
        self.setWindowTitle("LobbsterX")
        self.resize(1150, 700)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.setCentralWidget(self.tabs)

        self.mputer = False
        new_tab_button = QPushButton()
        new_tab_button.setFixedSize(25, 25)

        icon = QIcon("assets/plus.png") 
        new_tab_button.setIcon(icon)
        new_tab_button.setIconSize(QSize(20, 20)) 
        new_tab_button.clicked.connect(self.new_tab)
        self.tabs.setCornerWidget(new_tab_button, Qt.Corner.TopRightCorner)

        toolbar = QToolBar()

        puter_action = QAction("Mputer ⟡", self)
        puter_action.triggered.connect(self.toggle_puter)
        toolbar.addAction(puter_action)

        devtools_action = QAction("DevTools", self)
        devtools_action.triggered.connect(self.toggle_devtools)
        toolbar.addAction(devtools_action)

        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, toolbar)

        self.new_tab(initial_buss_url)


    def new_tab(self, buss_url=None):
        settings = SettingsBridge()
        tab = BrowserTab(buss_url or settings.getHomepage() or "search.app")
        index = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(index)

    def open_puter(self):
        self.puter_window = PuterWindow()
        self.puter_window.show()
    
    def toggle_devtools(self):
        current_tab = self.tabs.currentWidget()
        if not isinstance(current_tab, BrowserTab):
            return

        if current_tab.devtools is None:
            current_tab.show_devtools()
        else:
            current_tab.close_devtools()

    def toggle_puter(self):
        if self.mputer == False:
            self.open_puter()
        else:
            self.puter_window.close()


    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/lobbesterRB.png"))

    theme = SettingsBridge().getTheme()

    if theme == "dark":
        app.setStyleSheet(themes.themDark)
    else:
        app.setStyleSheet(themes.themeLight)
    
    start_url = None
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.startswith("buss://"):
            start_url = arg[7:]
        else:
            start_url = arg 
    browser = Browser(initial_buss_url=start_url)
    browser.show()
    sys.exit(app.exec())
