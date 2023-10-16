import datetime
from time import strftime
import customtkinter 
import pyttsx3
import os


#Used to run the Text to speech
engine = pyttsx3.init()



customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

#Root info
root = customtkinter.CTk()
root.title("Projects")
root.iconbitmap('Pictures/title.ico')
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

#Option frame is the from on the left
OptionsFrame = customtkinter.CTkFrame(root)
OptionsFrame.pack(side = customtkinter.LEFT)
OptionsFrame.pack_propagate(False)
OptionsFrame.configure(width=250, height=height)

#Main frame is the middle frame
MainFrame = customtkinter.CTkFrame(root, border_width=2, border_color= 'white')
MainFrame.pack(side = customtkinter.LEFT)
MainFrame.pack_propagate(False)
MainFrame.configure(width = 700, height=height)

#Text box on the right
T= customtkinter.CTkTextbox(root, width=350, height=height)
T.configure(state="disabled") 
T.pack(pady=12, padx=10, side = customtkinter.RIGHT)


def time():
    string = strftime('%H:%M:%S %p')
    clock.configure(text=string)
    clock.after(1000,time)

#Outputs text depending on Time of day
def FindToD():
    currentTime = datetime.datetime.now().hour
    if 12 > currentTime >= 0:
        ToD = "Good Morning"
    elif 19 > currentTime >= 12:
        ToD = "Good Afternoon"
    elif currentTime >= 19:
        ToD = "Good Evening"
    return ToD       

#Takes in a function and inputs it into the text box
def PrintButton(ButtonPress):
        T.configure(state="normal") 
        T.insert(customtkinter.END ,ButtonPress + "\n")
        T.configure(state="disabled")

def DeletePage(): 
    for frame in MainFrame.winfo_children():
        frame.destroy()

def DeleteText():
    T.configure(state="normal") 
    T.delete(1.0, customtkinter.END)
    T.configure(state="disabled")

#Opens a new page and deletes the old one by calling DeletePage function
def indicate(page):
    DeletePage()
    page()

#These are the different frames that can be accesed from the option frame via buttton
def WeatherPage():
    import weather
    WeatherFrame = customtkinter.CTkFrame(MainFrame) 

    title = customtkinter.CTkLabel(master=WeatherFrame, text= "Weather system")
    title.pack(pady=12, padx=10)

    prompt = customtkinter.CTkLabel(master=WeatherFrame, text= "Enter a city")
    prompt.pack(pady=12, padx=10)

    LFCity = customtkinter.StringVar()
    Enter_City = customtkinter.CTkEntry(master=WeatherFrame, width=250, textvariable= LFCity)
    Enter_City.pack(pady=12, padx=10)

    TempBtn = customtkinter.CTkButton(master=WeatherFrame, text="Temperature", command=lambda : PrintButton(weather.temp(weather.generate_response(weather.Make_Url(weather.Get_City(LFCity.get()))),weather.Get_City(LFCity.get()))))
    TempBtn.pack(pady=12, padx=10)

    FlBtn = customtkinter.CTkButton(master=WeatherFrame, text="Feels Like", command=lambda: PrintButton(weather.FL(weather.generate_response(weather.Make_Url(weather.Get_City(LFCity.get()))),weather.Get_City(LFCity.get()))))
    FlBtn.pack(pady=12, padx=10)

    HumidityBtn = customtkinter.CTkButton(master=WeatherFrame, text="Humidity", command=lambda : PrintButton(weather.Humidity(weather.generate_response(weather.Make_Url(weather.Get_City(LFCity.get()))),weather.Get_City(LFCity.get()))))
    HumidityBtn.pack(pady=12, padx=10)

    WSBtn = customtkinter.CTkButton(master=WeatherFrame, text="Wind Speed", command=lambda : PrintButton(weather.WindSpeed(weather.generate_response(weather.Make_Url(weather.Get_City(LFCity.get()))),weather.Get_City(LFCity.get()))))
    WSBtn.pack(pady=12, padx=10)

    SCBtn = customtkinter.CTkButton(master=WeatherFrame, text="Sky Condition", command=lambda : PrintButton(weather.Desc(weather.generate_response(weather.Make_Url(weather.Get_City(LFCity.get()))),weather.Get_City(LFCity.get()))))
    SCBtn.pack(pady=12, padx=10)

    SRBtn = customtkinter.CTkButton(master=WeatherFrame, text="Sun Rise", command=lambda : PrintButton(weather.sunrise(weather.generate_response(weather.Make_Url(weather.Get_City(LFCity.get()))),weather.Get_City(LFCity.get()))))
    SRBtn.pack(pady=12, padx=10)

    SSBtn = customtkinter.CTkButton(master=WeatherFrame, text="Sun Set", command=lambda : PrintButton(weather.sunset(weather.generate_response(weather.Make_Url(weather.Get_City(LFCity.get()))),weather.Get_City(LFCity.get()))))
    SSBtn.pack(pady=12, padx=10)


    WeatherFrame.pack(pady=20, padx=60, fill="both", expand=True)

def DictPage():
    import Dictionary
    DictFrame = customtkinter.CTkFrame(MainFrame)
    label = customtkinter.CTkLabel(master=DictFrame, text= "Dictionary")
    label.pack(pady=12, padx=10)

    # Label for the word entry field
    label_word = customtkinter.CTkLabel(master=DictFrame, text="Enter a word:")
    label_word.pack(pady=12, padx=10)

    # Entry field for the word
    LFWord = customtkinter.StringVar()
    entry_word = customtkinter.CTkEntry(master=DictFrame, width=250, textvariable=LFWord)
    entry_word.pack(pady=12, padx=10)

    SearchBtn = customtkinter.CTkButton(master=DictFrame, text= "Search word", command= lambda : PrintButton(Dictionary.search_definition(LFWord.get())))
    SearchBtn.pack(pady=12, padx =10)

    DictFrame.pack(pady=20, padx=60, fill="both", expand=True)

def GamesPage():
    GamesFrame = customtkinter.CTkFrame(MainFrame)
    
    game = "Air_Hockey.exe"
   
    deleteBtn = customtkinter.CTkButton(GamesFrame, text="Air Hockey", command= lambda :  os.startfile(game))
    deleteBtn.pack(pady=12, padx=10)

    GamesFrame.pack(pady = 20)

def TTSPage():
    TextToSpeech = customtkinter.CTkFrame(MainFrame)

    voicecbox = customtkinter.CTkComboBox(TextToSpeech, values=['Male','Female'])
    voicecbox.pack(pady=12, padx=10)

    speedcbox = customtkinter.CTkComboBox(TextToSpeech, values=['Fast','Normal','Slow'])
    speedcbox.set('Normal')
    speedcbox.pack(pady=12, padx=10)

    speakBtn = customtkinter.CTkButton(master=TextToSpeech, text="Speak", command= lambda : Speak())
    speakBtn.pack(pady=12, padx=10)
        
    def Speak():
            text = T.get(1.0, customtkinter.END)
            gender = voicecbox.get()
            speed = speedcbox.get()
            voices = engine.getProperty('voices')
            def setVoice():
                if (gender == 'Male'):
                    engine.setProperty('voice', voices[0].id)
                    engine.say(text)
                    engine.runAndWait()
                else:
                    engine.setProperty('voice', voices[1].id)
                    engine.say(text)
                    engine.runAndWait()
            if (speed == 'Fast'):
                engine.setProperty('rate',250)
                setVoice()
            elif (speed == 'Normal'):
                engine.setProperty('rate',150)
                setVoice()
            else:
                engine.setProperty('rate',60)
                setVoice()             

    TextToSpeech.pack(pady = 20)


clock = customtkinter.CTkLabel(master=OptionsFrame)
clock.pack(pady=12, padx=10)
time()
FindToD()

Greeting = customtkinter.CTkLabel(master=OptionsFrame,text=FindToD())
Greeting.pack(pady=12, padx=1)

HomeBtn = customtkinter.CTkButton(OptionsFrame, text= "Weather",hover_color= "green", command= lambda: indicate(WeatherPage))
HomeBtn.pack(pady=12, padx =10)

MenuBtn = customtkinter.CTkButton(OptionsFrame, text= "Dictionary",hover_color= "green", command= lambda: indicate(DictPage))
MenuBtn.pack(pady=12, padx =10)

AboutBtn = customtkinter.CTkButton(OptionsFrame, text= "Games",hover_color= "green", command= lambda: indicate(GamesPage))
AboutBtn.pack(pady=12, padx =10)

TTSBtn = customtkinter.CTkButton(OptionsFrame, text= "Text to Speech",hover_color= "green", command= lambda: indicate(TTSPage))
TTSBtn.pack(pady=12, padx =10)

# Every option Button is before this one
deleteBtn = customtkinter.CTkButton(OptionsFrame, text="Clear Text Area", command= lambda : DeleteText(), fg_color="red", hover_color="#700f0f")
deleteBtn.pack(pady=12, padx=10)

root.mainloop()