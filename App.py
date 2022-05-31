from tkinter import *

def Valid():
  mdp=passwordEntry.get()
  email=emailEntry.get()
  window.destroy()
  app= Tk()
  
  app.mainloop()
window = Tk()

emailEntry=Entry(window)
emailEntry.pack()

passwordEntry=Entry(window)
passwordEntry.pack()

Save=Button(window, text="validé", command=Valid)

window.mainloop()
