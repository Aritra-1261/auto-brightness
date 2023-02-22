from time import time
import cv2
import math as M
import screen_brightness_control as sbc

class capbr:
    def __init__(self):
        self.b_sum=0
    def cap(self):
        vid = cv2.VideoCapture(0)

        c_time=time()+2
        w_time=time()+0.15
        count=0   
        while(c_time>time()):
            
            # Capture the video frame
            # by frame
            ret, frame = vid.read()
             
            if(ret==True and time()>w_time):
                (B, G, R) = frame[100, 100]
                r,g,b=int(R),int(G),int(B)
                #calcuating the percieved brightness value
                k=(r+r+b+g+g+g)/6
                k=M.ceil((k/255)*100)
                count+=1
                self.b_sum+=k
        print(count)
        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return self.b_sum//count

def auto():
    capt=capbr()

    print("Previous Brightness :{}%".format(sbc.get_brightness()))

    #Auto set the brightness of the primary display
    sbc.set_brightness(capt.cap(), display=0)
    print("Current Brightness :{}%".format(sbc.get_brightness()))