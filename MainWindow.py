from PyQt4.QtCore import *
from PyQt4.QtGui import *
from display_widget import *
from sql_connection import *
from PyQt4.QtSql import *
import sys

class Window(QMainWindow):
    """simple window layout"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        #create actions
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database",self)
        self.find_products = QAction("Find Products",self)
        self.show_products = QAction("Show Products",self)
        
        #add menu to a bar
        self.menu = QMenuBar()
        self.database_toolbar = QToolBar()
        self.database_menu = self.menu.addMenu("Database")
        self.products_toolbar = QToolBar()
        self.products_menu = self.menu.addMenu("Products")
        
        #add actions o menu
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)

        self.products_menu.addAction(self.find_products)
        self.products_menu.addAction(self.show_products)
        

        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)

        self.addToolBar(self.database_toolbar)

        self.setMenuBar(self.menu)

        self.open_database.triggered.connect(self.open_connection)

        
        
    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        print(path)
        self.connection = SQLConnection(path)
        ok = self.connection.open_database()
        print(ok)

    def close_connection(self):
        pass

    def display_products(self):
        if not hasattr(self,'display_widget'):
            self.display_widget = DisplayWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_producs_by_number((1,))
        self.display_widget.show_results(query)

    def show_product_table(self):
        pass
            


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    application.exec_()
    
