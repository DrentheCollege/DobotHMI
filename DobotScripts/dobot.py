import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}


#Load Dll and get the CDLL object
def init():
    global state, api, lastindex
    api = dType.load()
    state = dType.ConnectDobot(api, "", 115200)[0]
    print("Connect status:",CON_STR[state])
    if (state == dType.DobotConnect.DobotConnect_NoError):
        dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
        dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
        dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

def home():
    global state, api, lastindex
    if (state == dType.DobotConnect.DobotConnect_NoError):
        #Clean Command Queued
        dType.SetQueuedCmdClear(api)
        #Async Home
        dType.SetHOMECmd(api, temp = 0, isQueued = 1)
        dType.SetQueuedCmdStartExec(api)
        dType.SetQueuedCmdStopExec(api)

def disconnect():
    #Disconnect Dobot
    dType.DisconnectDobot(api)

def move(movement):
    # SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200 + offset, offset, offset, offset, isQueued = 0)
    print("move function" + movement)

def get_position():
    # p = dType.getPos(api)
    # result = '{"x": ' + p[0] + ',"y": ' + p[1] + ',"z": ' + p[2] + ',"r": ' + p[3] + '}'
    result = '{"x": 11,"y": 12,"z": 13,"r": 14}'
    return result
