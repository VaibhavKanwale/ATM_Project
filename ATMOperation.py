from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00
def deposite():
    damt=float(input("Enter the Deposit Amount:"))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxxxxxxx1234 Credited with INR:{}".format(damt))
        print("Now Ur Account xxxxxxxxxx1234 Balance After Deposit INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter the Withdarw Amount:"))
    if(wamt<=0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxxxxxx1234 Debited with INR:{}".format(wamt))
        print("Now Ur Account xxxxxxxxxx1234 Balance after Withdraw INR:{}".format(bal))
def balenq():
    print(" Ur Balance in Account xxxxxxxxxx1234 INR:{}".format(bal))
