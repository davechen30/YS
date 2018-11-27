# import StringIO

import xlrd
import xlwt
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def writeExcel(sheetName,columnName,data):
    file = xlwt.Workbook(encoding = 'utf-8')
    sheet = file.add_sheet(sheetName)
    style_heading = xlwt.easyxf("""
        font:
            name Arial,
            colour_index black,
            bold on,
            height 0xA0;
        align:
            wrap off,
            vert center,
            horiz center;
        pattern:
            pattern solid,
            fore-colour white;
        borders:
            left THIN,
            right THIN,
            top THIN,
            bottom THIN;
        """
                                   )
    style_body = xlwt.easyxf("""
            font:
                name Arial,
                bold off,
                height 0XA0;
            align:
                wrap on,
                vert center,
                horiz left;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                             )
    for x,columnName in enumerate(columnName):
        # 写入数据sheet.write(行,列,value)
        sheet.write(0, x, columnName,style_heading)
    for col,colData in enumerate(data):
        for row,rowData in enumerate(colData):
            sheet.write(col+1, row, rowData,style_body)
    # file.save(fileName)
    return file

def readExcel(excelName):
    file = xlrd.open_workbook(excelName)

