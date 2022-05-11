import os


class Download:
    @staticmethod
    def download_from_remote(remote_url):
        pass

    @staticmethod
    def create_directory(directory="Data"):
        current_directory = Download.get_current_directory()
        path = os.path.join(current_directory, directory)
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)

    @staticmethod
    def get_current_directory():
        return os.getcwd()
