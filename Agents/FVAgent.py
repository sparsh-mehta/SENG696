from spade import agent, quit_spade
import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

from Agents.AgentComm import AgentCommunication
from FileVerification.Test import FileVerification


class FVAgentClass(Agent):
    class FVAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("FVAgent Start")

        async def run(self):
            #print("Agent2Class:Agent2Behaviour:run")

            msg = await self.receive(timeout=5)     # wait for a message for 5 seconds
            if msg:
                ReceivedMessage = msg.body.split(":")
                print("{FVAgentClass} Request- " + msg.body)
                msg = Message(to=AgentCommunication.IAAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                #TODO call FileVerification Function here
                error = FileVerification(ReceivedMessage[1])
                data = ''
                msg.body = AgentCommunication.FVAgentID + AgentCommunication.IAAgentID + str(error) + ':' + data
                print("FVAgent Message Recieved")
                #print(ReceivedMessage)

                # Send response to Agent1 agent
                #msg.body = "FVAgent -> IAAgent Message Sent"
                print("{FVAgentClass} Response- " + msg.body)

                #print("Agent2Class:Agent2Behaviour:run:msg:response:{CovidReport.pdf Sent}")
                await self.send(msg)


    async def setup(self):
        print("FVAgent Setup")
        b = self.FVAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def startFVAgent():
    FVAgentObj = FVAgentClass(AgentCommunication.FVAgentUserID, AgentCommunication.FVAgentPassword)
    FVAgentObj.start().result()