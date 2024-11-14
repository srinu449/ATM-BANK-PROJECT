class bank:
    acbal=10000
    wc=3
    dc=3
    def confirm(self):
        print("1. Contiue ")
        print("0. Exit")
        option=int(input("Choose your option :"))
        if option==1:
            obj.viewOptions()

    def deposit(self):
        if self.dc==0:
                print("try after 24 hours")
        else:
            while(self.dc):
                amount=int(input("Enter deposite amount"))
                if(amount%100==0):
                    if(amount<=50000):
                        self.acbal=self.acbal+amount
                        print("your account balance is : ",self.acbal)
                        self.dc-=1
                        break;
                    else:
                        print("amount should be less than 50000 only")
                        self.dc-=1
                else:
                    print("enter multiples of 100 only")
                    self.dc-=1
    def withdraw(self):
        five=0
        two=0
        one=0
        if self.wc==0:
                print("try after 24 hours")
        else:
            while(self.wc):
                amount=int(input("Enter withdraw amount"))
                amountt=amount
                five=amount//500
                amount=amount%500
                two=amount//200
                amount=amount%200
                one=amount//100
                amount=amount%100
                if(amount<=self.acbal ):
                    if(amount%100==0):
                        if(amount<=20000):
                            print("no.of 500 notes",five)
                            print("no.of 200 notes",two)
                            print("no.of 100 notes",one)
                            self.acbal=self.acbal-amountt
                            print("available balance is: ",self.acbal)
                            self.wc-=1
                            break;
                        else:
                            print("limit is 20000 only")
                            self.wc-=1
                    else:
                        print("enter multiples of 100 only")
                        self.wc-=1
                else:
                    print("insufficient balance")
                    self.wc-=1

    def balance(self):
        print("your balance amount is: ",self.acbal)

    def viewOptions(self):
        print("1. deposite")
        print("2. withdraw")
        print("3. balance enquiry")
        print("0. exit")
        option=int(input("choose your option"))
        if option==1:
            obj.deposit()
            obj.confirm()
        elif option==2:
            obj.withdraw()
            obj.confirm()
        elif option==3:
            obj.balance()
            obj.confirm()


    def validate(self):
        pin=1234
        print("welcome to my bank")
        upin=int(input("enter pin number: "))

        if pin==upin:
            obj.viewOptions()


        else:
            print("invalid")

obj=bank()
obj.validate()