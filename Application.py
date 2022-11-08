import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


from Agents.IAAgent import startIAAgent
from Agents.IPAgent import startIPAgent
from Agents.FVAgent import startFVAgent
from Agents.DBAgent import startDBAgent
from Agents.AgentComm import request, AgentCommunication

from GUI.MainPage import MainPage
from GUI.ImageProcessingPage import ImageProcessingPage

Curr_Frame = 0

def startAgents():
    startIPAgent()
    # startFVAgent()
    # startDBAgent()
    startIAAgent()


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "BTC")

        self.geometry("1000x600")
        self.resizable(False, False)
        self.title("Agent Communication Application")
        self.configure(bg="#bcb8b8")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (MainPage.MainPage, ImageProcessingPage.ImageProcessingPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        Curr_Frame = MainPage.MainPage
        #Curr_Frame = ImageProcessingPage.ImageProcessingPage

        self.show_frame(Curr_Frame)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



if __name__ == '__main__':
    startAgents()
    app = Application()
    app.mainloop()

