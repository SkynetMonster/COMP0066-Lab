from datetime import date


class CreditCard:
    def __init__(self, expiryMonth, expiryYear, firstName, lastName, ccNumber):
        self.em = expiryMonth
        self.ey = expiryYear
        self.fn = firstName
        self.ln = lastName
        self.cc = ccNumber

    def formatExpiryDate(self):
        return str(self.em) + '/' + str(self.ey)[2:4]

    def formatFullName(self):
        return self.fn + ' ' + self.ln

    def formatCCNumber(self):
        return str(self.cc[0:4]) + ' ' + str(self.cc[4:8]) + ' ' + str(self.cc[8:12]) + ' ' + str(self.cc[12: 16])

    def isValid(self):
        today = date.today()
        if (self.em <= today.month) and (self.ey <= today.year):
            return 'True'
        else:
            return 'False'

    def __str__(self):
        return 'Number: ' + self.formatCCNumber() + ' ' + 'Expiry date: ' + self.formatExpiryDate() + '\nAccount holder: ' + self.formatFullName() + ' ' + 'Is valid: ' + self.isValid()


cc1 = CreditCard(10, 2014, "Bob", "Jones", "1234567890123456")
print(cc1.__str__())