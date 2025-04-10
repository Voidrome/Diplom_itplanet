import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QTableWidgetItem, 
    QStackedWidget
)

import Main_Window
import books
import izdatel

import vidacha
import chitatel



class Expample(QtWidgets.QMainWindow, Main_Window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        



class Zakladka(QtWidgets.QMainWindow,vidacha.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellAccidents)
        self.Add.clicked.connect(self.AddAccidents)
        
        self.Change.clicked.connect(self.ChangeAccidents)

    def test(self):

        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Vidacha_knig'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellAccidents(self):
           
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Vidacha_knig' WHERE ID_vidacha = ?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
    
    def AddAccidents(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Vidacha_knig' (ID_knigi,ID_chitatel,data_vidachi,data_vozrata) VALUES(?,?,?,?)", (self.AddLine.text(), self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text()))
        self.connection.commit()
        self.connection.close()


    def ChangeAccidents(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Vidacha_knig' SET ID_knigi='{self.ChangeLine_1.text()}', ID_chitatel='{self.ChangeLine_2.text()}', data_vidachi='{self.ChangeLine_3.text()}', data_vozrata='{self.ChangeLine_4.text()}'  WHERE ID_vidacha='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()

class Drivers(QtWidgets.QMainWindow,chitatel.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellDrivers)
        self.Add.clicked.connect(self.AddDrivers)

        self.Change.clicked.connect(self.ChangeDrivers)
        
        
    
    def test(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Chitatel'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellDrivers(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Chitatel' WHERE ID_chitatel =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddDrivers(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Chitatel' ('Imya', 'Familia', 'Adres', 'Telefon') VALUES (?, ?, ?, ?)",
                       (self.AddLine.text(), self.AddLine_2.text(), self.AddLine_3.text(), self.AddLine_4.text(),))
                           
        self.connection.commit()
        self.connection.close()


    def ChangeDrivers(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Chitatel' SET Imya='{self.ChangeLine_1.text()}', Familia='{self.ChangeLine_2.text()}', Adres='{self.ChangeLine_3.text()}', Telefon='{self.ChangeLine_4.text()}' WHERE ID_chitatel='{self.ChangeLine.text()}'")
        
        self.connection.commit()
        self.connection.close()

class Knizhka(QtWidgets.QMainWindow,izdatel.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellFuel)
        self.Add.clicked.connect(self.AddFuel)

        self.Change.clicked.connect(self.ChangeFuel)
        

    def test(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Izdatel'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellFuel(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Izdatel' WHERE ID_izdatel =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddFuel(self):

        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Izdatel' (Name_izdatel,Adres_izd,Telefon_izd,Email_izd,Site_izd) VALUES(?,?,?,?,?)", (self.AddLine.text(), self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text(),self.AddLine_5.text(),))
        self.connection.commit()
        self.connection.close()


    def ChangeFuel(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Izdatel' SET Name_izdatel='{self.ChangeLine_1.text()}', Adres_izd='{self.ChangeLine_2.text()}', Telefon_izd='{self.ChangeLine_3.text()}', Email_izd='{self.ChangeLine_4.text()}', Site_izd='{self.ChangeLine_5.text()}' WHERE ID_izdatel='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()


class Inspection(QtWidgets.QMainWindow,books.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test1)
        self.Dell.clicked.connect(self.DellInspection)
        self.Add.clicked.connect(self.AddInspection)
        self.Change.clicked.connect(self.ChangeInspection)


    def test1(self):
        
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Books'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellInspection(self):
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Books' WHERE ID_knigi =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()


    def AddInspection(self):

        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Books' (Name_book,Avtor,Year,Izdatel,Zhanr,Kolvo_stranic) VALUES(?,?,?,?,?,?)", (self.AddLine.text(), self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text(),self.AddLine_5.text(),self.AddLine_6.text()))
        self.connection.commit()
        self.connection.close()

    def ChangeInspection(self):
        
        self.connection = sqlite3.connect('biblio.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Books' SET Name_book='{self.ChangeLine_1.text()}', Avtor='{self.ChangeLine_2.text()}', Year='{self.ChangeLine_3.text()}', Izdatel='{self.ChangeLine_4.text()}', Zhanr='{self.ChangeLine_5.text()}', Kolvo_stranic='{self.ChangeLine_6.text()}' WHERE ID_knigi='{self.ChangeLine.text()}'")
      
        self.connection.commit()
        self.connection.close()






class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)



        self.example = Expample()
        self.Zakladka = Zakladka()
        self.Drivers = Drivers()
        self.Knizhka = Knizhka()
        self.inspection = Inspection()

        
        

        self.stacked_widget.addWidget(self.example)
        self.stacked_widget.addWidget(self.Zakladka)
        self.stacked_widget.addWidget(self.Drivers)
        self.stacked_widget.addWidget(self.Knizhka)
        self.stacked_widget.addWidget(self.inspection)

        
    

        self.example.AccidentsBtn.clicked.connect(self.show_accidents)
        self.Zakladka.Back.clicked.connect(self.show_example)
        self.example.DriversBtn.clicked.connect(self.show_Drivers)
        self.Drivers.Back.clicked.connect(self.show_example)
        self.example.FuelBtn.clicked.connect(self.show_fuel)
        self.Knizhka.Back.clicked.connect(self.show_example)
        self.example.InspectionsBtn.clicked.connect(self.show_inspection)
        self.inspection.Back.clicked.connect(self.show_example)

        
        
        

    def show_example(self):
        self.stacked_widget.setCurrentWidget(self.example)

    def show_accidents(self):
        self.stacked_widget.setCurrentWidget(self.Zakladka)
    
    def show_Drivers(self):
        self.stacked_widget.setCurrentWidget(self.Drivers)
    
    def show_fuel(self):
        self.stacked_widget.setCurrentWidget(self.Knizhka)

    def show_inspection(self):
        self.stacked_widget.setCurrentWidget(self.inspection)
    




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
