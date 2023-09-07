from tkinter import*
import json
from tkinter import messagebox
import pyttsx3



def main():

    from difflib import get_close_matches
    audio=pyttsx3.init()


    def wordaudio():
        voices=audio.getProperty('voices')
        audio.setProperty('voice', voices[0].id)
        audio.say(Entryword.get())
        audio.runAndWait()


    def  meaningaudio():
       voices=audio.getProperty('voices')
       audio.setProperty('voice', voices[0].id)
       audio.say(textarea.get(1.0,END))
       audio.runAndWait()


    def exit():
        res=messagebox.askyesno( 'Do you want to exit?')
        if res==True:
            root.destroy()#to close windowhello

        else:
            pass


    def clear():
        textarea.config(state=NORMAL)
        Entryword.delete(0, END)
        textarea.delete(1.0, END)
        textarea.config(state=DISABLED)


    def search():
        data=json.load(open('data.json'))
        word=Entryword.get()

        word=word.lower()

        if word in data:
            meaning=data[word]


            textarea.config(state=NORMAL)
            textarea.delete(1.0,END)
            for item in meaning:
                textarea.insert(END,u"\u2022"+item+'\n\n')
            textarea.config(state=DISABLED)



        elif len(get_close_matches(word,data.keys()))>0:

            close_match=get_close_matches(word,data.keys())[0]

            respond=messagebox.askyesno('Confirm',f'Did you mean {close_match} instead?')

            if respond==True:
                Entryword.delete(0,END)
                Entryword.insert(END,close_match)

                meaning=data[close_match]
                textarea.delete(1.0,END)
                textarea.config(state=NORMAL)
                for item in meaning:
                    textarea.insert(END,u'\u2022'+ item +'\n\n')

                textarea.config(state=DISABLED)

            else:
                textarea.delete(1.0,END)
                messagebox.showinfo('Information',"The word you enter doesnt exist")
                Entryword.delete(0,END)

        else:
            messagebox.showerror('Error','The word does not exist.Please enter correct word.')
            Entryword.delete(0
                             ,END)
            textarea.delete(1.0, END)



    root=Tk()
    root.geometry("1000x626+100+30")
    root.title("Audio dictionary")
    root.resizable(0,0)
    bgimage=PhotoImage(file="newsd.png")
    bgLabel=Label(root,image=bgimage)
    bgLabel.place(x=0,y=0)



    M=Label(root,text="ENTER WORD",font=("Britannic Bold",30,"bold",),bg="grey54",fg="white")

    M.place(x=200,y=100)

    Entryword=Entry(root,font=("Yu Gothic UI Semibold",16,"bold"),bg="grey75",justify=CENTER,bd=13,relief=GROOVE,width=19,)
    Entryword.place(x=200,y=170)

    searchimage=PhotoImage(file="icons8-search-more-24.png")
    searchButton=Button(root,image=searchimage,bd=7,bg="gray86",cursor="hand2",width=44,height=40,activebackground="gray86",relief="groove",command=search)
    searchButton.place(x=240,y=260)

    micimage=PhotoImage(file="icons8-microphone-24 (1).png")
    micButton=Button(root,image=micimage,bd=7,bg="gray86",cursor="hand2",width=44,height=40,activebackground="gray86",command=wordaudio,relief="groove")
    micButton.place(x=340,y=260)


    M=Label(root,text="MEANING",font=("Britannic Bold",30,"bold",),bg="gray54",fg="white")

    M.place(x=580,y=50)

    textarea=Text(root,width=32,height=10,font=("arial Black",11,"bold"),bd=13,bg="grey67",relief="groove")
    textarea.place(x=580,y=120)


    audioimage=PhotoImage(file="icons8-microphone-24 (1).png")
    audioButton=Button(root,image=audioimage,bd=7,bg="gray86",cursor="hand2",width=46,height=36,activebackground="gray86",command=meaningaudio,relief="groove")
    audioButton.place(x=600,y=380)

    clearimage=PhotoImage(file="icons8-clear-symbol-30.png")
    clearButton=Button(root,image=clearimage,bd=7,bg="gray86",cursor="hand2",width=44,height=36,activebackground="gray86",command=clear,relief="groove")
    clearButton.place(x=700,y=380)

    exitimage=PhotoImage(file="icons8-exit-sign-50 (1).png")
    exitButton=Button(root,image=exitimage,bd=7,bg="gray86",cursor="hand2",width=44,height=36,activebackground="gray86",command=exit,relief="groove")
    exitButton.place(x=790,y=380)

    def enter_function(event):
        searchButton.invoke()







    root.bind("<Return>",enter_function)

    root.mainloop()

