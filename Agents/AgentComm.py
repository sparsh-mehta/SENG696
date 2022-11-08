# ------------------------------Protocol Related Defines Don't Change##-----------------------------------
class AgentCommunication:

    CommunicationTxBuffer = ""
    CommunicationRxBuffer = ""
    CommunicationFlag = False
    CommunicationError = False

    IAAgentUserID = "faker1@jabbim.com"
    IAAgentPassword = "Qwerty123"
    IPAgentUserID = "faker@lightwitch.org"
    IPAgentPassword = "Qwerty123"
    FVAgentUserID = "faker2@jabbim.com"
    FVAgentPassword = "Qwerty123"
    DBAgentUserID = "faker3@jabbim.com"
    DBAgentPassword = "Qwerty123"

    # Agent IDs
    IAAgentID = "1"
    IPAgentID ="2"
    FVAgentID = "3"
    DBAgentID = "4"

    # Error Codes
    Success = '0'
    Failure = '1'

    # index reserved for :
    SenderAgentIDIndex = 0
    ReceiverAgentIDIndex = 1
    ErrorCodeIndex = 2
    DataIndex = 3
    
# ------------------------------------------------------------------------------------------

def request(SenderAgentID, ReceiverAgentID, ErrorCode, Data):
    AgentCommunication.CommunicationTxBuffer = SenderAgentID + ReceiverAgentID + ErrorCode + ':' + Data
    AgentCommunication.CommunicationFlag = True
    while AgentCommunication.CommunicationFlag:
        pass

    # if Slave Agent is not responding
    if AgentCommunication.CommunicationError:
        AgentCommunication.CommunicationRxBuffer = ""
    AgentCommunication.CommunicationTxBuffer = ""    
    
    # AgentCommunication.CommunicationRxBuffer = "410:Data"
    AgentCommunication.CommunicationRxBuffer = AgentCommunication.CommunicationRxBuffer.split(":")
    # AgentCommunication.CommunicationRxBuffer = ["410", "Data"]

    return AgentCommunication.CommunicationRxBuffer[0][AgentCommunication.ErrorCodeIndex], AgentCommunication.CommunicationRxBuffer[1:]