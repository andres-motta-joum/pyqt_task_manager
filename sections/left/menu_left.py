from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem

class LeftFrame(QFrame):
    itemClicked = pyqtSignal(int)  # Señal personalizada para pasar el índice

    def __init__(self, tasks):
        super(LeftFrame, self).__init__()
        self.setFixedWidth(270)
        self.setObjectName('main_frame')
        self.def_sections(tasks)
        with open('sections/left/menu_left.css', 'r') as file:
            styles = file.read()
        self.setStyleSheet(styles)

    def def_sections(self, tasks):
        header_layout = QHBoxLayout()
        titulo = QLabel('Tus tareas')
        titulo.setFixedSize(170, 40)
        agregar = QPushButton('+', objectName="button_add")
        header_layout.addWidget(titulo)
        header_layout.addWidget(agregar)

        list_widget = QListWidget()
        for i in range(len(tasks)):
            item = QListWidgetItem(f"{tasks[i]['tittle']}")
            list_widget.addItem(item)
            item.setData(Qt.UserRole, i)
        list_widget.setCurrentRow(0)

        list_widget.itemClicked.connect(self.handle_item_click)

        main_layout = QVBoxLayout()
        main_layout.addLayout(header_layout)
        main_layout.addWidget(list_widget)

        self.setLayout(main_layout)

    def handle_item_click(self, item):
        index = item.data(Qt.UserRole)
        self.itemClicked.emit(index)  # Emitir la señal con el índice