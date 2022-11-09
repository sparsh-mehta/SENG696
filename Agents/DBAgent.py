from spade import agent, quit_spade
import time
import asyncio
import os
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template

from Agents.AgentComm import AgentCommunication
from DATABASE_CODE import database
import Converter


class DBAgentClass(Agent):
    class DBAgentBehaviour(CyclicBehaviour):
        async def on_start(self):
            print("DBAgent Start")

        async def run(self):
            #print("Agent2Class:Agent2Behaviour:run")

            msg = await self.receive(timeout=5) # wait for a message for 10 seconds
            if msg:
                ReceivedMessage = msg.body
                print("{DBAgentClass} Request- " + ReceivedMessage)
                ReceivedMessage = ReceivedMessage.split(":")[1:]
                # print("DBAgent Message Recieved")
                
                msg = Message(to=AgentCommunication.IAAgentUserID)  # Instantiate the message
                msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
                data = ''
                #Case 1 - Generate report request
                if ReceivedMessage[0] == '0' and ReceivedMessage[1] == '0' and ReceivedMessage[2] == '0':
                    # path exists or not
                    if os.path.exists('database.csv'):
                        print("DataBase Found")                    
                        try:
                            data = Converter.encode_file_to_str('database.csv')
                            error = '0'
                        except:
                            error = AgentCommunication.FileEncodeError

                    else:
                        #Path not exist
                        print("DataBase Not Found")
                        error = AgentCommunication.DatabaseNotFound
                            
                # Case 2: Save Entry to Database
                else:
                    error = database(ReceivedMessage[0], ReceivedMessage[1], ReceivedMessage[2])

                # Send response to Agent1 agent
                msg.body = AgentCommunication.DBAgentID + AgentCommunication.IAAgentID + str(error) + ':' + data
                print("{DBAgentClass} Response- " + msg.body)

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