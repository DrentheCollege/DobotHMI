#!/usr/bin/python

import asyncio
import websockets
import signal
import sys
import dobot
import database
import json

def signal_handler(single, frame):
    print("Disconnecting Dobot")
    dobot.disconnect()
    sys.exit(0)

async def server(websocket):
    async for message in websocket:
        print(message)
        data = json.loads(message)
        if data["command"] == "connect":
            result = '{"result":"connected"}'
        if data["command"] == "home":
            dobot.home();
            result = '{"result":"homing"}'
        if data["command"] == "save":
            database.save_position(data["position"])
            result = '{"result":"saved"}'
        if data["command"] == "get":
            result = database.get_position(data["position"])
        if data['command'] == "move":
            dobot.move(data["movement"])
            result = '{"result": "position", "position": ' + dobot.get_position() + '}'
        print(result)
        await websocket.send(result)

async def main():
    signal.signal(signal.SIGINT, signal_handler)
    dobot.init()
    async with websockets.serve(server, "", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
