from hanoi.hanoi import HanoiSolver
from dobotcontroller import Controller

hs = HanoiSolver([1,2,3,4,],[0,0,0,0],[0,0,0,0])
sequence = hs.Solve(4)
ctrl = Controller()
ctrl.RunSequence(sequence)