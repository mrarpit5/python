class m:
    def __init__(self,n,n1):
        self.n=n
        self.n1=n1
    def ma(self):
        try:
            ans=self.n/self.n1
            print(ans)
        except():
            print("exception")
ob2=m(10,2)
ob2.ma()
