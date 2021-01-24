#!/home/ou/soft/Anaconda/anaconda3/bin/python
import xlwt
import xlrd

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = bold
    font.color_index = 4
    font.height = height
    font.name = name
    style.font = font
    return style

def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok = True)
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
    column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其他']
    status = [u'预定', u'出票', u'退票', u'业务小计']
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style("Time New Roman", 220, True))
    i  = 1
    while i < 4 * len(column0):
        sheet1.write_merge(i, i+3, 0, 0, column0[(int)(i/4)], set_style("Arial", 220, True))
        sheet1.write_merge(i, i+3, 7, 7)
        i += 4
    sheet1.write_merge(21, 21, 0, 1, u'合计', set_style("Time New Roman", 220, True))
    i=0
    while i < 4 * len(column0):
        for j in range(0, len(status)):
            sheet1.write(i+j+1, 1, status[j])
        i += 4
    f.save('test.xlsx')


def read_excel():
    wb = xlrd.open_workbook(r'test.xlsx')
    print(wb.sheet_names())
    sheet1 = wb.sheet_by_index(0)
    rowNum = sheet1.nrows
    colNum = sheet1.ncols
    print("nrows %d, ncols %d"%(rowNum, colNum))
    for i in range(0, rowNum):
        print(sheet1.row_values(i))

if __name__ == '__main__':
    write_excel()
    read_excel()
