import cv2 as cv
import mediapipe as mp
import pyautogui as pg
import time 

# Set webcam resolution
def set_resolution(cap):
    cap.set(3,300)
    cap.set(4,300)

# Simulate keypress based on finger count
def press_key(count):
    if(count==4):
        pg.press('up')
        print("Pressed: UP arrow")
    elif(count==3):
        pg.press('down')
        print("Pressed: DOWN arrow")
    elif(count==2):
        pg.press('right')
        print("Pressed: RIGHT arrow")
    elif(count==1):
        pg.press('left')
        print("Pressed: LEFT arrow")
    elif(count==0):
        pg.press('space')
        print("Pressed: SPACE bar")

# Initialize MediaPipe and camera
hands_module=mp.solutions.hands
drawing_utils=mp.solutions.drawing_utils

capcturer=cv.VideoCapture(0)
set_resolution(capcturer)

tipsId=[4,8,12,16,20]
last_pressed_time=0
delay=0.35

with  hands_module.Hands(max_num_hands=1) as Hands:

    while True:
        _,frame=capcturer.read()

        frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        frame.flags.writeable=False
        results=Hands.process(frame)
        frame.flags.writeable=True
        frame=cv.cvtColor(frame,cv.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            hand_landmark = results.multi_hand_landmarks[0]
            label = results.multi_handedness[0].classification[0].label
            
            lmlist=[]
            h,w,c=frame.shape
            for id,lm in enumerate(hand_landmark.landmark):
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmlist.append([id, cx, cy])
            
            drawing_utils.draw_landmarks(frame,hand_landmark,hands_module.HAND_CONNECTIONS)
            
            fingers=[]

            # Thumb (based on hand orientation)
            if label=='Right':
                if lmlist[3][1]>lmlist[4][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            
            # Other fingers
            else:
                if lmlist[3][1]<lmlist[4][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)                
        
            for id in range(1, 5):
                if lmlist[tipsId[id]][2] < lmlist[tipsId[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            count=fingers.count(1)
            current_time=time.time()

            if current_time-last_pressed_time>delay:
                press_key(count)
                last_pressed_time=current_time
        
            cv.putText(frame, f'Count: {count}', (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv.imshow('Camera',frame)

        if cv.waitKey(3) & 0xFF == ord('q'):
            break

capcturer.release()
cv.destroyAllWindows()