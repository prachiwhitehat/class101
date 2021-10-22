import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A60Ohnq_Y7pUvmR-Vy_S7WKDB7PzZlatL4iMNcj6bHzWtgVgfMb-pdTRp065KIQqVrHNGw-wCgi0ESLXR5rRFMbFqR3pK9ydhcFHRR7G5YQhaGMtUN47wyhZZ8W4Kcor8imdiPiOQy-w'
    transferData = TransferData(access_token)

    file_from = 'text.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()