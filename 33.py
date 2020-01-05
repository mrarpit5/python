class Deductions:
    def display():
        pay = int(input("Enter pay : "))
        hours = int(input("Enter hours worked : "))
        it = pay*15/100
        print("Federal income tax : ",it)
        ps = pay*3/100
        print("Payroll savings : ",ps)
        st = pay*6.2/100
        print("Social security tax : ",st)
        rp = pay*8.5/100
        print("Retirement pension : ",rp)
        netpay = pay + (it-ps-st-rp)
        print("Netpay : ",netpay)
Deductions.display()
