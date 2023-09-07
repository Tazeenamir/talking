from tkinter import*
import pyttsx3
audio=pyttsx3.init()

def main():
    w.destroy()
    import main
    main.main()

w=Tk()
w.geometry("750x500")
w.title("welcome ")
w.resizable(0,0)
bgimage=PhotoImage(file="brt.png")
bgLabel=Label(w,image=bgimage)
bgLabel.place(x=0,y=0)
M=Label(w,text="WELCOME TO AUDIO DICTIONARY",font=("Britannic Bold",35,"bold",),bg="grey86",fg="grey54")
M.place(x=13,y=80)

image=PhotoImage(file="next2.png")
NextButton=Button(w,image=image,bd=7,bg="gray86",cursor="hand2",width=125,height=45,activebackground="gray86",relief="groove",command=main)
NextButton.place(x=300,y=150)
def wordaudio():
    voices=audio.getProperty('voices')
    audio.setProperty('voice', voices[1].id)
    audio.say(("welcome to audio dictionary    "))
    audio.say(("click on next to find the meanings "))
    audio.runAndWait()

micimage=PhotoImage(file="icons8-microphone-24 (1).png")
micButton=Button(w,image=micimage,bd=7,bg="gray86",cursor="hand2",width=44,height=40,activebackground="gray86",command=wordaudio)
micButton.place(x=500,y=500)
def enter_function(event):
    micButton.invoke()





w.bind("<Return>",enter_function)



w.mainloop()