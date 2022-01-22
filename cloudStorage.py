import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, filefrom,fileto):
        dbx = dropbox.Dropbox(self.access_token)

        with open(filefrom, 'rb') as f:
            dbx.files_upload(f.read(), fileto)

def main():
    access_token = 'qrwcc6KWrjgAAAAAAAAAAcKN9Ci-mXLWi8j4CpUdH-BG4ZUkGLslYXeh4J_GZxMC'
    transferData = TransferData(access_token)

    filefrom = input("Please write down your source of the file ")
    fileto = input("Please write down your dropbox location ")

    transferData.upload_file(filefrom,fileto)
    print("File has been moved")



main()
