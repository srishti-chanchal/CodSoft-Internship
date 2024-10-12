from tkinter import*

app= Tk()
app.tittle("to-do-list")
app.geometry("720x480")
app.resizeable(False,False)
app.config(bg="#242424")

#heading of the app
tittle= label(app,text="TO-DO-LIST",font=("consolas",18),bg="#242424",fg="#fff")
tittle.pack()

#entry for the app
text = StringVar()
task_entry=Entry(app,width=34,textvariable=text,font=("consolas",12))
task_entry.pack()

#buttons for the app
add= Button(app,text="Add", width=5,font=("consolas",12))
 add.place(x=250,y=110)          
            