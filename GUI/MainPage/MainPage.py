import tkinter as tk
import tkinter.simpledialog , tkinter.filedialog, tkinter.messagebox
from PIL import ImageTk, Image

from GUI.ImageProcessingPage import ImageProcessingPage
from Application import Curr_Frame
from Agents.AgentComm import request, AgentCommunication
import Converter


MainPageFrame = tk.Frame
class MainPage(MainPageFrame):
    #Button Callbacks Here
    def Button0_Callback(self, controller):
        print("{MainPage}:Button 0 Pressed")
        Curr_Frame = ImageProcessingPage.ImageProcessingPage
        controller.show_frame(Curr_Frame)

    def Button1_Callback(self, controller):
        print("{MainPage}:Button 1 Pressed")
        returnVar = tkinter.simpledialog.askstring('Password', 'Enter Password \t \t \t', show='*', parent=controller)
        print(returnVar)
        if returnVar == '98':
            try:      
                returnError, returnData = request(SenderAgentID=AgentCommunication.IAAgentID,
                    ReceiverAgentID=AgentCommunication.DBAgentID, 
                    ErrorCode=AgentCommunication.Success,
                    Data= '0:0:0')    # Data = 0:0:0 for case of report generation request
                #Handling DBAgent Errors
                if returnError is AgentCommunication.FileDecodeError:
                    print("File Decoding Error")
                    tkinter.messagebox.showerror(title="Error", message="File Decoding Error")
                    return
                elif returnError is AgentCommunication.DatabaseNotFound:
                    print("Database Not Found Error")
                    tkinter.messagebox.showerror(title="Error", message="Database Not Found Error")
                    return

            except:
                print('Communication Error')
                tkinter.messagebox.showerror(title="Error", message="No Response")
                return

            try:
                returnFilePath = tkinter.filedialog.askdirectory()
            except:
                print('Directory Not Selected')
                return
            
            returnFilePath = returnFilePath + '/downloadedFile.csv'
            try:
                Converter.decode_str_to_file(returnData[0], returnFilePath)
                tkinter.messagebox.showinfo(title="Success", message="File Downloaded")
            except:
                print("File Decoding Error")
                tkinter.messagebox.showerror(title="Error", message="File Decoding Error")
                return

        else:   #create pop up for wrong password
            tkinter.messagebox.showerror(title="Error", message="Wrong Password")




    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create Canvas
        self.Canvas0 = tk.Canvas(self)
        self.Canvas0.place(x = 0, y = 0)
        self.Canvas0.configure(bg="#bcb8b8")
        self.Canvas0.configure(height=600)
        self.Canvas0.configure(width=1000)
        self.Canvas0.configure(bd=0)
        self.Canvas0.configure(highlightthickness=0)
        self.Canvas0.configure(relief="ridge")
        self.Canvas0Image = tk.PhotoImage(file = f"GUI/MainPage/background.png")
        self.Canvas0.create_image(458.0, 176.0,image=self.Canvas0Image)

        #Create Button 0 (Process Image)
        self.Button0 = tk.Button(self)
        self.Button0Image = tk.PhotoImage(file = f"GUI/MainPage/img0.png")
        self.Button0.configure(image=self.Button0Image)
        self.Button0.configure(borderwidth=0)
        self.Button0.configure(highlightthickness=0)
        self.Button0.configure(command=lambda:MainPage.Button0_Callback(self, controller))
        self.Button0.configure(relief="flat")
        self.Button0.place(x = 157, y = 426, height=98, width=335)

        #Create Button 1 (Generate Report)
        self.Button1 = tk.Button(self)
        self.Button1Image = tk.PhotoImage(file = f"GUI/MainPage/img1.png")
        self.Button1.configure(image=self.Button1Image)
        self.Button1.configure(borderwidth=0)
        self.Button1.configure(highlightthickness=0)
        self.Button1.configure(command=lambda:MainPage.Button1_Callback(self, controller))
        self.Button1.configure(relief="flat")
        self.Button1.place(x=513, y=426, height=98, width=335)