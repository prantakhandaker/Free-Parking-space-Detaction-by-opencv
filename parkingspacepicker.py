
import cv2
import pickle

width,height = (143-98), (131-111)


try:
    with open('CarParkPos','rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events,x,y,flags,params):
    if events ==cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    with open('CarParkPos','wb') as f:
        pickle.dump(posList,f)

while True:
    img = cv2.imread('carpark.png')
    cv2.rectangle(img, (98, 111), (143, 131), (255, 0, 255), 1)

    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),1)
    cv2.imshow('Image', img)

    cv2.setMouseCallback('Image',mouseClick)

    cv2.waitKey(1)