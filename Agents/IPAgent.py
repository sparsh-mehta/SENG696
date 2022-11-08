import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

from Agents.AgentComm import AgentCommunication
import Converter

class IPAgentClass(Agent):
    class IPAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("IPAgent Start")

        async def run(self):
            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                ReceivedMessage = ReceivedMessage.split(":")
                Converter.decode_str_to_file(ReceivedMessage[1], "decodedImage.jpeg")
                
                #TODO call ProcessImage Function here
                #accuracy, cls, error = ImageProcess()
                ReturnAccuracy = "95785"
                Returnclass = "cat"
                ReturnError = "0"
                
                #print("IPAgent Message Recieved")
                #print(ReceivedMessage)
                
                msg = Message(to=AgentCommunication.IAAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                # Send response to Agent1 agent
                msg.body = AgentCommunication.IPAgentID + \
                        AgentCommunication.IAAgentID + \
                        ReturnError + ":" + \
                        Returnclass + ":" + ReturnAccuracy
                print(msg.body)

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