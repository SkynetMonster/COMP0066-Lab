class Robot1:
    def __init__(self):
        self.batteryCharge = 5.0

    def move(self, distance):
        dalm = 0.0
        if self.batteryCharge < 0.5:
            print('Not Enough Power')
        else:
            while dalm <= distance:
                dalm += 1
                if self.batteryCharge < 0.5:
                    print('Out of Power')
                    break
                self.batteryCharge -= 0.5
                print(dalm)
        return None

    def batteryReCharge(self, charge):
        self.batteryCharge += charge
        return print('Battery charge is: ' + str(self.batteryCharge))


r = Robot1()
r.move(11)
r.batteryReCharge(2.5)
r.batteryReCharge(0.5)
r.move(5)
