from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal, QSettings

class SettingsBridge(QObject):
    settingChanged = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.settings = QSettings("LobsterX", "Settings")

    @pyqtSlot(result=str)
    def getTheme(self):
        return self.settings.value("theme", "dark")  # default: "dark"

    @pyqtSlot(str)
    def setTheme(self, theme):
        print(f"Setting theme to: {theme}")
        self.settings.setValue("theme", theme)
        self.settingChanged.emit("theme", theme)

    @pyqtSlot(result=str)
    def getHomepage(self):
        return self.settings.value("homepage", "search.app")  # default: "search.app"

    @pyqtSlot(str)
    def setHomepage(self, homepage):
        print(f"Setting homepage to: {homepage}")
        self.settings.setValue("homepage", homepage)
        self.settingChanged.emit("homepage", homepage)
