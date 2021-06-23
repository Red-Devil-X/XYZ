import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f= open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.Ay6xDuufFoS3UgM_sAFcHN4G_I-w26_A4zEGHkWgbIL8LN5pYeb9hxcfTGYL3uyX3TIsYCb3xdrbDz13zbs1uLMg4bntjbGQXpoXAzJLffkfGZx1kvQFNME8hbjV2jw02eSOt2k'
    transferdata=TransferData(access_token)

    file_from=input("Enter the file path to transfer : ")
    file_to=input("Enter the full path to upload to dropbox : ")

    transferdata.upload_file(file_from,file_to)
    print("File has been moved")

main()