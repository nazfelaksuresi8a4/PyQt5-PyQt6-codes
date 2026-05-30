from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys as _s

def sort_row(parent : QObject,
             table_widget: QTableWidget,
             row: int,
             col: int,
             keyword: str,
             log_list: QListWidget):
    if row > 0:
        row = row - 1
    else:
        row = row

    for Col in range(col):
            try:
                if table_widget.item(row,Col):
                    if table_widget.item(row,Col).text() == keyword:
                        log_list.addItem(QListWidgetItem(f'Bulundu; satır: {row+1} || sütun: {Col+1} || bulunan: {table_widget.item(row,Col).text()}'))
                    
                
            except Exception as sortException:
                print(sortException)
                QMessageBox.critical(parent,'Kritik hata',f'Sorgu sırasında bir hata meydana geldi. Hata: {sortException} || Satır: {row+1} || Sütun: {Col+1}')


def sort_col(parent: QObject,
              table_widget : QTableWidget,
              row : int,
              col : int,
              keyword : str,
              log_list : QListWidget):
    if col > 0:
        col = col - 1
    else:
        col = col

    for Row in range(row):
            try:
                if table_widget.item(Row,col):
                    if table_widget.item(Row,col).text() == keyword:
                        log_list.addItem(QListWidgetItem(f'Bulundu; satır: {Row+1} || sütun: {col+1} || bulunan: {table_widget.item(Row,col).text()}'))
                    
                
            except Exception as sortException:
                print(sortException)
                QMessageBox.critical(parent,'Kritik hata',f'Sorgu sırasında bir hata meydana geldi. Hata: {sortException} || Satır: {Row+1} || Sütun: {col+1}')

def sort_all(parent: QObject,
              table_widget : QTableWidget,
              row : int,
              col : int,
              keyword : str,
              log_list : QListWidget):
    for Row in range(row):
        for Col in range(col):
            try:
                if table_widget.item(Row,Col):
                    if table_widget.item(Row,Col).text() == keyword:
                        log_list.addItem(QListWidgetItem(f'Bulundu; satır: {Row+1} ||sütun: {Col+1} || bulunan: {table_widget.item(Row,Col).text()}'))

            except Exception as sortException:
                            print(sortException)
                            QMessageBox.critical(parent,'Kritik hata',f'Sorgu sırasında bir hata meydana geldi. Hata: {sortException} || Satır: {Row+1} || Sütun: {col+1}')



app = QApplication(_s.argv)
MainWindow = QMainWindow()

#widgets-layouts
MainWidget = QWidget()
MainLayout = QVBoxLayout()

TableWidget = QTableWidget()
TableWidget.setRowCount(10)
TableWidget.setColumnCount(10)

sort_row_button = QPushButton('Satır sorgula')
sort_col_button = QPushButton('Kolon sorgula')
sort_all_button = QPushButton('Tabloyu sorgula')

row_col_input = QSpinBox()
row_col_input.setRange(0,TableWidget.rowCount())


keyword_input = QLineEdit()
keyword_input.setPlaceholderText('Anahtar kelimenizi giriniz..')
keyword_input.setAlignment(Qt.AlignCenter)

results_list = QListWidget()

#layout-widget-append
MainLayout.addWidget(keyword_input)
MainLayout.addWidget(row_col_input)
MainLayout.addWidget(TableWidget)
MainLayout.addWidget(sort_col_button)
MainLayout.addWidget(sort_row_button)
MainLayout.addWidget(sort_all_button)
MainLayout.addWidget(results_list)

#function-binding
sort_row_button.clicked.connect(lambda : sort_row(MainWindow,
                                                  TableWidget,
                                                  row_col_input.value(),
                                                  TableWidget.columnCount(),
                                                  keyword_input.text(),
                                                  results_list))
sort_col_button.clicked.connect(lambda : sort_col(MainWindow,
                                                  TableWidget,
                                                  TableWidget.rowCount(),
                                                  row_col_input.value(),
                                                  keyword_input.text(),
                                                  results_list))

sort_all_button.clicked.connect(lambda : sort_all(MainWindow,
                                                  TableWidget,
                                                  TableWidget.rowCount(),
                                                  TableWidget.columnCount(),
                                                  keyword_input.text(),
                                                  results_list))

#widget-settings
MainWidget.setLayout(MainLayout)

#finally-settings
MainWindow.setCentralWidget(MainWidget)


if __name__ == "__main__":
    MainWindow.show()
    _s.exit(app.exec_())
