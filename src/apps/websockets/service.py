from typing import List
from pydantic import BaseModel, Json, ValidationError
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from collections import defaultdict


class GroupManager:
    def __init__(self):
        self.active_rooms: dict = defaultdict(dict)
        self.active_connections: List[WebSocket] = []
    async  def connect(self,websocket:WebSocket,roomname:str):
        print(socket_manager.active_rooms)
        await websocket.accept()
        if self.active_rooms[roomname] == {}:
            print("im heree")
            self.active_rooms[roomname] = []
        self.active_rooms[roomname].append(websocket)
        print(len(self.active_rooms[roomname]), "lenght")
        self.active_connections.append(websocket)
    async def disconnect(self,websocket:WebSocket,roomname:str):
        self.active_rooms[roomname].remove(websocket)
        self.active_connections.remove(websocket)
    async def send_group_message(self,websocket:WebSocket,roomname:str,message:str):
        if websocket in self.active_rooms[roomname]:
            for socket in self.active_rooms[roomname]:
                await socket.send_text(message)
        else:
            self.connect(websocket,roomname)
            self.send_group_message(websocket,roomname,message)
        
    async def send_personal_message(self,roomname:str,message:str):
        for socket in self.active_rooms[roomname]:
            await socket.send_text(message)
    async def send_json_message(self, roomname: str, message: Json):
        for socket in self.active_rooms[roomname]:
            await socket.send_json(message)
    async def send_file(self,roomname:str,img:bytes):
        for socket in self.active_rooms[roomname]:
            await socket.send_bytes(img)



socket_manager = GroupManager()


    

    
