import random


class Robot2:
    def __init__(self):
        self.sos = []

    def setSayings(self, u):
        self.sos = u

    def speak(self):
        r = random.randint(1, len(self.sos))
        return print(self.sos[r-1])


r1 = Robot2()
u1 = ["Exterminate, Exterminate!", "I obey!",
      "You cannot escape.", "Robots do not feel fear.",
      "The Robots must survive!"]
r1.setSayings(u1)
print("Robot r1 says: ")
r1.speak()

print("Robot r2 says: ")
r2 = Robot2()
u2 = ["I obey!"]
r2.setSayings(u2)
r2.speak()
