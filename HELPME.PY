import cv2
from pyzbar.pyzbar import decode

def decoder(frame):
    decoding_info = decode(frame)
    return decoding_info
cap = cv2.VideoCapture(0)
redirect = '127.0.0.1'
website_list = ['youtube.com', 'www.youtube.com']
host_path = 'C:\Windows\System32\drivers\etc\hosts'
printed = False
printed1 = False
while True:
    ret, frame = cap.read()
    decoding_info = decoder(frame)
    if decoding_info:
        with open(host_path, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
            f.truncate()
        if not printed1:
            print('Unlocked!')
            printed1 = True
        break
    else:
        with open(host_path, 'r+') as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect+' '+website+'\n')
        if not printed:
            print('Blocked!')
            printed = True
    cv2.imshow('Self control', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()        

