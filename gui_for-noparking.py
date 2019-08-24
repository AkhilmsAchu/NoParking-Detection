import tkinter
import cv2

from main import preprocess,extract_contours,cleanAndRead

viewwindow=tkinter.Tk()
viewwindow.title("No Parking Detection")
def livestream():
    cap=cv2.VideoCapture(0)

    if cap.isOpened():
           ret,frame=cap.read()
    else:
           ret=False
    while ret:
          
          ret,img=cap.read()
          
          cv2.imshow(viewwindow,img)
          print ("DETECTING PLATE . . .")
          #tkinter.Image(viewwindow,cv2.imwrite(img)).grid(row=1,column=0)
         
          if cv2.waitKey(1)==27:
             break;
    cv2.destroyAllWindows()
    cap.release()

#root menu initialised to understand

root_menu=tkinter.Menu(viewwindow)
viewwindow.config(menu=root_menu)


file_menu=tkinter.Menu(root_menu)


root_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="Open File",command=livestream)

file_menu.add_command(label="Live Stream",command=livestream)



viewwindow.mainloop()
