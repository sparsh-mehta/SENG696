from spade import agent, quit_spade
import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

from Agents.AgentComm import AgentCommunication
import Convertor

class IAAgentClass(Agent):
    class IAAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("IAAgent Start")

        async def run(self):
            await asyncio.sleep(5)
            if AgentCommunication.CommunicationFlag:
                msg = Message(to=AgentCommunication.IPAgentUserID)  # Instantiate the message

                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")

                # Set the message content

                #msg.body = "IAAgent-> IPAgent Message Sent"
                msg.body = Convertor.encode_file_to_str("Documents/AgentModel.png")
                #print(msg.body)

                # Send Message
                await self.send(msg)
                
                # wait for a message for 5 seconds
                msg = await self.receive(timeout=5)

                if msg:
                    # Copy Received to Communication RX Buffer
                    AgentCommunication.CommunicationRxBuffer = msg.body
                    print("IAAgent Message Recieved")
                    AgentCommunication.CommunicationError = False

                else:
                    #AgentCommunication.CommunicationFlag = False
                    AgentCommunication.CommunicationError = True
                    #print("Agent1Class:Agent1Behaviour:run:msg:response:\"No Response\"")
                    print("No Response")
                print("----------------------------------------")


    async def setup(self):
        print("IAAgent Setup")
        b = self.IAAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def startIAAgent():
    IAAgentObj = IAAgentClass(AgentCommunication.IAAgentUserID, AgentCommunication.IAAgentPassword)
    IAAgentObj.start().result()