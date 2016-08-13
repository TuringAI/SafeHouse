from datetime import date, datetime
from Tkinter import *
import cv2
import nest

username = ""
password = ""
home_nest = nest.Nest(username, password)

day = datetime.today().timetuple().tm_yday
spring = range(80, 172)
summer = range(172, 264)
fall = range(264, 355)

class SafeHouse:
    def __init__(self, master):
        self.master = master
        master.title("SafeHouse Widget")

        #photo = PhotoImage(file="logo.png")

        self.label = Label(master, text="Your Appliances")
        self.label.pack()

        self.thermostat_button = Button(master, text="Thermostat", command=self.thermostat)
        self.thermostat_button.pack()

        self.thermostat_entry = Button(master, text="Thermostat", command=self.thermostat)
        self.thermostat_button.pack()

        self.refrigerator_button = Button(master, text="Refrigerator", command=self.refrigerator)
        self.refrigerator_button.pack()

        self.oven_button = Button(master, text="Oven", command=self.oven)
        self.oven_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def thermostat(self):
        for device in home_nest.devices:
            print '        Device: %s' % device.name

    def refrigerator(self):
        print("Here's a placeholder")

    def oven(self):
        print("Here's a placeholder")

face_cascade = cv2.CascadeClassifier("haar_face.xml")
eye_cascade = cv2.CascadeClassifier("haar_eye.xml")

def main():
    video_capture = cv2.VideoCapture(0)
    root = Tk()
    root.iconbitmap("favicon.ico")
    safehouse = SafeHouse(root)
    root.mainloop()
    while True:
        # Capture frame
        ret, frame = video_capture.read()
        # Convert to grayscale and detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, \
            minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        if len(faces) > 0:
        # If summer, make it hotter; if winter, make it colder
            if day in range(172, 264): #SUMMER
                for device in home_nest:
                    device.temp = 90
            if day in range(1, 79): #WINTER
                for device in home_nest:
                    device.temp = 20
        '''# Draw rectangle
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
        # Show whole frame
        cv2.imshow('Faces', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break'''
    # End the recording and close all windows
    video_capture.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
    
