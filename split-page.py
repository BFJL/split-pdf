import PyPDF2


def split(start_page, end_page, file_path):
    file_name = file_path.split('.')[0]
    start_page -= 1

    input_file = PyPDF2.PdfReader(open(file_path, 'rb'))
    output_file = PyPDF2.PdfWriter()

    for page_num in range(start_page, end_page):
        single_page = input_file.pages[page_num]
        output_file.add_page(single_page)
    output_file.write(open(f"{file_name}_{start_page+1}-{end_page}.pdf", 'wb'))


if __name__ == '__main__':
    file = "最短路径问题专练1.pdf"
    split(1, 2, file)
