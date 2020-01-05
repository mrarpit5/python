class error(Exception):
    pass
class demo(error):
    pass
try:
    i_num = int(input("enter no"))
    if i_num == 0:
        raise error
    else:
        print(i_num)
except error:
    print("exception")
    print()


    
