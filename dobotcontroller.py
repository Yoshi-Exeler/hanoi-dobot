from typing import Any
from hanoi.turn import HanoiTurn
from vector import Vector
from serial.tools import list_ports

import pydobot

class Controller:
    STACK_1_POS: Vector
    STACK_2_POS: Vector
    STACK_3_POS: Vector
    NEUTRAL_POS: Vector
    dobot: Any
    port: Any


    def __init__(self) -> None:
        self.STACK_1_POS = Vector(0,0,0)
        self.STACK_2_POS = Vector(0,0,0)
        self.STACK_3_POS = Vector(0,0,0)
        available_ports = list_ports.comports()
        self.port = available_ports[0].device
        self.device = pydobot.Dobot(port=self.port, verbose=True)
        print("dobot connected successfully on "+self.port)
        pass

    def RunSequence(self, sequence) -> None:
        for elem in sequence:
            self.executeTurn(elem)
        pass

    def executeTurn(self, turn) -> None:
        self.moveToVector(self.indexToVector(turn.From)) # go to point a
        self.device.suck(True) # enable the gripper
        self.moveToVector(self.indexToVector(turn.To)) # go to point b
        self.device.suck(False) # disable the gripper
        self.moveToVector(self.NEUTRAL_POS) # return to a neutral position
        pass

    def indexToVector(self, idx: int) -> Vector:
        if idx == 0:
            return self.STACK_1_POS
        if idx == 1:
            return self.STACK_2_POS
        else:
            return self.STACK_3_POS

    def moveToVector(self, target: Vector) -> None:
        self.device.move_to(target.X, target.Y, target.Z, 0, wait=True)
        pass
