import tkinter as tk
from PIL import ImageTk, Image
import tkinter.filedialog

from GUI.MainPage import MainPage
from Application import Curr_Frame
from Agents.AgentComm import request, AgentCommunication
from Converter import encode_file_to_str

ImageProcessingPageFrame = tk.Frame

class ImageProcessingPage(ImageProcessingPageFrame):
    filename = ''
    #Button Callbacks Here
    def Button0_Callback(self, controller):
        print("{ImageProcessingPage} Button 0 Pressed")
        Curr_Frame = MainPage.MainPage
        controller.show_frame(Curr_Frame)

    def Button1_Callback(self, controller):
        print("{ImageProcessingPage} Button 1 Pressed")
        # f_types = [('Jpeg Files', '*.jpeg'), ('PNG Files','*.png')]

        try:
            ImageProcessingPage.filename = tkinter.filedialog.askopenfilename(multiple=True)[0]
            print(ImageProcessingPage.filename)
        except:
            print('File Not Selected')
            return

        try:
            returnError, returnData = request(SenderAgentID=AgentCommunication.IAAgentID,
                ReceiverAgentID=AgentCommunication.FVAgentID, 
                ErrorCode=AgentCommunication.Success,
                Data= ImageProcessingPage.filename.split('.')[-1])
        except:
            print('Communication Error')
            tkinter.messagebox.showerror(title="Error", message="No Response")
            return

        if returnError is AgentCommunication.Failure:
            print('Invalid File')
            tkinter.messagebox.showerror(title="Error", message="Invalid File")
            return 

        self.image1 = Image.open(ImageProcessingPage.filename).resize((300, 300))
        self.test = ImageTk.PhotoImage(self.image1)
        self.Label0.configure(image=self.test)
        self.Label0.image = self.test
        


    def Button2_Callback(self, controller):
        print("{ImageProcessingPage} Button 2 Pressed")
        # requesting IP Agent for class and accuracy
        try:
            self.image = Image.open(ImageProcessingPage.filename).resize((300, 300))
            self.image.save(ImageProcessingPage.filename)
        except:
            print('File Not Selected')
            tkinter.messagebox.showerror(title="Error", message="File Not Selected")
            return

        try:
            try:
                self.data = encode_file_to_str(ImageProcessingPage.filename)
            except:
                print("File Encoding Error")
                tkinter.messagebox.showerror(title="Error", message="File Encoding Error")
                return
            returnError, returnData = request(SenderAgentID=AgentCommunication.IAAgentID,
                    ReceiverAgentID=AgentCommunication.IPAgentID, 
                    ErrorCode=AgentCommunication.Success,
                    Data= self.data)
            #Handling IPAgent Errors
            if returnError is AgentCommunication.FileDecodeError:
                print("File Decoding Error")
                tkinter.messagebox.showerror(title="Error", message="File Decoding Error")
                return

        except:
            print('Communication Error')
            tkinter.messagebox.showerror(title="Error", message="No Response")
            return

        self.Label1.configure(text = returnData[0])
        self.Label2.configure(text = str(float(returnData[1])/100)+"%")
        # Sending data copy to Db Agent
        tempVar = ImageProcessingPage.filename.split('/')[-1]

        try:
            returnError, returnData = request(SenderAgentID=AgentCommunication.IAAgentID,
                    ReceiverAgentID=AgentCommunication.DBAgentID, 
                    ErrorCode=AgentCommunication.Success,
                    Data= tempVar + ':' + returnData[0] + ':' + returnData[1])
        except:
            print('Communication Error')
            tkinter.messagebox.showerror(title="Error", message="No Response")
            return


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
        self.Canvas0Image = tk.PhotoImage(file = f"GUI/ImageProcessingPage/background.png")
        self.Canvas0.create_image(506.5, 300.0,image=self.Canvas0Image)     

        # Create Label (Image)
        self.Label0 = tk.Label(self)
        self.Label0.configure(bg="#FFFFFF")
        self.Label0.place(x=540, y=140)

        # Create Label (Class)
        self.Label1 = tk.Label(self)
        self.Label1.configure(bg="#D9D9D9")
        self.Label1.configure(font=("Inter", 16, 'bold'))
        self.Label1.place(x=190, y=408)

        # Create Label (Accuracy)
        self.Label2 = tk.Label(self)
        self.Label2.configure(bg="#D9D9D9")
        self.Label2.configure(font=("Inter", 16, 'bold'))
        self.Label2.place(x=190, y=478)

        #Create Button 0 (Back)
        self.Button0 = tk.Button(self)
        self.Button0Image = tk.PhotoImage(file = f"GUI/ImageProcessingPage/img0.png")
        self.Button0.configure(image=self.Button0Image)
        self.Button0.configure(borderwidth=0)
        self.Button0.configure(highlightthickness=0)
        self.Button0.configure(command=lambda:ImageProcessingPage.Button0_Callback(self, controller))
        self.Button0.configure(relief="flat")
        self.Button0.place(x = 13, y = 16, height=45, width=94)

        #Create Button 1 (Upload File)
        self.Button1 = tk.Button(self)
        self.Button1Image = tk.PhotoImage(file = f"GUI/ImageProcessingPage/img1.png")
        self.Button1.configure(image=self.Button1Image)
        self.Button1.configure(borderwidth=0)
        self.Button1.configure(highlightthickness=0)
        self.Button1.configure(command=lambda:ImageProcessingPage.Button1_Callback(self, controller))
        self.Button1.configure(relief="flat")
        self.Button1.place(x = 130, y = 154, height=59, width=143)

        #Create Button 2 (Process)
        self.Button2 = tk.Button(self)
        self.Button2Image = tk.PhotoImage(file = f"GUI/ImageProcessingPage/img2.png")
        self.Button2.configure(image=self.Button2Image)
        self.Button2.configure(borderwidth=0)
        self.Button2.configure(highlightthickness=0)
        self.Button2.configure(command=lambda:ImageProcessingPage.Button2_Callback(self, controller))
        self.Button2.configure(relief="flat")
        self.Button2.place(x = 136, y = 236, height=59, width=137)
