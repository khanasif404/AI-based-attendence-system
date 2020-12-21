import face_recognition as fc
import cv2
import numpy as np
import pandas as pd
import time
import smtplib
v=cv2.VideoCapture(0)
i=fc.load_image_file(r'C:\Users\Asif khan\Pictures\Camera Roll\WIN_20190629_17_46_07_Pro.jpg')
j=fc.load_image_file(r'C:\Users\Asif khan\Pictures\Camera Roll\WIN_20190629_23_40_27_Pro.jpg')
f1=fc.face_locations(i)
f2=fc.face_locations(j)
e1=fc.face_encodings(i,f1)[0]
e2=fc.face_encodings(j,f2)[0]
print(f1,f2)
print(e1,e2)
e=[e1,e2]
ask=input("enter any key to start the camera ")
d=pd.DataFrame(e)
d.to_csv('image_encodings.csv',index=False)
rcf=pd.read_csv('image_encodings.csv')
name=['abhimanyu','asif']
todaydate=time.strftime("%d/%m/%y")
todaytime=time.strftime("%H/%M/%S")
Student_name=['abhimanyu','asif']
absent=['A','A']
e_mail=['abhimanyushekhawat487@gmail.com','asifk4468@gmail.com']
newcsv={'name':Student_name,'time':todaytime,'date':todaydate,'mail_ids':e_mail,'Atendence':absent}
newd=pd.DataFrame(newcsv)
newd.to_csv('Nattendence.csv',index=False)
print(newd)
while True:
    while True:
        r,live=v.read()
        FL=fc.face_locations(live)               
        if(len(FL)>0):
            [x1,y1,x2,y2]=FL[0]
            cv2.rectangle(live,(y2,x1),(y1,x2),(150,0,255),5) 
            E=fc.face_encodings(live,FL)[0]
        
            res=fc.compare_faces(rcf,E)
            print(res)
            r=True in res
            if(r==True):
                print(name[res.index(True)])
                cv2.putText(live,name[res.index(True)],(x1,y2),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255))
        cv2.imshow('image',live)
        k=cv2.waitKey(1)
        if(k==ord('q')):
            cv2.destroyAllWindows()
            break
        
        
    if(r==True):
        absent[res.index(True)]='P'
        newd['Atendence']=pd.DataFrame(absent,index=[0,1],columns=['Atendence'])
        newd.to_csv('Nattendence.csv',index=False)
        print(newd)

