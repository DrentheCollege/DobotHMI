#!/usr/bin/python

import asyncio
import websockets
import signal
import sys
import DobotCommands as dc
import DatabaseActions as da
import json

def signal_handler(single, frame):
    print("Disconnecting Dobot")
    dc.DobotDisconnect()
    sys.exit(0)

async def server(websocket):
    async for message in websocket:
        data = json.loads(message)
        if data["command"] == "connect":
            await websocket.send("connected")
            # return
        if data["command"] == "home":
            dc.DobotHome();
            await websocket.send("homing")
            # return
        if data["command"] == "save":
            da.savePosition(data["position"])
            await websocket.send(message)
        if data["command"] == "get":
            da.getPosition(data["position"])
            await websocket.send(message)

async def main():
    signal.signal(signal.SIGINT, signal_handler)
    dc.DobotInit()
    async with websockets.serve(server, "", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
