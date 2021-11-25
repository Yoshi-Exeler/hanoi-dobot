from typing import List
from hanoi.turn import HanoiTurn

#funktion bewege (Zahl i, Stab a, Stab b, Stab c) {
#    falls (i > 0) {
#       bewege(i-1, a, c, b);
#       verschiebe oberste Scheibe von a nach c;
#       bewege(i-1, b, a, c);
#    }
#}

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
    