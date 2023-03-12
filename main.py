import PyPDF2
import os

left_margin = right_margin = 30
top_margin = 5
bottom_margin = 5

input_file_path = []
output_file_path = []
# os.makedirs('.\\修改')  # 新建文件夹

file_path = '.\\'
file_list = os.listdir(file_path)
for i in file_list:
    if os.path.splitext(i)[1] == '.pdf':
        input_file_path.append('.\\' + i)
        output_file_path.append('.\\修改\\' + '修改' + i)


def split_lift(page):
    page.mediaBox.lowerLeft = (left_margin, bottom_margin)
    page.mediaBox.lowerRight = (width + 5, bottom_margin)
    page.mediaBox.upperLeft = (left_margin, height - top_margin)
    page.mediaBox.upperRight = (width + 5, height - top_margin)


def split_right(page):
    page.mediaBox.lowerLeft = (width, bottom_margin)
    page.mediaBox.lowerRight = (width * 2, bottom_margin)
    page.mediaBox.upperLeft = (width, height - top_margin)
    page.mediaBox.upperRight = (width*2, height - top_margin)


def split(page, l, r, height):
    page.mediaBox.lowerLeft = (l, bottom_margin)
    page.mediaBox.lowerRight = (r, bottom_margin)
    page.mediaBox.upperLeft = (l, height - top_margin)
    page.mediaBox.upperRight = (r, height - top_margin)


def split3():
    for m in range(len(input_file_path)):
        input_file = PyPDF2.PdfFileReader(open(input_file_path[m], 'rb'))
        input_file2 = PyPDF2.PdfFileReader(open(input_file_path[m], 'rb'))
        input_file3 = PyPDF2.PdfFileReader(open(input_file_path[m], 'rb'))
        output_file = PyPDF2.PdfFileWriter()

        page_info = input_file.getPage(0)
        width = float(page_info.mediaBox.getWidth()) / 3
        height = float(page_info.mediaBox.getHeight())
        page_count = input_file.getNumPages()

        for page_num in range(page_count):
            if page_num ==0:
                left_page = input_file.getPage(page_num)
                split(left_page, 0, width+20, height)
                output_file.addPage(left_page)

                m_page = input_file2.getPage(page_num)
                split(m_page, width+20, width*2+30, height)
                output_file.addPage(m_page)

                right_page = input_file3.getPage(page_num)
                split(right_page, width*2+20, width*3, height)
                output_file.addPage(right_page)
            else:
                left_page = input_file.getPage(page_num)
                split(left_page, 0, width-10, height)
                output_file.addPage(left_page)

                m_page = input_file2.getPage(page_num)
                split(m_page, width-10, width * 2, height)
                output_file.addPage(m_page)

                right_page = input_file3.getPage(page_num)
                split(right_page, width * 2 - 10, width * 3, height)
                output_file.addPage(right_page)
        print("试卷分割完成！")
        output_file.write(open(output_file_path[m], 'wb'))


def split2():
    for m in range(len(input_file_path)):
        input_file = PyPDF2.PdfFileReader(open(input_file_path[m], 'rb'))
        input_file2 = PyPDF2.PdfFileReader(open(input_file_path[m], 'rb'))
        output_file = PyPDF2.PdfFileWriter()

        page_info = input_file.getPage(0)
        width = float(page_info.mediaBox.getWidth()) / 2
        height = float(page_info.mediaBox.getHeight())
        page_count = input_file.getNumPages()

        for page_num in range(page_count):
            left_page = input_file.getPage(page_num)
            split(left_page, 0, width, height)
            output_file.addPage(left_page)

            m_page = input_file2.getPage(page_num)
            split(m_page, width, width * 2, height)
            output_file.addPage(m_page)
        print("试卷分割完成！")
        output_file.write(open(output_file_path[m], 'wb'))


split2()