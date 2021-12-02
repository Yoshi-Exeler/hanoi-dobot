from typing import Any
from typing import List
class Vec3D:
    X: float
    Y: float
    Z: float

    def __init__(self,x,y,z) -> None:
        self.X = x
        self.Y = y
        self.Z = z
        pass

    def __str__(self) -> str:
        return "X:"+str(self.X)+"Y:"+str(self.Y)+"Z:"+str(self.Z)
        pass

class Vec2D:
    X: float
    Z: float

    def __init__(self,x,z) -> None:
        self.X = x
        self.Z = z
        pass

    def __str__(self) -> str:
        return "X:"+str(self.X)+"Z:"+str(self.Z)
        pass


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
        self.lastPost: Vec3D
        pass

    def RunSequence(self, sequence) -> None:
        for elem in sequence:
            self.executeTurn(elem)
        pass

    def executeTurn(self, turn) -> None:
        self.moveToVector(self.indexToVector(turn.From),self.getStackHeight(turn.From)) # go to point a
        #self.device.suck(True) # enable the gripper
        self.changeStackHeight(turn.From,-1)
        self.moveToVector(self.indexToVector(turn.To),self.getStackHeight(turn.To)) # go to point b
        #self.device.suck(False) # disable the gripper
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
        dType.SetPTPCmd(api,2,target.X,height,target.Z,0,1)
        self.lastPost = Vec3D(target.X, height, target.Z)
        pass

class HanoiSolver:
    __sequence: list
    __r1: list
    __r2: list
    __r3: list

    def __init__(self,a,b,c) -> None:
        self.__r1 = a
        self.__r2 = b
        self.__r3 = c
        self.__sequence = []
        pass

    def Solve(self,i) -> List:
        self.solve(i,self.__r1,self.__r2,self.__r3)
        return self.__sequence

    def solve(self,i,a,b,c) -> None:
        if i > 0:
            self.solve(i-1,a,c,b)
            self.__sequence.append(HanoiTurn(self.getIndex(a),self.getIndex(c)))
            swap = c[self.topmost(c)] 
            c[self.topmost(c)] = a[self.topmost(a)] 
            a[self.topmost(a)] = swap
            print(self.getIndex(a)," --> ",self.getIndex(c))
            self.solve(i-1,b,a,c)
        pass

    def topmost(self,a) -> int:
        index = 0
        while True:
            if index == len(a)-1 or a[len(a)-(index+1)] != 0:
                break
            index += 1
        return index

    def getIndex(self,n) -> None:
        if n == self.__r1:
            return 0
        if n == self.__r2:
            return 1
        if n == self.__r3:
            return 2
    
class HanoiTurn:
    From: int
    To: int

    def __init__(self,fromP,toP) -> None:
        self.From = fromP
        self.To = toP


hs = HanoiSolver([1,2,3,4,],[0,0,0,0],[0,0,0,0])
sequence = hs.Solve(4)
ctrl = Controller()
ctrl.RunSequence(sequence)
