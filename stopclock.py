import tkinter as tk

def start():
    global run
    if not run:
        update()
        run=True
def stop():
    global run
    if run:
        result.after_cancel(ut)
        run=False
def reset():
    global run
    result.after_cancel(ut)
    run=False
    global s,h,m
    s,m,h=0,0,0
    result.config(text="00:00:00")
def update():
    global s,h,m
    s+=1
    if s==60:
        m+=1
        s=0
    if m==60:
        h+=1
        m=0
    result.config(text=f"{h:02}:{m:02}:{s:02}")
    global ut
    ut=result.after(1000,update)

run=False    
t=0
s=m=h=0
root=tk.Tk()
root.title("Stopwatch")
root.geometry("500x200")
root.config(bg='light blue')
root.resizable(False,False)

i=tk.PhotoImage(file="stopclock.png")
root.iconphoto(False,i)

result=tk.Label(root,width=80,height=5,text='00:00:00',bd=5,bg='white',font=('ariel',35))
result.pack(padx=15,pady=(10,110))

button = tk.Button(root, text="Start",width=10,height=2,font=('ariel',12),bg="white",bd=3,command=lambda:start()).place(x=50,y=100)
button = tk.Button(root, text="Stop", width=10,height=2,font=('ariel',12),bg="white",bd=3,command=lambda:stop()).place(x=200,y=100)
button = tk.Button(root, text="Reset", width=10,height=2,font=('ariel',12),bg="white",bd=3,command=lambda:reset()).place(x=350,y=100)


root.mainloop()
