while True:
        print('\nselect an operation:')
        print('1 Add (+)')
        print('2 sub (-)')
        print('3 multiply (*)')
        print('4 division (/)')
        print('5 exit')
        
        choice=input('enter your choice:  ')
        if choice=='5':
            print('exiting calculator')
            break
        if choice not in ['1','2','3','4','+','-','*','/']:
            print('invalid choice')
            continue
        num1=float(input('enter the first number: '))
        num2=float(input('enter the second number: '))
        
        if choice == '1' or choice=='+' :
            print('add',num1+num2)
        elif choice=='2' or choice=='-' :
            print('sub',num1-num2)
        elif choice=='3' or choice=='*' :
            print('multiply',num1*num2)
        elif choice=='4' or choice=='/' :
            print('division', num1/num2)
            
        else :
                print("ERROR: please enter between 1-4")
                continue
