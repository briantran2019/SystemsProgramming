class FileIO:
    @staticmethod
    def read_file(file_path="to_read.txt") -> bytes:
        """
        This method reads data from a file specified by 'file_path' and returns it.
        TODO: Implement this method. Use binary mode "rb"
        """
        file = open(file_path, 'rb')
        lines = file.readlines()


    @staticmethod
    def write_file(data: bytes, file_path="to_write.txt"):
        """
        This method writes 'data' to a file specified by 'file_path'.
        TODO: Implement this method. Use binary mode "rb"
        """
        file = open(file_path, 'rb')
        lines = file.readlines()
        file.write(data.encode())


FileIO.read_file("text.txt")