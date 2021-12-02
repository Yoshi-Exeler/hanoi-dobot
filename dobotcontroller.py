from typing import Any
from hanoi.turn import HanoiTurn
from vector import Vec2D, Vec3D
from serial.tools import list_ports

import pydobot

class Controller:
    STACK_1_XZ: Vec2D
    STACK_2_XZ: Vec2D
    STACK_3_XZ: Vec2D
    STACK_1_H: float
    STACK_2_H: float
    STACK_3_H: float
    NEUTRAL_POS: Vec3D
    dobot: Any
    port: Any


    def __init__(self) -> None:
        self.STACK_1_XZ = Vec2D(0,0)
        self.STACK_2_XZ = Vec2D(0,0)
        self.STACK_3_XZ = Vec2D(0,0)
        self.STACK_1_H = 4
        self.STACK_2_H = 0
        self.STACK_3_H = 0
        available_ports = list_ports.comports()
        self.port = available_ports[0].device
        self.device = pydobot.Dobot(port=self.port, verbose=True)
        self.lastPost: Vec3D
        print("dobot connected successfully on "+self.port)
        pass

    def RunSequence(self, sequence) -> None:
        for elem in sequence:
            self.executeTurn(elem)
        pass

    def executeTurn(self, turn) -> None:
        self.moveToVector(self.indexToVector(turn.From),self.getStackHeight(turn.From)) # go to point a
        self.device.suck(True) # enable the gripper
        self.changeStackHeight(turn.From,-1)
        self.moveToVector(self.indexToVector(turn.To),self.getStackHeight(turn.To)) # go to point b
        self.device.suck(False) # disable the gripper
        self.changeStackHeight(turn.To,1)
        self.moveToVector(self.NEUTRAL_POS) # return to a neutral position
        pass

    def getStackHeight(self, idx: int) -> float:
        if idx == 0:
            return self.computeH(self.STACK_1_H)
        if idx == 1:
            return self.computeH(self.STACK_2_H)
        else:
            return self.computeH(self.STACK_3_H)

    def computeH(self,plates: int) -> float:
        return plates * 1 # insert magic number here

    def changeStackHeight(self,idx,delta) -> None:
        if idx == 0:
            self.STACK_1_H += delta
        if idx == 1:
            self.STACK_2_H += delta
        else:
            self.STACK_3_H += delta

    def indexToVector(self, idx: int) -> Vec2D:
        if idx == 0:
            return self.STACK_1_XZ
        if idx == 1:
            return self.STACK_2_XZ
        else:
            return self.STACK_3_XZ

    def computeRotation(self, newVec: Vec3D) -> float:
        # do magic rotation calc here
        return 0

    def moveToVector(self, target: Vec2D,height: float) -> None:
        self.device.move_to(target.X, height, target.Z, self.computeRotation(target.X, height, target.Z), wait=True)
        self.lastPost = Vec3D(target.X, height, target.Z)
        pass
