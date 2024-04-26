"""
数据定义的类
"""

class Record:
    province = None,
    gdp: dict = {}

    def __str__(self):
        return f"{self.province},{self.gdp}"

class FileReader:
    def read_data(self)->list[Record]:
        pass

class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path


    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="GB2312")
        date_lines = f.readlines()
        #print(date_lines)
        date_line_year = date_lines[0].split(',')
        #print(date_line_year)
        record_list: list[Record] = []
        for line in date_lines:
            date_line = line.split(',')
            #print(date_line)
            record = Record()
            record.province = date_line[0]
            #print(f"{record.province}")
            i = 1
            while i < len(date_line_year):
                record.gdp[date_line_year[i]] = date_line[i]
                i += 1
            print(record)
            #到上面那一步是正确的，如何将数据封装

            record_list.append(record)
        f.close()

        return record_list

if __name__=='__main__':
    text_file_reader = TextFileReader("分省年度数据.csv")
    list1=text_file_reader.read_data()
