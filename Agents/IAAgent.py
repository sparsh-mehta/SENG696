import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

from Agents.AgentComm import AgentCommunication
import Converter

class IAAgentClass(Agent):
    class IAAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("IAAgent Start")

        async def run(self):
            await asyncio.sleep(5)
            if AgentCommunication.CommunicationFlag:
                # Instantiate the message
                if AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.DBAgentID:
                    msg = Message(to=AgentCommunication.DBAgentUserID)
                elif AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.FVAgentID:
                    msg = Message(to=AgentCommunication.FVAgentUserID)
                elif AgentCommunication.CommunicationTxBuffer[AgentCommunication.ReceiverAgentIDIndex] == AgentCommunication.IPAgentID:
                    msg = Message(to=AgentCommunication.IPAgentUserID)

                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")

                # Set the message content

                msg.body = AgentCommunication.CommunicationTxBuffer
                print("{IAAgentClass}-Request" + msg.body)
                #msg.body = Converter.encode_file_to_str("C:/Users/ispar/Desktop/PRS_Project696.xlsx")
                #print(msg.body)

                # Send Message
                await self.send(msg)
                
                # wait for a message for 5 seconds
                msg = await self.receive(timeout=5)

                if msg:
                    # Copy Received to Communication RX Buffer
                    AgentCommunication.CommunicationRxBuffer = msg.body
                    print("{IAAgentClass}-Response:" + AgentCommunication.CommunicationRxBuffer)
                    AgentCommunication.CommunicationError = False
                    AgentCommunication.CommunicationFlag = False

                else:
                    AgentCommunication.CommunicationFlag = False
                    AgentCommunication.CommunicationError = True
                    #print("Agent1Class:Agent1Behaviour:run:msg:response:\"No Response\"")
                    print("{IAAgentClass}-No Response")
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