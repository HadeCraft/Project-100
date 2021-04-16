class Atm(object):
    def __init__(self,atmCardNumber,pinNumber,cashWidthdrawal,balanceEnquiry):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber
        self.cashWidthdrawal = cashWidthdrawal
        self.balanceEnquiry = balanceEnquiry

    def atmCardNumber(self):
        print("I HAVE YOUR ATM CARD NUMBER :)")

    def pinNumber(self):
        print("TELL ME YOU PIN NUMBER :(")

    def cashWidthdrawal(self):
        print("YOU HAVE WIDTHDRAWTH RS 5,00,00,000 FROM THE BANK")

    def balanceEnquiry(self):
        print("YOU PICK THE WRONG PLACE BUDDY FOR BALANCE ENQUIRY :)")

Money = Atm("123456789","1234","YOU HAVE WIDTHDRAWTH MONEY THEN REPAY IT","I THINK YOU ARE NOT ASKING FOR MONEY")

print(Money.atmCardNumber())
print(Money.pinNumber())
print(Money.cashWidthdrawal())
print(Money.balanceEnquiry())
