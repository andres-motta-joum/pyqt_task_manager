from PyQt5.QtWidgets import QFrame, QVBoxLayout, QWidget, QTabWidget, QHBoxLayout, QPushButton, QLabel, QScrollArea

class ViewTask(QFrame):
    def __init__(self, task):
        super(ViewTask, self).__init__()
        self.def_sections(task)
        with open('sections/right/view_task/view_task.css', 'r') as file:
            styles = file.read()
        self.setStyleSheet(styles)

    def def_sections(self, task):
        content = QFrame(self)
        content.setObjectName('content')
        content.setFixedWidth(596)

        info_layout = QVBoxLayout()
        info_layout.setSpacing(30)
        # Crear y asignar título
        tittle_label = QLabel(task['tittle'])
        tittle_label.setObjectName("tittle_label")
        info_layout.addWidget(tittle_label)

        # Crear y asignar descripción
        description_label = QLabel(f'Descripción:\n{task["description"]}')
        description_label.setObjectName("description_label")
        description_label.setWordWrap(True)
        scroll_area = QScrollArea()
        scroll_area.setWidget(description_label)
        scroll_area.setWidgetResizable(True)
        info_layout.addWidget(scroll_area)

        # Crear y asignar estado
        state_label = QLabel(f'Estado: {task["state"]}')
        state_label.setObjectName("state_label")
        info_layout.addWidget(state_label)

        actions_layout = QHBoxLayout()

        update_button = QPushButton('Actualizar')
        update_button.setObjectName('update_button')
        actions_layout.addWidget(update_button)

        delete_button = QPushButton('Eliminar')
        delete_button.setObjectName('delete_button')
        actions_layout.addWidget(delete_button)
    
        info_layout.addLayout(actions_layout)
        content.setLayout(info_layout)

        
        
