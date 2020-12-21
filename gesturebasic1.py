import cv2
i=cv2.imread(r'C:\Users\Asif khan\Desktop\green.png')
j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
k=i[:,:,1]
g=cv2.subtract(j,k)
g=cv2.multiply(g,3)
cv2.imshow('image',j)
r,gb=cv2.threshold(g,80,255,0)
cnt,r=cv2.findContours(g,0,1) #with this zero we are neglecting the extra small contoures
if(len(cnt)>0):
    cv2.drawContours(i,cnt,-1,(0,0,255),5)

    cv2.imshow('contoure',i)
    cv2.imshow('final',gb)
    k=cv2.waitKey(0)
    cv2.destroyAllWindow()
