from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):

    def read(self, filepath=""):
        with open(filepath, 'r') as file:
            content = file.read()
            print(content)

    def write(self, filepath="", data=""):
        with open(filepath, 'w') as file:
            file.write(data)