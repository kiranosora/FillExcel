import xlrd
import xlwt
import pymysql

title=['ID', 'name', 'score']
names=['ou','orenane', 'wangm']
scores=[100, 90, 99]

def write_excel():
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("sheet", cell_overwrite_ok = True)
    for colId in range(0, len(title)):
        for rowId in range(0, len(names)+1):
            if rowId == 0:
                sheet.write(rowId, colId, title[colId])
            else :
                if colId == 0:
                    sheet.write(rowId, colId, rowId - 1)
                elif colId == 1:
                    sheet.write(rowId, colId, names[rowId - 1])
                elif colId == 2:
                    sheet.write(rowId, colId, scores[rowId - 1])
    wb.save('scores.xlsx')

def read_excel():
    wb = xlrd.open_workbook(r'scores.xlsx')
    sheet = wb.sheet_by_index(0)
    rowValues=[]
    for i in range(0, sheet.nrows):
        rowValues.append(sheet.row_values(i))
    return rowValues


def connectDB:
    #Connect to database
    mydb = pymysql.connect(
            host='localhost',
            user='root',
            password='X-1oastrike',
            )
    mycursor = mydb.cursor()
    return mycursor

def export2MySql(mycursor, values, appendMode=False):
    if not appendMode:
        try:
            mycursor.execute("CREATE DATABASE testDB")
        except :
            print("Error")
        try:
            mycursor.execute("USE testDB")
        except :
            print("Error")
        try:
            mycursor.execute("CREATE TABLE testTable(ID INT NOT NULL AUTO_INCREMENT, name VARCHAR(100) NOT NULL, score INT NOT NULL, PRIMARY KEY (ID) ) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
        except:
            print("Error")
    mycursor.execute("INSERT INTO testTable (name, score) values (%s, %s)", values)
    print(mycursor)
    mycursor.close
    mydb.commit()
    mydb.close()


if __name__ == '__main__':
    write_excel()
    rowVaues=read_excel()
    mycursor = connectDB()
    appendMode = False
    for i in range(1, len(rowVaues)):
        values = rowVaues[i][1:] 
        export2MySql(mycursor, values, appendMode)
