from abc import ABC, abstractmethod


class FatherClass:
    def __init__(self,title):
        self.company = title

    def make_payment(self,mode,amount):
        if mode == "cash" or mode =="cheque":
            print(f"A payment of ₹{amount:.2f} is made thru' {mode}")
        else:
            print("Other modes of payment not accepted")
    @abstractmethod
    def recieve_payment(self,mode,amount):
        print("hello")


class Sonclass(FatherClass):
    def recieve_payment(self, mode, amount):
        print("Other modes of payment not accepted")

    def __init__(self,title):
        super().__init__(title)  #Referes to immediate base class and is required whtn U want to call the base
        # class's init to set the values to the base clas
        self.company = title
    def make_payment(self,mode,amount):
        if mode == "cash" or mode =="upi":
            print(f"A payment of ₹{amount:.2f} is made thru' {mode}")
        else:
            print("Cheque payments not accepted")

business = Sonclass('SBC Provisions')
print(business.company)
business.make_payment("upi",6000)
business.recieve_payment("cheque",6555)
