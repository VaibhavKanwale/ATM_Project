from ATMMenu import menu
from ATMExcept import DepositError,WithDrawError,InSuffFundError
from ATMOperation import deposite,withdraw,balenq
import sys
while(True):
    menu()
    try:
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                try:
                    deposite()
                except DepositError:
                    print("Don't enter -VE OR Zero for Deposit Amount")
                except ValueError:
                    print("Don't try Deposit alnums,strs and symbols for Depositing Amount")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("Don't enter -VE OR Zero for Withdrawing Amount")
                except InSuffFundError:
                    print("Ur Account does not have Sufficient Funds")
                except ValueError:
                    print("Don't try Withdraw alnums,strs and symbols for Depositing Amount")
            case 3:
                balenq()
            case 4:
                print("Thx for using this program")
                sys.exit()
            case _:
                print("Ur Selection of Operation Wrong--Try Again")
    except ValueError:
        print("Ur Choice of Operation should not be alnums,strs and symbols")

