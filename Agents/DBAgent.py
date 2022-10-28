from spade import agent, quit_spade
import time
import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

from Agents.AgentComm import AgentCommunication


class DBAgentClass(Agent):
    class DBAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("DBAgent Start")

        async def run(self):
            #print("Agent2Class:Agent2Behaviour:run")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                print("DBAgent Message Recieved")
                #print(ReceivedMessage)
                
                msg = Message(to=AgentCommunication.IAAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                # Send response to Agent1 agent
                msg.body = "DBAgent -> IAAgent Message Sent"
                print(msg.body)

                #print("Agent2Class:Agent2Behaviour:run:msg:response:{CovidReport.pdf Sent}")
                await self.send(msg)


    async def setup(self):
        print("DBAgent Setup")
        b = self.DBAgentBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

def startDBAgent():
    DBAgentObj = DBAgentClass(AgentCommunication.DBAgentUserID, AgentCommunication.DBAgentPassword)
    DBAgentObj.start().result()