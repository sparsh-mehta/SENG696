from spade import agent, quit_spade
import time
import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template



# ------------------------------Protocol Related Defines ##Don't Change##-----------------------------------
class AgentCommunication:

    CommunicationTxBuffer = ""
    CommunicationRxBuffer = ""
    CommunicationFlag = False
    CommunicationError = False

    Agent1UserID = "faker1@jabbim.com"
    Agent1Password = "Qwerty123"
    Agent2UserID = "faker@lightwitch.org"
    Agent2Password = "Qwerty123"
    #Agent3UserID = "professor16@jabbim.com"  # "professor16@jabbim.com"
    #Agent4UserID = "professor17@jabbim.com"

    # Command IDs


    # Agent IDs
    Agent1 = "1"
    Agent2 = "2"
    Agent3 = "3"
    Agent4 = "4"

    # Error Codes


    # Protocol Format


    # index reserved for :

# ------------------------------------------------------------------------------------------


class Agent1Class(Agent):
    class Agent1Behaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"Agent1Class.Agent1Behaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            #print("SenderAgent:Agent1Behaviour:run")
            await asyncio.sleep(5)
            if AgentCommunication.CommunicationFlag:
                msg = Message(to=AgentCommunication.Agent2UserID)  # Instantiate the message

                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")

                # Set the message content
                msg.body = "Agent1->Agent2 Message Sent"
                print(msg.body)

                # Send Message
                await self.send(msg)
                #print("Agent1Class:Agent1Behaviour:run:msg:request:\"{}\"".format(msg.body))

                # wait for a message for 5 seconds
                msg = await self.receive(timeout=5)

                if msg:
                    # Copy Received to Communication RX Buffer
                    AgentCommunication.CommunicationRxBuffer = msg.body
                    #print("Agent1Class:Agent1Behaviour:run:msg:response:\"{}\"".format(msg.body))
                    print("Agent1 Message Recieved")
                    AgentCommunication.CommunicationError = False
                    #AgentCommunication.CommunicationFlag = False

                else:
                    #AgentCommunication.CommunicationFlag = False
                    AgentCommunication.CommunicationError = True
                    #print("Agent1Class:Agent1Behaviour:run:msg:response:\"No Response\"")
                    print("Agent1 Message Recieved")
                
                print("----------------------------------------")

                
            # else:
                # No Messages to be sent
            #await asyncio.sleep(2)

    async def setup(self):
        print("Agent1Class:setup")
        b = self.Agent1Behaviour()
        self.add_behaviour(b)


class Agent2Class(Agent):
    class Agent2Behaviour(CyclicBehaviour):
        async def on_start(self):
            print("Class:{\"Agent2Class.Agent2Behaviour\"}, Method:{\"on_start\"}")

        async def run(self):
            #print("Agent2Class:Agent2Behaviour:run")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                print("Agent2 Message Recieved")
                #print(ReceivedMessage)
                
                msg = Message(to=AgentCommunication.Agent1UserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative

                # Send response to Agent1 agent
                msg.body = "Agent2->Agent1 Message Sent"
                print(msg.body)

                #print("Agent2Class:Agent2Behaviour:run:msg:response:{CovidReport.pdf Sent}")
                await self.send(msg)


    async def setup(self):
        print("Agent2Class:setup")
        b = self.Agent2Behaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

#Dummy Var
AgentCommunication.CommunicationFlag = True
Agent1 = Agent1Class(AgentCommunication.Agent1UserID, AgentCommunication.Agent1Password)
Agent1.start().result()
Agent2 = Agent2Class(AgentCommunication.Agent2UserID, AgentCommunication.Agent2Password)
Agent2.start().result()
while True:
    pass






# class DummyAgent(agent.Agent):
#     async def setup(self):
#         print("Hello World! I'm agent {}".format(str(self.jid)))
# dummy = DummyAgent("faker@lightwitch.org", "Qwerty123")
# future = dummy.start()
# future.result()
# dummy.stop()
# quit_spade()