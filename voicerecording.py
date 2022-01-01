from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv

window = Tk()
window.geometry("610x710+410+15")
window.title("Voice Recorder")
window.configure(background="grey")

def fun_rec():
    freq = 44100
    dur = int(time_dur.get())
    temp_file = file_name.get()
    recording = sound.rec(dur*freq, samplerate=freq, channels=2)

    try :
        my_temp = int(time_dur.get())
    except:
        print("Do Print the correct value")

    while my_temp>0:
        window.update()
        time.sleep(1)
        my_temp = my_temp-1

        if my_temp ==0 :
            messagebox.showinfo("Time countdown here", "time is up")
        
        Label(text=f"{str(my_temp)}", font="Arial 40", width=4, background="grey").place(x=250, y=600)
    sound.wait()
    write(temp_file + ".wav", freq, recording)


icon_img = PhotoImage(file="icon.png")
window.iconphoto(False, icon_img)

img = PhotoImage(file="icon.png")
my_image = Label(image=img, background="grey")
my_image.pack(padx=15, pady=15)

Label(text="Voice Recorder", font=("Arial", 32, "bold"), background="grey", fg="black").pack()

time_dur = StringVar()
time_entry = Entry(window, textvariable=time_dur, font=("Arial", 32, "bold"), width=15).pack(pady=10)
Label(text="Enter the time in seconds", font=("Arial" , 17, "bold"), background="grey", fg="black", pady=15).pack()

file_name = StringVar()
file_entry = Entry(window, textvariable=file_name, font=("Arial", 32, "bold"), width=15).pack(pady=10)
Label(text="Enter the file name to save", font=("Arial" , 17, "bold"), background="grey", fg="black", pady=15).pack()

record_bt = Button(window , font=("Arial", 22 , "bold"), text="Record", bg="grey", fg="black", borderwidth=1, command=fun_rec , pady=2, padx=2).pack()

window.mainloop()
