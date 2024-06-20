from PyQt5.QtWidgets import QFrame, QVBoxLayout, QWidget, QTabWidget, QHBoxLayout, QPushButton

class AddTask(QFrame):
    def __init__(self):
        super(AddTask, self).__init__()
        self.def_sections()
        with open('sections/right/view_task/view_task.css', 'r') as file:
            styles = file.read()
        self.setStyleSheet(styles)

    def def_sections(self):
        boton = QPushButton(self)
        boton.setText("ADD")