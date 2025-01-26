import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller
screen_width = 1920  # Replace with your screen's width
screen_height = 1080  # Replace with your screen's height

cap = cv2.VideoCapture(0)
cap.set(3,screen_width  )  # Set width
cap.set(4,screen_height)   # Set height 

detector = HandDetector(detectionCon=0.8)
keys = [["Q","W","E","R","T","V","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L",";"],
        ["Z","X","C","V","B","N","M",",",".","/"],
        ]
finalText =''

keyboard = Controller()

#def drawALL(img, buttonList ):
    #for button in buttonList:
       # x,y = button.pos
       # w,h = button.size
#cv2.rectangle(img,button.pos,(x+w,y+h),(255,0,255),cv2.FILLED) 
       # cv2.putText(img,button.text,(x+20,y+65),
         #           cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
         # 
class Button():
    def __init__(self, pos, text, size=[85,85]):
        self.pos = pos 
        self.size = size
        self.text = text
         
        
    
buttonList = []
for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
                buttonList.append(Button([100 * j + 50,100 * i +50], key))

backspace_x_position = 100 * len(keys[2]) + 50  # Position based on keyboard width                
backspace_y_position = 100 * 2 + 50  # This should be below the keyboard 
buttonList.append(Button([backspace_x_position, backspace_y_position], "Backspace", size=[150, 85]))        
def drawAll(img, bottonList):
    imgNew = np.zeros_like(img,np.uint8)
    for button in buttonList:
        x,y = button.pos
        w,h = button.size
        radius = 20
        if button.text == "Backspace":
            text_size = 0.8
            text_offset_x = 2
            text_offset_y = h//2+10
            thickness = 1
        else:
            text_size = 4
            text_offset_x = 20
            text_offset_y = h//2+10
        cvzone.cornerRect(imgNew, (x,y,w,h),rt=radius, colorR=(150,150,150))
        cv2.rectangle(imgNew,button.pos,(x+ w,y+h),(169,169,169),cv2.FILLED) 
        cv2.putText(imgNew,button.text,(x+ text_offset_x,y+ text_offset_y),
                    cv2.FONT_HERSHEY_PLAIN, text_size, (255,255,255), 2) 
        
    out = img.copy()
    alpha = 0.2
    mask = imgNew.astype(bool)
    print(mask.shape)
    out[mask]= cv2.addWeighted(img,alpha,imgNew, 1-alpha , 0)[mask]
    return out 

def drawGreenBox(img, button, lmList):
    x, y = button.pos
    w, h = button.size
    if lmList and x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
        # Draw a green rectangle when the hand is over the button
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
 
while True:
    success, img = cap.read()
    img = cv2.flip(img,1) #inverting the hand movements
    
    # Check if the frame was successfully captured
    if not success or img is None:
        print("Failed to capture image")
        continue  # Skip the rest of the loop and try again

    # Detect hands if the frame is valid
    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)

    if hands:
        lmList = hands[0]['lmList']
        for button in buttonList:
            x,y = button.pos
            w,h = button.size
    
            if x< lmList[8][0] < x+w and y<lmList[8][1] < y+h:
                cv2.rectangle(img,button.pos,(x+w,y+h),(175, 0 ,175),cv2.FILLED) 
                cv2.putText(img,button.text,(x+20,y+65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
                point1 = lmList[8][:2]
                point2 = lmList[4][:2]
                l, _, _ = detector.findDistance(point1,point2, img,)
                
                #when clicked
                if l<30:
                    if button.text == "Backspace":
                        finalText = finalText[:-1]
                    else:     
                        keyboard.press(button.text)
                        cv2.rectangle(img,button.pos,(x+w,y+h),(0,255,0),cv2.FILLED) 
                        cv2.putText(img,button.text,(x+20,y+65),
                                 cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
                        finalText += button.text
                        sleep(0.15)
    (text_width,text_height), _ = cv2.getTextSize(finalText, cv2.FONT_HERSHEY_PLAIN, 5, 5)                
    cv2.rectangle(img,(50,350),(700,450),(255,255,204),cv2.FILLED) 
    cv2.putText(img,finalText,(60,430 ),
                cv2.FONT_HERSHEY_PLAIN, 5, (50,50,50), 5)            

    if hands:
        hand = hands[0]  # First detected hand
        lmList = hand['lmList']  # List of landmarks (21 points)
        bbox = hand['bbox']      # Bounding box info (x, y, w, h)

        # You can now use lmList and bbox for further processing
        print(f"Landmarks: {lmList}")
        print(f"Bounding Box: {bbox}")

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
