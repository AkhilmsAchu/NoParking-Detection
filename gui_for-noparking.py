from tkinter import *
from PIL import Image,ImageTk
import cv2
import numpy as np



def livestream():
    
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
           ret,img=cap.read()
    else:
           ret=False
    #while ret:
          
    ret,img=cap.read()
    
    cv2.imshow("Contours",img)
    cv2.waitKey(0)
    
    b,g,r=cv2.split(img)
    img1=cv2.merge((r,g,b))
    im=Image.fromarray(img)
    imgtk=ImageTk.PhotoImage(image=im)
    Label(viewwindow,image=imgtk).pack()
   # if cv2.waitKey(1)==27:
    #    break;
   # root.mainloop()







if __name__=='__main__':
        
    viewwindow=Tk()
    viewwindow.title("No Parking Detection")
    canvas=Canvas(viewwindow,width=300,height=300)
    canvas.pack();
    root_menu=Menu(viewwindow)
    viewwindow.config(menu=root_menu)
#    
#    livestream()
    file_menu=Menu(root_menu)
#      
#    
    root_menu.add_cascade(label="File",menu=file_menu)
#    
    file_menu.add_command(label="Open File",command=livestream)
#    
    file_menu.add_command(label="Live Stream",command=livestream)
    viewwindow.mainloop()
#    img=tkinter.PhotoImage(file="testData/data.jpg")
#    canvas.create_image(20,20,anchor=tkinter.NW,image=img)
#    if cv2.waitKey(1)==27:
#          cv2.destroyAllWindows()
    
    
    
              #time.sleep(t)
          #cv2.imshow(windowname,img)
          #print ("DETECTING PLATE . . .")
    #img = cv2.imread("testData/Final.JPG")
          #threshold_img = preprocess(img)
          #contours= extract_contours(threshold_img)
    	#if len(contours)!=0:
    		#print len(contours) #Test
    		# cv2.drawContours(img, contours, -1, (0,255,0), 1)
    		# cv2.imshow("Contours",img)
    		# cv2.waitKey(0)
    
    
          #cleanAndRead(img,contours)
          
  #  cv2.destroyAllWindows()
   # cap.release()
    
    
   # imgpath="data.jpg"
          #img=cv2.imread(img)
            #print(img)
            #cv2.imshow(canvas,img)
            #cv2.waitKey(0)
#    
    