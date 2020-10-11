from tkinter import *
from tkinter.tix import *
import requests

def search():
    search_word=user_input.get().lower()
    user_input.delete(0,'end')
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+search_word
    meaning=requests.get(url).json()
    if(type(meaning)==list):
        defs=[]
        output.config(text='\n'+meaning[0]['word'].upper(),font=('Courier',14),pady=2)
        for i in meaning:
            for j in i['meanings']:
                d = j['partOfSpeech'].capitalize()
                for k in j['definitions']:
                    d+='\n'+k['definition']
                defs.append(d)
        txt = ''
        for i in defs:
            txt+=i+'\n\n'
        output_pos.config(font=('Courier',11),text=txt,pady=4)
        
    else:
        txt="Sorry, couldn't find the definition for "+search_word+"!\nCheck the spelling and try again."
        output.config(text=txt,font=('Courier',12),pady=5)
        output_pos.config(text='')


root=Tk()
# root.geometry("450x500")
root.wm_title('Dictionary')
frame = Frame(width="500",height="400")
frame.pack()
title=Label(frame,text="Dictionary",font=('Courier',16))
title.pack(pady=10)
user_input_text=Label(frame,text="Enter a word:")
user_input_text.pack()
user_input=Entry(frame)
user_input.pack()
user_input.bind('<Return>',(lambda event: search()))
search_btn=Button(frame,text="Search",bg="lightgrey",command=search)
search_btn.pack(pady=5)
swin = ScrolledWindow(frame, width=500, height=350)
swin.pack()
win = swin.window
output=Label(win, wraplength=450)
output.pack()
output_pos=Label(win, wraplength=450)
output_pos.pack()
root.mainloop()