import tkinter as tk
from tkinter import ttk
from tkinter import Tk, font
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import textwrap
import pyttsx3
import random
import time
import os
import traceback
#from moviepy.editor import *
from tkinter import messagebox
from tkinter.scrolledtext import *
#from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips,concatenate_audioclips,TextClip,CompositeVideoClip


from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.editor import concatenate_videoclips,concatenate_audioclips,TextClip,CompositeVideoClip
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize

from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex






apache_log_file = r"apache log file.txt"
pure_silante_file_location = r"pure silent.mp3"
temp_voice  = r"TempVoiceFiles\temp.mp3"
on_image_location = r"power-gd0c2e4c17_1280.png"
off_image_location = r"button-gd1abd79bf_1280.png"
on_image_location2 = r"power-gd0c2e4c17_1280.png"
off_image_location2 = r"button-gd1abd79bf_1280.png"
location_of_frame = r"frame.png"
location_of_backup_frame = "backup Frame.jpg"

engine = pyttsx3.init()
voices = engine.getProperty('voices')

ws = Tk()
ws.title('Claro')
ws.geometry('620x930')
ws.config(bg='#345')

canvas = Canvas(
    ws,
    height=1024,
    width=720,
    bg="#474747"
    )

canvas.pack()

canvas.create_rectangle(
    #x1  y1  x2    y2
    0, 0, 0, 0,
    outline="#4E4E4E",
    fill="#4E4E4E")




def open_footage_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('All Suppoted Video Files', ".mp4 .m4p .m4v .mpg .mp2 .mpeg .mpe .mpv"),('RealMedia Variable Bitrate',".rmvb"),('MPEG Transport Stream',".MTS .M2TS .TS"),('QuickTime File Format',".mov .qt"),('Windows Media Video',".wmv"),('Raw video format',".yuv"),('Advanced Systems Format',".asf"),('Flash Video',".flv .f4v .f4p .f4a .f4b"),('WebM',".webm"),('Matroska',".mkv"),('Vob',".vob"),('All Files',"*")])
    print(file.name)

    locationVariable = tk.StringVar(value=file.name)
    tk.Entry(ws,textvariable=locationVariable, font=('Verdana',10)).place(x=337, y=81)

    footageLocationdll = r"AshipoohcallChio\footageLocation.dll"
    with open(footageLocationdll,'w') as footage_location_to_a_dll:
        footage_location_to_a_dll.write(str(file.name))

    footage_frame = VideoFileClip(file.name,audio=False)
    footage_frame.save_frame("frame.png")


    img  = Image.open("frame.png")
    image = img.resize((300, 250), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    lab=Label(image=photo).place(x=20,y=51)







def open_audio_file():
   file2 = filedialog.askopenfile(mode='r', filetypes=[('MP3',".mp3"),('All Files',"*")])
   print(file2.name)

   locationVariable2 = tk.StringVar(value=file2.name)
   tk.Entry(ws,textvariable=locationVariable2, font=('Verdana',10)).place(x=337, y=430)

   TTS_on_off_button = Button(text="Use Free TTS Service", state='disable',width=20,font=(r'Fonts\Poppins-Italic.ttf', 14, 'bold'), command=TTS_on_off)
   TTS_on_off_button.place(x=20, y=430)


   AudioLocationdllLocation = r"AshipoohcallChio\AudioLocation.dll"
   with open(AudioLocationdllLocation,'w') as Audio_Location_to_a_dll:
        Audio_Location_to_a_dll.write(str(file2.name))



#global is_on
is_on = True

label = Label(ws,
    text = "The Switch Is On!",
    fg = "green",
    font = ("Helvetica", 32))

label.pack(pady = 20)






def Switch():
    global is_on

    if is_on:
        button.config(image = off)
        label.config(text = "Switch is Off",
                        fg = "grey")
        is_on = False

        Label(ws, text='Silance Duration\n(Seconds)', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=367, y=170)
        silence_duration_input = tk.StringVar()
        silence_duration_input.set(1.5)
        tk.Entry(ws,width=3,textvariable = silence_duration_input,font=('Verdana',13)).place(x=487, y=176)


        Label(ws, text='Extra Seconds\n(Seconds)', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=377, y=220)
        Extra_Seconds_input = tk.IntVar()
        Extra_Seconds_input.set(2)
        tk.Entry(ws,width=3,textvariable = Extra_Seconds_input,font=('Verdana',13)).place(x=487, y=226)


        SilanceDurationLocationdll = r"AshipoohcallChio\SilanceDuration.dll"
        with open(SilanceDurationLocationdll,'w') as Silance_Duration_to_a_dll:
            Silance_Duration_to_a_dll.write(str(1.5))


        ExtraSecondsdllLocation = r"AshipoohcallChio\ExtraSeconds.dll"
        with open(ExtraSecondsdllLocation,'w') as Extra_Seconds_to_a_dll:
            Extra_Seconds_to_a_dll.write(str(2))



        def values2():
            print(silence_duration_input.get()) #This is a string
            print(Extra_Seconds_input.get())


            SilanceDurationLocationdll = r"AshipoohcallChio\SilanceDuration.dll"
            with open(SilanceDurationLocationdll,'w') as Silance_Duration_to_a_dll:
                Silance_Duration_to_a_dll.write(str(silence_duration_input.get()))


            ExtraSecondsdllLocation = r"AshipoohcallChio\ExtraSeconds.dll"
            with open(ExtraSecondsdllLocation,'w') as Extra_Seconds_to_a_dll:
                Extra_Seconds_to_a_dll.write(str(Extra_Seconds_input.get()))


        Button(ws, fg = "#ffffff", height=1, width= 15, text='Save Settings', bg='red',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: values2()).place(x=377, y=280)




    else:

        button.config(image = on)
        label.config(text = "Switch is On", fg = "green")
        is_on = True


        Label(ws, text='Silance Duration\n(Seconds)', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=367, y=170)
        silence_duration_input = tk.StringVar()
        silence_duration_input.set(1.5)
        tk.Entry(ws,width=3,textvariable = silence_duration_input,font=('Verdana',13),state='disabled').place(x=487, y=176)


        Label(ws, text='Extra Seconds\n(Seconds)', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=377, y=220)
        Extra_Seconds_input = tk.IntVar()
        Extra_Seconds_input.set(2)
        tk.Entry(ws,width=3,textvariable = Extra_Seconds_input,font=('Verdana',13),state='disabled').place(x=487, y=226)


        #Button(ws, fg = "#AAAAAA", height=1, width= 15, text='Save Settings', bg='#474747', state='disabled',font=(r'Fonts\Poppins-Italic.ttf', 16, 'bold'), command=lambda: values()).place(x=377, y=280)
        Button(ws, fg = "#AAAAAA", height=1, width= 15, text='Save Settings', bg='#474747',state='disabled',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: values()).place(x=377, y=280)






        SilanceDurationLocationdll = r"AshipoohcallChio\SilanceDuration.dll"
        with open(SilanceDurationLocationdll,'w') as Silance_Duration_to_a_dll:
            Silance_Duration_to_a_dll.write(str(1.5))


        ExtraSecondsdllLocation = r"AshipoohcallChio\ExtraSeconds.dll"
        with open(ExtraSecondsdllLocation,'w') as Extra_Seconds_to_a_dll:
            Extra_Seconds_to_a_dll.write(str(2))






canvas.create_line(0,340,960,340,fill = "white")
Label(ws, text='VIDEO', fg="lightblue",bg='green', font=(r'Fonts\PTSans-Bold.ttf',16, 'bold')).place(x=263, y=8)



Label(ws, text='Location of the video', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=337, y=51)
img  = Image.open(location_of_backup_frame)
image = img.resize((300, 250), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lab=Label(image=photo).place(x=20,y=51)

locationOfFootage = Text(ws, height=2, width=22) ; locationOfFootage.place(x=337, y=81)
Button(ws,fg = "#ffffff", height= 1, width= 6, text='   Browse   ', bg='red', font=(r'Fonts\Poppins-Italic.ttf', 14, 'bold'), command=open_footage_file).place(x=527, y=81)


try:
    os.remove(r"AshipoohcallChio\footageLocation.dll")
except:
    pass



Label(ws, text='Advanced Options', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',11, 'bold')).place(x=337, y=131)



on_png  = Image.open(on_image_location).resize((20, 20), Image.ANTIALIAS)
on =ImageTk.PhotoImage(on_png)
Label(image=on).place(x=480, y=131)



off_png  = Image.open(off_image_location).resize((20, 20), Image.ANTIALIAS)
off = ImageTk.PhotoImage(off_png)
Label(image=on).place(x=480, y=131)

button = Button(ws, image = on, bd = 0, command = Switch)
button.place(x=480, y=131)



Label(ws, text='Silance Duration\n(Seconds)', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=367, y=170)
silence_duration_input = tk.StringVar()
silence_duration_input.set(1.5)
tk.Entry(ws,width=3,textvariable = silence_duration_input,font=('Verdana',13),state='disabled').place(x=487, y=176)


Label(ws, text='Extra Seconds\n(Seconds)', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=377, y=220)
Extra_Seconds_input = tk.IntVar()
Extra_Seconds_input.set(2)
tk.Entry(ws,width=3,textvariable = Extra_Seconds_input,font=('Verdana',13),state='disabled').place(x=487, y=226)





SilanceDurationLocationdll = r"AshipoohcallChio\SilanceDuration.dll"
with open(SilanceDurationLocationdll,'w') as Silance_Duration_to_a_dll:
    Silance_Duration_to_a_dll.write(str(1.5))

ExtraSecondsdllLocation = r"AshipoohcallChio\ExtraSeconds.dll"
with open(ExtraSecondsdllLocation,'w') as Extra_Seconds_to_a_dll:
    Extra_Seconds_to_a_dll.write(str(2))




#Button(ws, fg = "#AAAAAA", height=1, width= 15, text='Save Settings', bg='#474747', state='disabled',font=(r'Fonts\Poppins-Italic.ttf', 16, 'bold'), command=lambda: values()).place(x=377, y=280)
Button(ws, fg = "#AAAAAA", height=1, width= 15, text='Save Settings', bg='#474747',state='disabled',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: values()).place(x=377, y=280)



canvas.create_line(0,340,960,340,fill = "white")
Label(ws, text='AUDIO', fg="lightblue",bg='green', font=(r'Fonts\PTSans-Bold.ttf',16, 'bold')).place(x=263, y=350)




Label(ws, text='Location to the voice file', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=337, y=400)
locationOfAudio = Text(ws, height=2, width=22) ; locationOfAudio.place(x=337, y=430)
Button(ws,fg = "#ffffff", height= 1, width= 6, text='   Browse   ', bg='red', font=(r'Fonts\Poppins-Italic.ttf', 14, 'bold'), command=open_audio_file).place(x=527, y=430)


Label(ws, text='OR', fg="yellow",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=285, y=430)




def TTS_on_off():

    if TTS_on_off_button.config('text')[-1] == 'ON':
        TTS_on_off_button.config(text='OFF')

        Label(ws, text='Location to the voice file', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=337, y=400)
        locationOfAudio = Text(ws, height=2, width=22) ; locationOfAudio.place(x=337, y=430)
        Button(ws,fg = "#ffffff", height= 1, width= 6, text='   Browse   ', bg='red', font=(r'Fonts\Poppins-Italic.ttf', 14, 'bold'), command=open_audio_file).place(x=527, y=430)


        Label(ws, text='Sentence', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=20, y=480)
        Sentence_input = Text(ws,height =1, width=53,font=('Verdana',13),state='disabled') ; Sentence_input.place(x=20, y=500)

        #Label(ws, text='Male', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=20, y=530)



        def print_selection():
            if (Male_checkbox_value.get() == 1):
                print("Male is ticked")



                voicer_name = StringVar(ws)
                voicer_name.set("Microsoft David") # default value


                def Male_voices(voicer_name):
                    print(voicer_name)

                options = OptionMenu(ws, voicer_name, "Microsoft David",command=Male_voices)
                options.config(font=('verdana','10'))
                options.place(x=20,y=580)


            elif (Male_checkbox_value.get() == 0):
                print("Male is not ticked")

            if (Female_checkbox_value.get() == 1):
                print("Female is ticked")

                voicer_name = StringVar(ws)
                voicer_name.set("Microsoft Hazel") # default value


                def female_voices(voicer_name):
                    print(voicer_name)

                options = OptionMenu(ws, voicer_name, "Microsoft Hazel","Microsoft Zira",command=female_voices)
                options.config(font=('verdana','10'))
                options.place(x=20,y=580)


            elif (Female_checkbox_value.get() == 0):
                print("Female is not ticked")





        Male_checkbox_value = tk.IntVar()
        Male_checkbox = tk.Checkbutton(ws,state='disabled',font=('verdana','10') ,text='Male',variable=Male_checkbox_value, onvalue=1, offvalue=0, command=print_selection)
        Male_checkbox.place(x=20,y=540)

        Female_checkbox_value = tk.IntVar()
        Female_checkbox = tk.Checkbutton(ws,state='disabled',font=('verdana','10'), text='Female',variable=Female_checkbox_value, onvalue=1, offvalue=0, command=print_selection)
        Female_checkbox.place(x=100,y=540)



        voicer_name = StringVar(ws)
        voicer_name.set("Not Selected") # default value


        def voices(voicer_name):
            print(voicer_name)

        #options = OptionMenu(ws,voicer_name, "Not Selected",command=voices)
        #options.config(font=('verdana','10'))
        #options.place(x=20,y=580)


        Label(ws,text='Speed Rate\n(Seconds)', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=240, y=540)
        Speed_Rate = tk.IntVar()
        Speed_Rate.set(120)
        textExample = tk.Entry(ws,state='disabled',textvariable = Speed_Rate,width=5)
        textExample.place(x=330,y=550)

        Button(ws, fg = "#AAAAAA", height=1, width= 15, text='Listen', bg='#474747',state='disabled',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: Speed_rate()).place(x=440, y=540)
        Button(ws, fg = "#AAAAAA", height=1, width= 15, text='Save Settings', bg='#474747',state='disabled',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: Listen_to()).place(x=440, y=580)


        SpeedRatedllLocation = r"AshipoohcallChio\SpeedRate.dll"
        with open(SpeedRatedllLocation,'w') as Speed_Rate_to_a_dll:
            Speed_Rate_to_a_dll.write(str(120))


        try:
            os.remove("AshipoohcallChio\Sentence.dll")
            os.remove("AshipoohcallChio\VoicerName.dll")
        except:
            os.remove("AshipoohcallChio\VoicerName.dll")
            os.remove("AshipoohcallChio\Sentence.dll")





        def Speed_rate():
            print(Speed_Rate.get())
            print(Sentence_input.get("1.0","end-1c"))



        def Listen_to():
            print("")













    else:
        TTS_on_off_button.config(text='ON')

        Label(ws, text='Location to the voice file', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=337, y=400)
        locationOfAudio = Text(ws,state='disable', height=2, width=22) ; locationOfAudio.place(x=337, y=430)
        Button(ws,state='disable',fg = "#ffffff", height= 1, width= 6, text='   Browse   ', bg='#474747', font=(r'Fonts\Poppins-Italic.ttf', 14, 'bold'), command=open_audio_file).place(x=527, y=430)



        Label(ws, text='Sentence', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=20, y=480)
        Sentence_input = Text(ws,height =1, width=53,font=('Verdana',13)) ; Sentence_input.place(x=20, y=500)

        #Label(ws, text='Male', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=20, y=530)



        def print_selection():
            if (Male_checkbox_value.get() == 1):
                print("Male is ticked")



                voicer_name = StringVar(ws)
                voicer_name.set("Microsoft David") # default value


                def Male_voices(voicer_name):
                    print(voicer_name)


                    VoicerNamedllLocation = r"AshipoohcallChio\VoicerName.dll"
                    with open(VoicerNamedllLocation,'w') as Voicer_Name_to_a_dll:
                        Voicer_Name_to_a_dll.write(voicer_name)



                options = OptionMenu(ws, voicer_name, "Microsoft David",command=Male_voices)
                options.config(font=('verdana','10'))
                options.place(x=20,y=580)


            elif (Male_checkbox_value.get() == 0):
                print("Male is not ticked")

            if (Female_checkbox_value.get() == 1):
                print("Female is ticked")

                voicer_name = StringVar(ws)
                voicer_name.set("Microsoft Hazel") # default value


                def female_voices(voicer_name):
                    print(voicer_name)

                    VoicerNamedllLocation = r"AshipoohcallChio\VoicerName.dll"
                    with open(VoicerNamedllLocation,'w') as Voicer_Name_to_a_dll:
                        Voicer_Name_to_a_dll.write(voicer_name)

                options = OptionMenu(ws, voicer_name, "Microsoft Hazel","Microsoft Zira",command=female_voices)
                options.config(font=('verdana','10'))
                options.place(x=20,y=580)


            elif (Female_checkbox_value.get() == 0):
                print("Female is not ticked")





        Male_checkbox_value = tk.IntVar()
        Male_checkbox = tk.Checkbutton(ws,font=('verdana','10') ,text='Male',variable=Male_checkbox_value, onvalue=1, offvalue=0, command=print_selection)
        Male_checkbox.place(x=20,y=540)

        Female_checkbox_value = tk.IntVar()
        Female_checkbox = tk.Checkbutton(ws,font=('verdana','10'), text='Female',variable=Female_checkbox_value, onvalue=1, offvalue=0, command=print_selection)
        Female_checkbox.place(x=100,y=540)



        voicer_name = StringVar(ws)
        voicer_name.set("Not Selected") # default value


        #def voices(voicer_name):
        #    print(voicer_name)

        #options = OptionMenu(ws,voicer_name, "Not Selected",command=voices)
        #options.config(font=('verdana','10'))
        #options.place(x=20,y=580)


        Label(ws,text='Speed Rate\n(Seconds)', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=240, y=540)
        Speed_Rate = tk.IntVar()
        Speed_Rate.set(120)
        textExample = tk.Entry(ws,textvariable = Speed_Rate,width=5)
        textExample.place(x=330,y=550)



        def Speed_rate():
            print(Speed_Rate.get())
            print(Sentence_input.get("1.0","end-1c"))



            SentencedllLocation = r"AshipoohcallChio\Sentence.dll"
            with open(SentencedllLocation,'w') as Sentence_to_a_dll:
                Sentence_to_a_dll.write(str(Sentence_input.get("1.0","end-1c")))



            SpeedRatedllLocation = r"AshipoohcallChio\SpeedRate.dll"
            with open(SpeedRatedllLocation,'w') as Speed_Rate_to_a_dll:
                Speed_Rate_to_a_dll.write(str(Speed_Rate.get()))



            Button(ws,fg = "#FFFFFF", height=1, width= 15, text='Listen', bg='red',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: Listen_to()).place(x=440, y=540)




        def Listen_to():
            SpeedRatedllLocation = r"AshipoohcallChio\SpeedRate.dll"
            with open(SpeedRatedllLocation,'r') as Speed_Rate_dll:
                Speed_Rate_Location = Speed_Rate_dll.readline()
            print("dll -",Speed_Rate_Location)

            SentencedllLocation = r"AshipoohcallChio\Sentence.dll"
            with open(SentencedllLocation,'r') as Sentence_from_dll:
                Sentence_location = Sentence_from_dll.readline()
            print("dll -",Sentence_location)

            VoicerNamedllLocation = r"AshipoohcallChio\VoicerName.dll"
            with open(VoicerNamedllLocation,'r') as Voicer_Name_from_dll:
                Voicer_Name_location = Voicer_Name_from_dll.readline()
            print("dll -",Voicer_Name_location)



            engine = pyttsx3.init()
            voices = engine.getProperty('voices')

            speed_rate = float(Speed_Rate_Location)
            Text_To_Speak = Sentence_location

            Path_to_save_the_voice  = temp_voice
            male_voices = (0)
            female_voices = (1,2)

            if "Hazel" in Voicer_Name_location:
                engine.setProperty('voice', voices[1].id)
                engine. setProperty("rate", speed_rate)
                engine.say(Text_To_Speak)
                engine.runAndWait()

            elif "Zira" in Voicer_Name_location:
                engine.setProperty('voice', voices[2].id)
                engine. setProperty("rate", speed_rate)
                engine.say(Text_To_Speak)
                engine.runAndWait()


            elif "David" in Voicer_Name_location:
                engine.setProperty('voice', voices[0].id)
                engine. setProperty("rate", speed_rate)
                engine.say(Text_To_Speak)
                engine.runAndWait()




        Button(ws,state='disable',fg = "#FFFFFF", height=1, width= 15, text='Listen', bg='#474747',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: Listen_to()).place(x=440, y=540)
        Button(ws, fg = "#FFFFFF", height=1, width= 15, text='Save Settings', bg='red',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: Speed_rate()).place(x=440, y=580)






TTS_on_off_button = Button(text="Use Free TTS Service", width=20,font=(r'Fonts\Poppins-Italic.ttf', 14, 'bold'), command=TTS_on_off)
TTS_on_off_button.place(x=20, y=430)


Label(ws, text='Sentence', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=20, y=480)
Sentence_input = Text(ws,height =1, width=53,font=('Verdana',13),state='disabled') ; Sentence_input.place(x=20, y=500)

#Label(ws, text='Male', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=20, y=530)



def print_selection():
    if (Male_checkbox_value.get() == 1):
        print("Male is ticked")



        voicer_name = StringVar(ws)
        voicer_name.set("Microsoft David") # default value


        def Male_voices(voicer_name):
            print(voicer_name)

        options = OptionMenu(ws, voicer_name, "Microsoft David",command=Male_voices)
        options.config(font=('verdana','10'))
        options.place(x=20,y=580)


    elif (Male_checkbox_value.get() == 0):
        print("Male is not ticked")

    if (Female_checkbox_value.get() == 1):
        print("Female is ticked")

        voicer_name = StringVar(ws)
        voicer_name.set("Microsoft Hazel") # default value


        def female_voices(voicer_name):
            print(voicer_name)

        options = OptionMenu(ws, voicer_name, "Microsoft Hazel","Microsoft Zira",command=female_voices)
        options.config(font=('verdana','10'))
        options.place(x=20,y=580)


    elif (Female_checkbox_value.get() == 0):
        print("Female is not ticked")





Male_checkbox_value = tk.IntVar()
Male_checkbox = tk.Checkbutton(ws,state='disabled',font=('verdana','10') ,text='Male',variable=Male_checkbox_value, onvalue=1, offvalue=0, command=print_selection)
Male_checkbox.place(x=20,y=540)

Female_checkbox_value = tk.IntVar()
Female_checkbox = tk.Checkbutton(ws,state='disabled',font=('verdana','10'), text='Female',variable=Female_checkbox_value, onvalue=1, offvalue=0, command=print_selection)
Female_checkbox.place(x=100,y=540)



voicer_name = StringVar(ws)
voicer_name.set("Not Selected") # default value


def voices(voicer_name):
    print(voicer_name)

#options = OptionMenu(ws,voicer_name, "Not Selected",command=voices)
#options.config(font=('verdana','10'))
#options.place(x=20,y=580)


Label(ws,text='Speed Rate\n(Seconds)', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=240, y=540)
Speed_Rate = tk.IntVar()
Speed_Rate.set(120)
textExample = tk.Entry(ws,state='disabled',textvariable = Speed_Rate,width=5)
textExample.place(x=330,y=550)

Button(ws, fg = "#AAAAAA", height=1, width= 15, text='Listen', bg='#474747',state='disabled',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: Speed_rate()).place(x=440, y=540)
Button(ws, fg = "#AAAAAA", height=1, width= 15, text='Save Settings', bg='#474747',state='disabled',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: Listen_to()).place(x=440, y=580)


try:
    os.remove("AshipoohcallChio\Sentence.dll")
    os.remove("AshipoohcallChio\VoicerName.dll")
except:

    Error = traceback.format_exc()


    try:
        if "AshipoohcallChio\\VoicerName.dll" in Error:
            os.remove("AshipoohcallChio\Sentence.dll")

        elif "AshipoohcallChio\\Sentence.dll" in Error:
            os.remove("AshipoohcallChio\VoicerName.dll")

    except:
        pass



    print(Error)


SpeedRatedllLocation = r"AshipoohcallChio\SpeedRate.dll"
with open(SpeedRatedllLocation,'w') as Speed_Rate_to_a_dll:
    Speed_Rate_to_a_dll.write(str(120))







def Speed_rate():
    print(Speed_Rate.get())
    print(Sentence_input.get("1.0","end-1c"))

def Listen_to():
    print("")

try:
    os.remove("AshipoohcallChio\AudioLocation.dll")
except:
    pass













def Text_Sentence():
    print(Sentence_input_to_TEXT.get("1.0","end-1c"))


    #SenteseByTextdll = r"AshipoohcallChio\SenteseByText.dll"
    #with open(SenteseByTextdll,'w') as Sentese_By_Text_to_a_dll:
        #Sentese_By_Text_to_a_dll.write(str(Sentence_input_to_TEXT.get("1.0","end-1c")))






canvas.create_line(0,640,960,640,fill = "white")
Label(ws, text='TEXT', fg="lightblue",bg='green', font=(r'Fonts\PTSans-Bold.ttf',16, 'bold')).place(x=263, y=650)
Label(ws, text='Sentence', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=20, y=670)

Sentence_input_to_TEXT = Text(ws,height =1, width=53,font=('Verdana',13)) ; Sentence_input_to_TEXT.place(x=20, y=700)
#Sentence_input_to_TEXT = Text(ws,height =1, width=44,font=('Verdana',13)) ; Sentence_input_to_TEXT.place(x=20, y=700)
#Button(ws,fg = "#ffffff", height= 1, width= 6, text='   Append   ', bg='red', font=(r'Fonts\Poppins-Italic.ttf', 14, 'bold'), command=Text_Sentence).place(x=527, y=692)


#global is_on2
is_on2 = True

def Switch2():
    global is_on2

    if is_on2:
        button2.config(image = off2)
        is_on2 = False


        Label(ws, text='Font', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=50, y=780)



        font_name = StringVar(ws)
        font_name.set("Verdana") # default value


        def selecting_font_func(font_name):
            print(font_name)

            fontdll = r"AshipoohcallChio\font.dll"
            with open(fontdll,'w') as fontdll_to_a_dll:
                fontdll_to_a_dll.write(str(font_name))


        all_system_fonts = font.families()
        selecting_font = OptionMenu(ws, font_name, *all_system_fonts,command=selecting_font_func)
        selecting_font.config(font=('Gisha','5','bold'))
        selecting_font.place(x=90,y=780)

        def values():
            print(FontSize_input.get())

            fontSizedll = r"AshipoohcallChio\fontSize.dll"
            with open(fontSizedll,'w') as fontSizedll_to_a_dll:
                fontSizedll_to_a_dll.write(str(FontSize_input.get()))


        Label(ws, text='Font Size', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=200, y=780)
        FontSize_input = tk.StringVar()
        FontSize_input.set("50")
        textExample = tk.Entry(ws,width=5,textvariable = FontSize_input)
        textExample.place(x=265,y=780)


        Label(ws, text='Text X Pos', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=330, y=780)
        Text_X_Pos_input = tk.StringVar()
        Text_X_Pos_input.set("10")
        textExample = tk.Entry(ws,width=5,textvariable = Text_X_Pos_input)
        textExample.place(x=405,y=780)


        Label(ws, text='Text Y Pos', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=50, y=830)
        Text_Y_Pos_input = tk.StringVar()
        Text_Y_Pos_input.set("4.3")
        textExample = tk.Entry(ws,width=5,textvariable = Text_Y_Pos_input)
        textExample.place(x=128,y=830)



        Label(ws, text='Color', fg="#FFFFFF",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=200, y=830)
        Text_Color_input = tk.StringVar()
        Text_Color_input.set("#FFFFFF")
        textExample = tk.Entry(ws,width=10,textvariable = Text_Color_input)
        textExample.place(x=265,y=830)

        Button(ws, fg = "#FFFFFF", height=1, width= 15, text='Save Settings', bg='red',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: values3()).place(x=440, y=830)

        def values3():
            print(Text_Color_input.get())
            print(Text_Y_Pos_input.get())
            print(Text_X_Pos_input.get())
            print(FontSize_input.get())


            fontSizedll = r"AshipoohcallChio\fontSize.dll"
            with open(fontSizedll,'w') as fontSizedll_to_a_dll:
                fontSizedll_to_a_dll.write(str(FontSize_input.get()))

            TextXposdll = r"AshipoohcallChio\TextXpos.dll"
            with open(TextXposdll,'w') as Text_X_pos_dll_to_a_dll:
                Text_X_pos_dll_to_a_dll.write(str(Text_X_Pos_input.get()))

            TextYposdll = r"AshipoohcallChio\TextYpos.dll"
            with open(TextYposdll,'w') as Text_Y_pos_dll_to_a_dll:
                Text_Y_pos_dll_to_a_dll.write(str(Text_Y_Pos_input.get()))

            TextColordll = r"AshipoohcallChio\TextColor.dll"
            with open(TextColordll,'w') as Text_Color_to_a_dll:
                Text_Color_to_a_dll.write(str(Text_Color_input.get()))








    else:

        button2.config(image = on2)
        is_on2 = True






        Label(ws, text='Font', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=50, y=780)



        font_name = StringVar(ws)
        font_name.set("Verdana") # default value


        def selecting_font_func(font_name):
            print(font_name)

        all_system_fonts = font.families()
        selecting_font = OptionMenu(ws, font_name, *all_system_fonts,command=selecting_font_func)
        selecting_font.config(font=('Gisha','5','bold'),state='disabled')
        selecting_font.place(x=90,y=780)

        def values():
            print(FontSize_input.get())


        Label(ws, text='Font Size', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=200, y=780)
        FontSize_input = tk.StringVar()
        FontSize_input.set("50")
        textExample = tk.Entry(ws,state='disabled',width=5,textvariable = FontSize_input)
        textExample.place(x=265,y=780)


        Label(ws, text='Text X Pos', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=330, y=780)
        Text_X_Pos_input = tk.StringVar()
        Text_X_Pos_input.set("10")
        textExample = tk.Entry(ws,state='disabled',width=5,textvariable = Text_X_Pos_input)
        textExample.place(x=405,y=780)


        Label(ws, text='Text Y Pos', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=50, y=830)
        Text_Y_Pos_input = tk.StringVar()
        Text_Y_Pos_input.set("4.3")
        textExample = tk.Entry(ws,state='disabled',width=5,textvariable = Text_Y_Pos_input)
        textExample.place(x=128,y=830)



        Label(ws, text='Color', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=200, y=830)
        Text_Color_input = tk.StringVar()
        Text_Color_input.set("#FFFFFF")
        textExample = tk.Entry(ws,state='disabled',width=10,textvariable = Text_Color_input)
        textExample.place(x=265,y=830)

        Button(ws,state='disabled', fg = "#FFFFFF", height=1, width= 15, text='Save Settings', bg='#474747',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: values3()).place(x=440, y=830)

        def values3():
            print(Text_Color_input.get())
            print(Text_Y_Pos_input.get())
            print(Text_X_Pos_input.get())
            print(FontSize_input.get())



        fontdll = r"AshipoohcallChio\font.dll"
        with open(fontdll,'w') as fontdll_to_a_dll:
            fontdll_to_a_dll.write('verdana')

        fontSizedll = r"AshipoohcallChio\fontSize.dll"
        with open(fontSizedll,'w') as fontSizedll_to_a_dll:
            fontSizedll_to_a_dll.write(str(50))


        TextXposdll = r"AshipoohcallChio\TextXpos.dll"
        with open(TextXposdll,'w') as Text_X_pos_dll_to_a_dll:
            Text_X_pos_dll_to_a_dll.write(str(10))

        TextYposdll = r"AshipoohcallChio\TextYpos.dll"
        with open(TextYposdll,'w') as Text_Y_pos_dll_to_a_dll:
            Text_Y_pos_dll_to_a_dll.write(str(4.3))

        TextColordll = r"AshipoohcallChio\TextColor.dll"
        with open(TextColordll,'w') as Text_Color_to_a_dll:
            Text_Color_to_a_dll.write('#FFFFFF')





Label(ws, text='Advanced Options', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',11, 'bold')).place(x=20, y=735)
on_png2  = Image.open(on_image_location).resize((20, 20), Image.ANTIALIAS)
on2 =ImageTk.PhotoImage(on_png2)
Label(image=on2).place(x=180, y=735)

off_png2  = Image.open(off_image_location).resize((20, 20), Image.ANTIALIAS)
off2 = ImageTk.PhotoImage(off_png2)
Label(image=off2).place(x=180, y=735)

button2 = Button(ws, image = on2, bd = 0,command = Switch2)
button2.place(x=180, y=735)
Label(ws, text='Font', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=50, y=780)



font_name = StringVar(ws)
font_name.set("Verdana") # default value


def selecting_font_func(font_name):
    print(font_name)


all_system_fonts = font.families()
selecting_font = OptionMenu(ws, font_name, *all_system_fonts,command=selecting_font_func)
selecting_font.config(font=('Gisha','5','bold'),state='disabled')
selecting_font.place(x=90,y=780)


fontdll = r"AshipoohcallChio\font.dll"
with open(fontdll,'w') as fontdll_to_a_dll:
    fontdll_to_a_dll.write('verdana')




def values():
    print(FontSize_input.get())


Label(ws, text='Font Size', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=200, y=780)
FontSize_input = tk.StringVar()
FontSize_input.set("50")
textExample = tk.Entry(ws,state='disabled',width=5,textvariable = FontSize_input)
textExample.place(x=265,y=780)


Label(ws, text='Text X Pos', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=330, y=780)
Text_X_Pos_input = tk.StringVar()
Text_X_Pos_input.set("10")
textExample = tk.Entry(ws,state='disabled',width=5,textvariable = Text_X_Pos_input)
textExample.place(x=405,y=780)


Label(ws, text='Text Y Pos', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=50, y=830)
Text_Y_Pos_input = tk.StringVar()
Text_Y_Pos_input.set("4.3")
textExample = tk.Entry(ws,state='disabled',width=5,textvariable = Text_Y_Pos_input)
textExample.place(x=128,y=830)



Label(ws, text='Color', fg="#AAAAAA",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',9, 'bold')).place(x=200, y=830)
Text_Color_input = tk.StringVar()
Text_Color_input.set("#FFFFFF")
textExample = tk.Entry(ws,state='disabled',width=10,textvariable = Text_Color_input)
textExample.place(x=265,y=830)

Button(ws,state='disabled', fg = "#FFFFFF", height=1, width= 15, text='Save Settings', bg='#474747',font=(r'Fonts\Poppins-Italic.ttf', 10, 'bold'), command=lambda: values3()).place(x=440, y=830)
canvas.create_line(0,865,960,865,fill = "white")



def values3():
    print(Text_Color_input.get())
    print(Text_Y_Pos_input.get())
    print(Text_X_Pos_input.get())
    print(FontSize_input.get())


fontdll = r"AshipoohcallChio\font.dll"
with open(fontdll,'w') as fontdll_to_a_dll:
    fontdll_to_a_dll.write('verdana')

fontSizedll = r"AshipoohcallChio\fontSize.dll"
with open(fontSizedll,'w') as fontSizedll_to_a_dll:
    fontSizedll_to_a_dll.write(str(50))


TextXposdll = r"AshipoohcallChio\TextXpos.dll"
with open(TextXposdll,'w') as Text_X_pos_dll_to_a_dll:
    Text_X_pos_dll_to_a_dll.write(str(10))

TextYposdll = r"AshipoohcallChio\TextYpos.dll"
with open(TextYposdll,'w') as Text_Y_pos_dll_to_a_dll:
    Text_Y_pos_dll_to_a_dll.write(str(4.3))

TextColordll = r"AshipoohcallChio\TextColor.dll"
with open(TextColordll,'w') as Text_Color_to_a_dll:
    Text_Color_to_a_dll.write('#FFFFFF')




try:
    os.remove("AshipoohcallChio\SenteseByText.dll")
except:
    pass






def Render(): #The main function
    #for widgets in ws.winfo_children():
      #widgets.destroy()
    SenteseByTextdll = r"AshipoohcallChio\SenteseByText.dll"
    with open(SenteseByTextdll,'w') as Sentese_By_Text_to_a_dll:
        Sentese_By_Text_to_a_dll.write(str(Sentence_input_to_TEXT.get("1.0","end-1c")))

    essen_var = 0
    audio_var = 0

    try:
        footageLocationdll = r"AshipoohcallChio\footageLocation.dll"
        with open(footageLocationdll,'r') as footage_location_from_dll:
            footage_location_dll = footage_location_from_dll.readline()
        print(footage_location_dll)
        essen_var = essen_var+1




        SenteseByTextdll = r"AshipoohcallChio\SenteseByText.dll"
        with open(SenteseByTextdll,'r') as Sentese_By_Text_Location_from_dll:
            Sentence_by_text_Location = Sentese_By_Text_Location_from_dll.readline()
        print(Sentence_by_text_Location)
        essen_var = essen_var+1


        if Sentence_by_text_Location == "":
            messagebox.showinfo('Error', "Plese Enter a Sentence.")
            essen_var = essen_var-1


        SilanceDurationLocationdll = r"AshipoohcallChio\SilanceDuration.dll"
        with open(SilanceDurationLocationdll,'r') as Silance_Duration_Location_location_dll:
            Silance_Duration_Location = Silance_Duration_Location_location_dll.readline()
        print(Silance_Duration_Location)
        essen_var = essen_var+1



        ExtraSecondsdllLocation = r"AshipoohcallChio\ExtraSeconds.dll"
        with open(ExtraSecondsdllLocation,'r') as ExtraSecondsdllLocation_from_dll:
            Extra_Seconds_location = ExtraSecondsdllLocation_from_dll.readline()
        print(Extra_Seconds_location)
        essen_var = essen_var+1



        fontdll = r"AshipoohcallChio\font.dll"
        with open(fontdll,'r') as font_from_dll:
            font_location = font_from_dll.readline()
        print(font_location)
        essen_var = essen_var+1



        fontSizedll = r"AshipoohcallChio\fontSize.dll"
        with open(fontSizedll,'r') as font_Size_dll_from_dll:
            font_Sized_location = font_Size_dll_from_dll.readline()
        print(font_Sized_location)
        essen_var = essen_var+1



        TextXposdll = r"AshipoohcallChio\TextXpos.dll"
        with open(TextXposdll,'r') as TextXposdll_dll_from_dll:
            Text_X_pos_location = TextXposdll_dll_from_dll.readline()
        print(Text_X_pos_location)
        essen_var = essen_var+1


        TextYposdll = r"AshipoohcallChio\TextYpos.dll"
        with open(TextYposdll,'r') as TextYposdll_dll_from_dll:
            Text_Y_pos_location = TextYposdll_dll_from_dll.readline()
        print(Text_Y_pos_location)
        essen_var = essen_var+1

        TextColordll = r"AshipoohcallChio\TextColor.dll"
        with open(TextColordll,'r') as TextColor_from_dll:
            Text_Color_location = TextColor_from_dll.readline()
        print(Text_Color_location)
        essen_var = essen_var+1


        try:
            AudioLocationdllLocation = r"AshipoohcallChio\AudioLocation.dll"
            with open(AudioLocationdllLocation,'r') as AudioLocation_from_dll:
                Audio_Location = AudioLocation_from_dll.readline()
            print("dll -",Audio_Location)
            audio_var = audio_var+1

        except:
            VoicerNamedllLocation = r"AshipoohcallChio\VoicerName.dll"
            with open(VoicerNamedllLocation,'r') as Voicer_Name_from_dll:
                Voicer_Name_location = Voicer_Name_from_dll.readline()
            print("dll -",Voicer_Name_location)
            audio_var = audio_var+5


            SentencedllLocation = r"AshipoohcallChio\Sentence.dll"
            with open(SentencedllLocation,'r') as Sentence_from_dll:
                Sentence_location = Sentence_from_dll.readline()
            print("dll -",Sentence_location)
            audio_var = audio_var+5



            SpeedRatedllLocation = r"AshipoohcallChio\SpeedRate.dll"
            with open(SpeedRatedllLocation,'r') as Speed_Rate_dll:
                Speed_Rate_Location = Speed_Rate_dll.readline()
            print("dll -",Speed_Rate_Location)
            audio_var = audio_var+5

            Error = traceback.format_exc()









    except:
        Error = traceback.format_exc()
        print(Error)

        if "footageLocation.dll" in Error:
            messagebox.showinfo('Error', "Please Select a Video")

        if "SenteseByText.dll" in Error:
            messagebox.showinfo('Error', "Plese Enter a Sentence and click on Append Button")

        if "VoicerName.dll" in Error:
            messagebox.showinfo('Error', "To use Free TTS Service, You have to select the Speaker from the Dropdown menu")

        if "Sentence.dll" in Error:
            messagebox.showinfo('Error', "Please Save the currunt Settings to Render the video")




    if essen_var == 9 and (audio_var == 1 or audio_var == 15): #Checks audio is made by microsoft speakers or audio given as a mp3 file. audio_var means audio variables. And if auduo_var ==1 it means user likes to make the voice by microsoft speakers and is audio_var ==2 it means user has given a mp3 file already.
        for widgets in ws.winfo_children():
            widgets.destroy()


        def output_location():
            folder = filedialog.askdirectory()
            locationVariable3 = tk.StringVar(value=folder)
            tk.Entry(ws,width = 30,textvariable=locationVariable3, font=('Verdana',15)).place(x=20, y=200)

            output_location_tmp = (f'''{folder}/{time.strftime("%d_%m_%Y %H-%M", time.localtime())}.mp4''')
            print(f'''{folder}/{time.strftime("%d_%m_%Y %H-%M", time.localtime())}''')

            def StartRender():

                Label(ws, text='Video is Rendering...', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',30, 'bold')).place(x=20, y=350)
                Label(ws, text='Do not interupt to the process', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=20, y=410)
                Label(ws, text='(Log will appear after completing the process)', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',10, 'bold')).place(x=20, y=448)

                Label(ws, text="# Claro is using the world's Fastst video rendering engine", fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',12, 'bold')).place(x=60, y=500)
                Label(ws, text="# It's supports over 100+ video formats", fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',12, 'bold')).place(x=60, y=530)



                if audio_var == 1:
                    silence_duration = float(Silance_Duration_Location)
                    footage_location = footage_location_dll
                    voice_location = Audio_Location
                    pure_silane_location = pure_silante_file_location
                    output_location = output_location_tmp
                    FootageText = Sentence_by_text_Location
                    TextFont = font_location
                    TextColor = Text_Color_location
                    TextFontSize = int(font_Sized_location)
                    TextXPos,TextYPos = float(Text_X_pos_location),float(Text_Y_pos_location)
                    ExtraSec = int(Extra_Seconds_location)







                    #Moviepy code will be here

                    #Assign audio,video,silence file to variables
                    footage = VideoFileClip(footage_location,audio=False)
                    pure_silane = AudioFileClip(pure_silane_location)
                    voice = AudioFileClip(voice_location)

                    #Create a silance(mute)
                    Slience_middle_of_voices = pure_silane.subclip(0,voice.duration*silence_duration)

                    #Creating Final Audio timeline and set is as the audio of the footage
                    final_audio = concatenate_audioclips([voice,Slience_middle_of_voices,voice,Slience_middle_of_voices,voice])
                    footage_duration = final_audio.duration



                    w,h = moviesize = footage.size



                    footage_append = []

                    if final_audio.duration > footage.duration:
                        while True:
                            footage_append.append(footage)
                            print(len(footage_append))

                            footage_repeatation = concatenate_videoclips(footage_append)

                            if footage_repeatation.duration > final_audio.duration:
                                print("yes")

                                final_footage_with_final_audio = footage_repeatation.set_audio(final_audio)

                                break



                    elif final_audio.duration <= footage.duration:
                        subcliped_footage = footage.subclip(0,final_audio.duration+2)
                        final_footage_with_final_audio = subcliped_footage.set_audio(final_audio)







                    my_text = TextClip(FootageText, font=TextFont, color= TextColor, fontsize=TextFontSize)
                    text_background = my_text.on_color(size=(footage.w + my_text.w, my_text.h+5), color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
                    txt_mov = text_background.set_pos( lambda t: (max(w/30, int(w-0.5*w*TextXPos)), max(TextYPos*h/6,int(100))) )

                    final_video = CompositeVideoClip([final_footage_with_final_audio,txt_mov])

                    final_video.subclip(0,final_audio.duration+ExtraSec).write_videofile(output_location)
                    #final_video.save_frame("frame.png")
                    #end by here


                    Label(ws, text='Video Renderd Successfully', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',30, 'bold')).place(x=20, y=350)
                    Label(ws, text='Please check on the output folder', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=20, y=410)


                    with open(apache_log_file,'r') as apachelog:
                        apache_log_print = apachelog.readlines()


                    TextBox = ScrolledText(ws, height='10', width='45', wrap=WORD)


                    for i in apache_log_print:

                        TextBox.insert(END, "The count is: " +str(i)+"\n")
                        TextBox.yview(END)


                    TextBox.place(x=100,y=650)





                elif audio_var == 15:
                    engine = pyttsx3.init()
                    voices = engine.getProperty('voices')

                    speed_rate = Speed_Rate_Location
                    Text_To_Speak = Sentence_location

                    Path_to_save_the_voice  = temp_voice
                    male_voices = (0)
                    female_voices = (1,2)

                    engine = pyttsx3.init()
                    voices = engine.getProperty('voices')

                    speed_rate = float(Speed_Rate_Location)
                    Text_To_Speak = Sentence_location

                    Path_to_save_the_voice  = temp_voice
                    male_voices = (0)
                    female_voices = (1,2)

                    if "Hazel" in Voicer_Name_location:
                        engine.setProperty('voice', voices[1].id)
                        engine. setProperty("rate", speed_rate)
                        engine.save_to_file(Text_To_Speak, Path_to_save_the_voice)
                        engine.runAndWait()

                    elif "Zira" in Voicer_Name_location:
                        engine.setProperty('voice', voices[2].id)
                        engine. setProperty("rate", speed_rate)
                        engine.save_to_file(Text_To_Speak, Path_to_save_the_voice)
                        engine.runAndWait()


                    elif "David" in Voicer_Name_location:
                        engine.setProperty('voice', voices[0].id)
                        engine. setProperty("rate", speed_rate)
                        engine.save_to_file(Text_To_Speak, Path_to_save_the_voice)
                        engine.runAndWait()


                    silence_duration = float(Silance_Duration_Location)
                    footage_location = footage_location_dll
                    voice_location = Path_to_save_the_voice
                    pure_silane_location = pure_silante_file_location
                    output_location = output_location_tmp
                    FootageText = Sentence_by_text_Location
                    TextFont = font_location
                    TextColor = Text_Color_location
                    TextFontSize = int(font_Sized_location)
                    TextXPos,TextYPos = float(Text_X_pos_location),float(Text_Y_pos_location)
                    ExtraSec = int(Extra_Seconds_location)




                    #Moviepy code will be here

                    #Assign audio,video,silence file to variables
                    footage = VideoFileClip(footage_location,audio=False)
                    pure_silane = AudioFileClip(pure_silane_location)
                    voice = AudioFileClip(voice_location)

                    #Create a silance(mute)
                    Slience_middle_of_voices = pure_silane.subclip(0,voice.duration*silence_duration)

                    #Creating Final Audio timeline and set is as the audio of the footage
                    final_audio = concatenate_audioclips([voice,Slience_middle_of_voices,voice,Slience_middle_of_voices,voice])
                    footage_duration = final_audio.duration



                    w,h = moviesize = footage.size



                    footage_append = []

                    if final_audio.duration > footage.duration:
                        while True:
                            footage_append.append(footage)
                            print(len(footage_append))

                            footage_repeatation = concatenate_videoclips(footage_append)

                            if footage_repeatation.duration > final_audio.duration:
                                print("yes")

                                final_footage_with_final_audio = footage_repeatation.set_audio(final_audio)

                                break



                    elif final_audio.duration <= footage.duration:
                        subcliped_footage = footage.subclip(0,final_audio.duration+2)
                        final_footage_with_final_audio = subcliped_footage.set_audio(final_audio)







                    my_text = TextClip(FootageText, font=TextFont, color= TextColor, fontsize=TextFontSize)
                    text_background = my_text.on_color(size=(footage.w + my_text.w, my_text.h+5), color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
                    txt_mov = text_background.set_pos( lambda t: (max(w/30, int(w-0.5*w*TextXPos)), max(TextYPos*h/6,int(100))) )

                    final_video = CompositeVideoClip([final_footage_with_final_audio,txt_mov])

                    final_video.subclip(0,final_audio.duration+ExtraSec).write_videofile(output_location)
                    #final_video.save_frame("frame.png")
                    #end by here




                    Label(ws, text='Video Renderd Successfully', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',30, 'bold')).place(x=20, y=350)
                    Label(ws, text='Please check on the output folder', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=20, y=410)

                    with open(apache_log_file,'r') as apachelog:
                        apache_log_print = apachelog.readlines()


                    TextBox = ScrolledText(ws, height='10', width='45', wrap=WORD)


                    for i in apache_log_print:

                        TextBox.insert(END, "The count is: " +str(i)+"\n")
                        TextBox.yview(END)


                    TextBox.place(x=100,y=650)








            Button(ws, fg = "#FFFFFF", height=1, width= 36, text='START', bg='#149FCF',font=(r'Fonts\Poppins-Italic.ttf', 16, 'bold'), command=lambda: StartRender()).place(x=20, y=250)



        Label(ws, text='Location to the Output', fg="#ffffff",bg='#474747', font=(r'Fonts\PTSans-Bold.ttf',15, 'bold')).place(x=20, y=150)
        location_of_output = Text(ws, height=2, width=52) ; location_of_output.place(x=20, y=200)
        Button(ws,fg = "#ffffff", height= 1, width= 6, text='   Browse   ', bg='red', font=(r'Fonts\Poppins-Italic.ttf', 14, 'bold'), command=output_location).place(x=450, y=200)




Button(ws, fg = "#FFFFFF", height=1, width= 35, text='RENDER', bg='#149FCF',font=(r'Fonts\Poppins-Italic.ttf', 16, 'bold'), command=lambda: Render()).place(x=70, y=876)







ws.mainloop()