import tkinter                                                        # IMPORTS
from tkinter import *
import pyautogui
import pydirectinput
import os
pyautogui.FAILSAFE = False

root = tkinter.Tk()                                            # SCREEN SETTINGS
root.title('Instalocker for toxic players')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - 600 / 2)
center_y = int(screen_height/2 - 200 / 2)
root.geometry(f'{600}x{800}+{center_x}+{center_y - 400}')
root.configure(bg = 'brown')
root.iconbitmap(os.path.abspath('icon1.ico'))

def raise_frame(frame,FRAME):
    FRAME.place_forget()
    frame.place(x = 100, y = 100)
def locate_and_click_the_target(image):
     t = None
     print(button_omen['state'])
     button_omen['state'] = 'disable'
     while t == None:
         print(t)
         print(button_omen['state'])
         t = pyautogui.locateCenterOnScreen(
                                            image,
                                            grayscale = True,
                                            confidence = 0.8
                                            )
     print(t)
     pydirectinput.click(t[0],t[1])
     pydirectinput.click(959,812)
     print('clicked')

f1 = Frame(root,bg = 'red',width = 400, height = 580)          # FRAME SWITCHING
f2 = Frame(root,bg = 'red')
#Label(f1,text = 'frame1').pack()
#Label(f2,text = 'frame2').pack()
button_map = tkinter.Button(
                            root,
                            text = 'select one agent',
                            bd=5,
                            relief = 'solid',
                            activeforeground = 'red',
                            activebackground = 'red',
                            command=lambda:raise_frame(f1,f2)
                            ).place(x = 50, y = 0)
button_agent = tkinter.Button(
                                root,
                                text = 'select agent by map',
                                bd=5,
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:raise_frame(f2,f1)
                                ).place(x = 400, y = 0)
raise_frame(f1,f2)

photo_sage = PhotoImage(file = 'chibi-sage 1.png')             # AGENT SELECTION
photo_sova = PhotoImage(file = 'chibi-sova 1.png')
photo_omen = PhotoImage(file = 'chibi-omen 1.png')
photo_yoru = PhotoImage(file = 'chibi-yoru 1.png')
photo_killjoy = PhotoImage(file = 'chibi-killjoy 1.png')
photo_raze = PhotoImage(file = 'chibi-raze 1.png')
photo_reyna = PhotoImage(file = 'chibi-reyna 1.png')
photo_viper = PhotoImage(file = 'chibi-viper 1.png')
button_sage = tkinter.Button(
                                f1,
                                image = photo_sage,
                                bd=5,
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:locate_and_click_the_target('sage.png')
                                )
button_sova = tkinter.Button(
                                f1,
                                image = photo_sova,
                                bd=5,
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:locate_and_click_the_target('sova.png')
                                )
button_omen = tkinter.Button(
                                f1,
                                image = photo_omen,
                                bd=5,
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:locate_and_click_the_target('omen.png')
                                )
button_killjoy = tkinter.Button(
                                f1,
                                image = photo_killjoy,
                                bd=5,
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:locate_and_click_the_target('killjoy.png')
                                )
button_raze = tkinter.Button(
                                f1,
                                image = photo_raze,
                                bd=5,
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:locate_and_click_the_target('raze.png')
                                )
button_yoru = tkinter.Button(
                                f1,
                                image = photo_yoru,
                                bd=5,
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:locate_and_click_the_target('yoru.png')
                                )
button_viper= tkinter.Button(
                                f1,
                                image = photo_viper,
                                bd=5,
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:locate_and_click_the_target('viper.png')
                                )
button_reyna = tkinter.Button(
                                f1,
                                image = photo_reyna,
                                bd=5,
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:locate_and_click_the_target('reyna.png')
                                )
button_omen.place(x = 20, y = 20)
button_yoru.place(x = 20, y = 300)
button_sage.place(x = 20, y = 160)
button_raze.place(x = 20, y = 440)
button_viper.place(x = 250, y = 20)
button_sova.place(x = 250, y = 160)
button_killjoy.place(x = 250, y = 300)
button_reyna.place(x = 250, y = 440)
L = [button_omen,button_yoru,button_raze,button_sage,button_viper,button_sova,button_killjoy,button_reyna]

mainloop()
