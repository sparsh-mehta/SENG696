from Agents.IAAgent import startIAAgent
from Agents.IPAgent import startIPAgent
from Agents.FVAgent import startFVAgent
from Agents.DBAgent import startDBAgent

def startAgents():
    startIPAgent()
    startFVAgent()
    startDBAgent()
    startIAAgent()

startAgents()
while True:
    pass