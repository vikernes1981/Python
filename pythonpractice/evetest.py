import sys
import urllib
import xml.dom.minidom
from PyQt4 import QtGui

#Enter your UserID and API Keys here
UserID = 'XXXXXXX'
Key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
class MainWindow(QtGui.QWidget):
    def __init__(self):
        #Create the layout and the table widget.
        QtGui.QMainWindow.__init__(self)
        layout = QtGui.QHBoxLayout(self)
        self.table = QtGui.QTableWidget(self)
        layout.addWidget(self.table)
        self.setLayout(layout)

        #Download the data and fill out the table.
        self.downloadData()
        self.setTableHeaders()
        self.setTableData()

    def downloadData(self):
        #These lines download the data from the website and load it into an XML parser
        downloadedData = urllib.urlopen('http://api.eve-online.com/account/Characters.xml.aspx?userid=%s&apikey=%s' % (UserID, Key))
        self.XMLData = xml.dom.minidom.parse(downloadedData)

    def setTableHeaders(self):
        #Get the column titles from the XML and load them into the table
        headerNode = self.XMLData.getElementsByTagName("rowset")[0]
        self.columnHeaders = headerNode.attributes['columns'].value.split(',')
        self.table.setColumnCount(len(self.columnHeaders))
        self.table.setHorizontalHeaderLabels(self.columnHeaders)

    def setTableData(self):
        #iterate through the data in the XML and load it into the table    
        dataNodes = self.XMLData.getElementsByTagName("row")
        self.table.setRowCount(len(dataNodes))
        for row, dataNode in enumerate(dataNodes):
            for col, columnHeader in enumerate(self.columnHeaders):
                self.table.setItem(row, col, QtGui.QTableWidgetItem(dataNode.attributes[columnHeader].value))

def main():
    app = QtGui.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()