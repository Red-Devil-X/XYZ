import cv2
import dropbox
import random
import time

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="Img" + str(number) + ".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time()
        result=False
    
    return image_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token="sl.AzP7CYjJ36MJeMlT2QYnms_u-wULlfz6dlx0H0NZ4QODFudkj4abay10qwKC3PXh1LqagZ8xNXDaTs42BqmpUlftuulUMHwrZzs2MI4ucVqP6JJPUvf0BfCtfNWYavLUlszKQh0"
    file=img_counter
    file_from=file
    file_to="/NewFolder1/" + (image_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f :
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()