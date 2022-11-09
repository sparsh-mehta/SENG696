import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

from Agents.AgentComm import AgentCommunication
import Converter
from ImageProcessing import image_classification_model

class IPAgentClass(Agent):
    class IPAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("IPAgent Start")

        async def run(self):
            msg = await self.receive(timeout=5) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                ReceivedMessage = ReceivedMessage.split(":")
                msg = Message(to=AgentCommunication.IAAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
                try:
                    Converter.decode_str_to_file(ReceivedMessage[1], "ImageProcessing/decodedImage.jpeg")
                    ReturnAccuracy, Returnclass, ReturnError = image_classification_model.processImage('ImageProcessing/decodedImage.jpeg')
                except:
                    print("{IPAgentClass}: FileDecodeError")
                    ReturnError = AgentCommunication.FileDecodeError
                    Returnclass = ""
                    ReturnAccuracy = ""
                
                #print("IPAgent Message Recieved")
                #print(ReceivedMessage)
                               
                # Send response to Agent1 agent
                msg.body = AgentCommunication.IPAgentID + \
                        AgentCommunication.IAAgentID + \
                        ReturnError + ":" + \
                        Returnclass + ":" + ReturnAccuracy
                print("{IPAgentClass} Request- " + msg.body)

                #print("Agent2Class:Agent2Behaviour:run:msg:response:{CovidReport.pdf Sent}")
                await self.send(msg)

                
            # else:
                # No Messages to be sent
            #await asyncio.sleep(2)

    async def setup(self):
        print("IPAgent Setup")
        b = self.IPAgentBehaviour()
        self.add_behaviour(b)

def startIPAgent():
    IPAgentObj = IPAgentClass(AgentCommunication.IPAgentUserID, AgentCommunication.IPAgentPassword)
    IPAgentObj.start().result()