themDark = """
        /* Base */
        QMainWindow, QWidget {
            background-color: #202124;
            color: #E8EAED;
            font-family: 'Segoe UI', sans-serif;
            font-size: 14px;
        }

        /* Buttons */
        QPushButton {
            background-color: #FF6347;
            color: #ffffff;
            padding: 6px 12px;
            border: none;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #fc573a;
        }

        /* Inputs */
        QLineEdit {
            background-color: #303134;
            color: #ffffff;
            border: 1px solid #5f6368;
            border-radius: 6px;
            padding: 4px 8px;
        }

        /* Toolbar */
        QToolBar {
            background-color: #292A2D;
            border-bottom: 1px solid #5f6368;
        }

        QAction {
            background-color: #FF6347;
            color: #ffffff;
        }

        QAction:hover {
            background-color: #fc573a;
            color: #ffffff;
        }

        /* Tabs */
        QTabWidget::pane {
            border: none;
            background-color: #202124;
        }
        QTabBar::tab {
            background-color: #303134;
            color: #E8EAED;
            padding: 8px 12px;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
        }
        QTabBar::tab:selected {
            background-color: #FF6347;
            color: #ffffff;
        }

        /* Scrollbars */
        QScrollBar:vertical {
            background: #202124;
            width: 12px;
            margin: 0px;
        }
        QScrollBar::handle:vertical {
            background: #5f6368;
            border-radius: 6px;
        }
    """

themeLight = """
        /* Base */
        QMainWindow, QWidget {
            background-color: #ffffff;
            color: #202124;
            font-family: 'Segoe UI', sans-serif;
            font-size: 14px;
        }

        /* Buttons */
        QPushButton {
            background-color: #FF6347;
            color: white;
            padding: 6px 12px;
            border: none;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF4500;
        }

        /* Inputs */
        QLineEdit {
            background-color: #f1f3f4;
            color: #202124;
            border: 1px solid #dadce0;
            border-radius: 6px;
            padding: 4px 8px;
        }

        /* Toolbar */
        QToolBar {
            background-color: #f1f3f4;
            border-bottom: 1px solid #dadce0;
        }

        /* Tabs */
        QTabWidget::pane {
            border: none;
            background-color: #ffffff;
        }
        QTabBar::tab {
            background-color: #e8eaed;
            color: #202124;
            padding: 8px 12px;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
        }
        QTabBar::tab:selected {
            background-color: #FF6347;;
            color: white;
        }

        /* Scrollbars */
        QScrollBar:vertical {
            background: #f1f3f4;
            width: 12px;
            margin: 0px;
        }
        QScrollBar::handle:vertical {
            background: #c0c0c0;
            border-radius: 6px;
        }
    """
