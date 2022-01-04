#!/usr/bin/python
import os, sys, pyglet, tkinter, cv2, screen1, screen2, screen4
from pyglet.window import key
from pyglet.window import mouse
from tkinter import filedialog
from pyzbar import pyzbar
from attendance_encoder import *

# initialize window
window = pyglet.window.Window(width=900, height=800, caption='CCF Tanay Attendance')

def resource_path(relative_path):
    #Get absolute path to resource, works for dev and for PyInstaller
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)

icon = pyglet.image.load(resource_path('assets/icon.png'))
window.set_icon(icon)

# for files
masterlist_file = ''
file_location = ''
existing_file = ''

# for attendance encoder
past_code = ''
curr_code = ''
flag = 1

class StartingScreen:
    def __call__(self):
        display_masterlist_name = pyglet.text.Label(str(masterlist_file),
                                                    font_name='Arial',
                                                    font_size=14,
                                                    color=(1,161,183,255),
                                                    x=500, y=605,
                                                    width = 400,
                                                    multiline = True)
        
        display_fileloc_name = pyglet.text.Label(str(file_location),
                                                font_name='Arial',
                                                font_size=14,
                                                color=(1,161,183,255),
                                                x=572, y=400,
                                                width = 400,
                                                multiline = True)

        display_existingfile_name = pyglet.text.Label(str(existing_file),
                                                    font_name='Arial',
                                                    font_size=14,
                                                    color=(1,161,183,255),
                                                    x=500, y=195,
                                                    width = 400,
                                                    multiline = True)

        # screen types
        def screen1_base():
            @window.event
            def on_draw():
                window.clear()
                screen1.screen1_sprite.draw()
                screen1.continue_btn_sprite.draw()
                screen1.openfile1_btn_sprite.draw()
                screen1.openfile2_btn_sprite.draw()
                screen1.openfileloc_btn_sprite.draw()
                display_masterlist_name.draw()
                display_fileloc_name.draw()
                display_existingfile_name.draw()
        
        def screen1_openfile_na():
            @window.event
            def on_draw():
                window.clear()
                screen1.screen1_sprite.draw()
                screen1.continue_btn_sprite.draw()
                screen1.openfile1_btn_sprite.draw()
                screen1.openfile2_btnna_sprite.draw()
                screen1.openfileloc_btn_sprite.draw()
                display_masterlist_name.draw()
                display_fileloc_name.draw()
                display_existingfile_name.draw()
        
        def screen1_openfileloc_na():
            @window.event
            def on_draw():
                window.clear()
                screen1.screen1_sprite.draw()
                screen1.continue_btn_sprite.draw()
                screen1.openfile1_btn_sprite.draw()
                screen1.openfile2_btn_sprite.draw()
                screen1.openfileloc_btnna_sprite.draw()
                display_masterlist_name.draw()
                display_fileloc_name.draw()
                display_existingfile_name.draw()

        # mouse events
        @window.event
        def on_mouse_press(x, y, button, modifiers):
            if button == mouse.LEFT:
                # when mouse clicks CONTINUE button
                if x > 687 and x < 840 and y > 49 and y < 94:
                    @window.event
                    def on_draw():
                        screen1.continue_btnclick_sprite.draw()

                # when mouse clicks Masterlist - Open File button
                if x > 360 and x < 479 and y > 594 and y < 629:
                    @window.event
                    def on_draw():
                        screen1.openfile1_btnclick_sprite.draw()

                # when mouse clicks Existing - Open File button
                if x > 360 and x < 479 and y > 184 and y < 221 and file_location == '':
                    @window.event
                    def on_draw():
                        screen1.openfile2_btnclick_sprite.draw()
                
                # when mouse clicks Open File Location button
                if x > 360 and x < 545 and y > 390 and y < 426 and existing_file == '':
                    @window.event
                    def on_draw():
                        screen1.openfileloc_btnclick_sprite.draw()
        
        @window.event
        def on_mouse_release(x, y, button, modifiers):
            global masterlist_file
            global file_location
            global existing_file

            if button == mouse.LEFT:
                # when mouse clicks CONTINUE button
                if ((x > 687 and x < 840 and y > 49 and y < 94)
                    and masterlist_file != '' and (file_location != '' or existing_file != '')):
                    AttScreen()

                # when mouse clicks Masterlist - Open File button
                elif x > 360 and x < 479 and y > 594 and y < 629:
                    # open file dialog
                    root = tkinter.Tk()
                    root.withdraw()
                    masterlist_file = filedialog.askopenfilename(initialdir=os.path.expanduser("~/Desktop"), 
                                                                    filetypes=[("Excel file", "*.xlsx")])
                    root.destroy()
                    display_masterlist_name.text = str(masterlist_file)

                    if str(file_location) != '':
                        screen1_openfile_na()
                    elif str(existing_file) != '':
                        screen1_openfileloc_na()
                    else:
                        screen1_base()
                
                # when mouse clicks Existing - Open File button
                elif x > 361 and x < 478 and y > 184 and y < 221 and file_location == '':
                    # open file dialog
                    root = tkinter.Tk()
                    root.withdraw()
                    existing_file = filedialog.askopenfilename(initialdir=os.path.expanduser("~/Desktop"), 
                                                                    filetypes=[("Excel file", "*.xlsx")])
                    root.destroy()
                    display_existingfile_name.text = str(existing_file)

                    if str(existing_file) != '':
                        screen1_openfileloc_na()
                    else:
                        screen1_base()

                # when mouse clicks Open File Location button
                elif x > 360 and x < 545 and y > 390 and y < 426 and existing_file == '':
                    # open file location dialog
                    root = tkinter.Tk()
                    root.withdraw()
                    file_location = filedialog.askdirectory(initialdir=os.path.expanduser("~/Desktop"))
                    root.destroy()
                    display_fileloc_name.text = str(file_location)

                    if file_location != '':
                        screen1_openfile_na()
                    else:
                        screen1_base()

                else:
                    if str(file_location) != '':
                        screen1_openfile_na()
                    elif str(existing_file) != '':
                        screen1_openfileloc_na()
                    else:
                        screen1_base()
        
        screen1_base()
        
class AttendanceScreen:
    cam_flag = 0
    createdfile = "None"
    attendee_name = ''

    def __call__(self):
        display_attendee_name = pyglet.text.Label("",
                                                font_name='Arial',
                                                font_size=35,
                                                color=(1,161,183,255),
                                                x=310, y=370,
                                                multiline=True,
                                                width=525,
                                                align="center")

        # for displaying name of attendee
        def update_name(dt):
            if str(self.attendee_name) == "QR code is not recognized." or str(self.attendee_name) == "":
                display_attendee_name.text = str(self.attendee_name)
            else:
                display_attendee_name.text = "Hello, " + str(self.attendee_name) + ".\nWelcome to CCF Tanay!"

        # CAMERA FUNCTIONS
        def ReadQRcodes(frame, id_list, filename: str):
            global curr_code
            global past_code
            global flag

            qrcodes = pyzbar.decode(frame)
            for qrcode in qrcodes:
                x, y , w, h = qrcode.rect
                
                qrcode_info = qrcode.data.decode('utf-8')
                cv2.rectangle(frame, (x, y),(x+w, y+h), (183, 161, 1), 2)
        
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, qrcode_info, (x, y-5), font, 1, (183, 161, 1), 2)

                # check for new scan
                past_code = curr_code
                curr_code = str(qrcode_info)

                if curr_code == '' or curr_code != past_code:
                    flag = 0
                else:
                    flag = 1
                
                if flag == 0:
                    flag = 1

                    # encode attendee info
                    ## convert attendance file to dict
                    att_list = ConvertAttFile(filename)

                    ## check qr code
                    self.attendee_name = AddPerson(curr_code, id_list, att_list, filename)
                    screen2_opencam()

                else:
                    pass

            return frame

        def CameraMain(select: int, masterlist, filepath: str) -> str:
            filename = filepath

            # convert masterlist to dict
            id_list = ConvertMasterlist(masterlist)

            if select == 0:     # filepath: location -> NEW EXCEL FILE
                # create new file
                filename = CreateNewFile(filepath)

            elif select == 1:   # filepath: file -> EXISTING EXCEL FILE
                pass

            camera = cv2.VideoCapture(0)
            ret, frame = camera.read()
            
            while ret:
                ret, frame = camera.read()
                frame = ReadQRcodes(frame, id_list, filename)
                cv2.imshow('QR code reader', frame)

                if cv2.waitKey(1) & 0xFF == 27:
                    break
    
            camera.release()
            cv2.destroyAllWindows()
            screen2_base()
            return filename

        # RECORD ATTENDANCE
        def RecordAttendance():
            # new file
            if masterlist_file != '' and file_location != '' and existing_file == '':
                createdfile = CameraMain(0, masterlist_file, file_location)
                return createdfile

            # existing file
            elif masterlist_file != '' and existing_file != '' and file_location == '':
                CameraMain(1, masterlist_file, existing_file)
                return "None"
        
        # timer for refreshing scan and screen

        # screen types
        def screen2_base():
            @window.event
            def on_draw():
                window.clear()
                screen2.screen2_sprite.draw()
                screen2.input_btn_sprite.draw()
                screen2.exit_btn_sprite.draw()
                screen2.opencam_btn_sprite.draw()
        
        def screen2_opencam():
            @window.event
            def on_draw():
                window.clear()
                screen2.screen2_sprite.draw()
                screen2.input_btnna_sprite.draw()
                screen2.exit_btnna_sprite.draw()
                screen2.opencam_btnclick_sprite.draw()
                screen2.closecam_sprite.draw()
                display_attendee_name.draw()

        # mouse events
        @window.event
        def on_mouse_press(x, y, button, modifiers):
            if button == mouse.LEFT:
                # when mouse clicks OPEN CAM button
                if x > 60 and x < 160 and y > 325 and y < 420:
                    @window.event
                    def on_draw():
                        screen2.opencam_btnclick_sprite.draw()

                # when mouse clicks EXIT button        
                elif x > 60 and x < 160 and y > 45 and y < 140 and self.cam_flag == 0:
                    @window.event
                    def on_draw():
                        screen2.exit_btnclick_sprite.draw()
                
                # when mouse clicks INPUT button
                elif x > 60 and x < 160 and y > 185 and y < 280 and self.cam_flag == 0:
                    @window.event
                    def on_draw():
                        screen2.input_btnclick_sprite.draw()

        @window.event
        def on_mouse_release(x, y, button, modifiers):
            global file_location
            global existing_file

            if button == mouse.LEFT:
                # when mouse clicks OPEN CAM button
                if (x > 60 and x < 160 and y > 325 and y < 420):
                    self.cam_flag = 1

                # when mouse clicks EXIT button        
                elif (x > 60 and x < 160 and y > 45 and y < 140) and self.cam_flag == 0:
                    FinScreen()
                    pyglet.clock.unschedule(update_name)
                    return

            if self.cam_flag == 0:
                screen2_base()
            else:
                screen2_opencam()
                self.createdfile = RecordAttendance()
                self.cam_flag = 0

            # for reopening of camera
            if self.createdfile != "None":
                existing_file = self.createdfile
                file_location = ''

        #print current mouse position, remove laterrrr
        @window.event
        def on_mouse_motion(x, y, dx, dy):
            print(x,y)

        screen2_base()
        pyglet.clock.schedule_interval(update_name, 1/60)
        
class FinishScreen:
    def __call__(self):
        
        # for formatting purposes
        saved_file = ""
        if len(str(existing_file)) > 25:
            for y in range(25, len(existing_file) + 25, 25):
                saved_file = saved_file + (str(existing_file)[y-25:y]) + "\n"

        display_saved_file = pyglet.text.Label(str(saved_file),
                                                font_name='Arial',
                                                font_size=25,
                                                color=(1,161,183,255),
                                                x=310, y=460,
                                                multiline=True,
                                                width=510,
                                                align='center')
        # screen types
        def screen4_base():
            @window.event
            def on_draw():
                window.clear()
                screen4.screen4_sprite.draw()
                screen4.return_btn_sprite.draw()
                display_saved_file.draw()
        
        # mouse events
        @window.event
        def on_mouse_press(x, y, button, modifiers):
            if button == mouse.LEFT:
                # when mouse clicks RETURN button
                if x > 660 and x < 840 and y > 49 and y < 83:
                    @window.event
                    def on_draw():
                        screen4.return_btnclick_sprite.draw()
            
        @window.event
        def on_mouse_release(x, y, button, modifiers):
            global masterlist_file
            global file_location
            global existing_file

            if button == mouse.LEFT:
                # when mouse clicks RETURN button
                if x > 660 and x < 840 and y > 49 and y < 83:
                    masterlist_file = ""
                    file_location = ""
                    existing_file = ""
                    StartScreen()

                else:
                    screen4_base()

        """#print current mouse position, remove laterrrr
        @window.event
        def on_mouse_motion(x, y, dx, dy):
            print(x,y)"""

        screen4_base()

StartScreen = StartingScreen()
AttScreen = AttendanceScreen()
FinScreen = FinishScreen()

StartScreen()
window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()
