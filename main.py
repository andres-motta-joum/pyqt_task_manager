import sys
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QDesktopWidget, QFrame, QPushButton, QVBoxLayout, QHBoxLayout)
from sections.left.menu_left import LeftFrame
from sections.right.view_task.view_task import ViewTask
from sections.right.add_task.add_task import AddTask

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        with open('main.css', 'r') as file:
            styles = file.read()
        self.setStyleSheet(styles)
    
    def inicializarUI(self):
        self.setWindowTitle("Gestor de Tareas")
        self.setFixedSize(900, 550)
        self.centerWindow()
        self.getData()
        self.crearSecciones()

    def centerWindow(self):
        screen_geometry = QDesktopWidget().screenGeometry() # Obtiene geometría Desktop
        x = (screen_geometry.width() - self.width()) // 2 # Centrar a la pantalla del Desktop
        self.move(x, 90)
    
    def getData(self):
        with open("tasks.json", "r") as json_file:
            json_data = json.load(json_file)
        self.tasks = json_data
    
    def crearSecciones(self):
        left_frame = LeftFrame(self.tasks)
        left_frame.itemClicked.connect(self.showTask)

        self.index_task = 0
        self.right_frame = ViewTask(self.tasks[self.index_task])

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(left_frame)
        self.main_layout.addWidget(self.right_frame)

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)
    
    def showAddTask(self):
        self.main_layout.removeWidget(self.right_frame)
        self.right_frame = AddTask()
        self.main_layout.addWidget(self.right_frame)

    def showTask(self, index):
        self.index_task = index
        self.main_layout.removeWidget(self.right_frame)
        self.right_frame = ViewTask(self.tasks[self.index_task])
        self.main_layout.addWidget(self.right_frame)
    
    def actionsTasks(self, action):
        action = action['action']
        task = action['task']

        if action == 'add':
            self.tasks.append(task) #agregar
            with open("tasks.json", "w") as json_file:
                json.dump(self.tasks, json_file, indent=4)
            
            print(f"agregado: {task}")
    
        elif action == 'update':
            self.tasks[task['id']] = task #actualizar
            with open("tasks.json", "w") as json_file:
                json.dump(self.tasks, json_file, indent=4)
            
            print(f"actualizado: {task}")

        elif action == 'delete':
            self.tasks.pop(task['id']) #eliminar
            with open("tasks.json", "w") as json_file:
                json.dump(self.tasks, json_file, indent=4)
            
            print(f"eliminado: {task}")
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
