def main():
    def PhNum(PhoNumber):
        Num=PhoNumber.split('-')
        AreaCode=Num[0]
        NumEnd=Num[1:]
        Number=''
        for n in NumEnd:
            for i in range (len(n)):
                if n[i] in 'ABCabc2':
                    Number=Number+'2'
                elif n[i] in 'DEFdef3':
                    Number=Number+'3'
                elif n[i] in 'GHIghi4':
                    Number=Number+'4'
                elif n[i] in 'JKLjkl5':
                    Number=Number+'5'
                elif n[i] in 'MNOmno6':
                    Number=Number+'6'
                elif n[i] in 'PQRSpqrs7':
                    Number=Number+'7'
                elif n[i] in 'TUVtuv8':
                    Number=Number+'8'
                elif n[i] in 'WXYZwxyz9':
                    Number=Number+'9'
                elif n[i] in '1':
                    Number=Number+'1'
                elif n[i] in '0':
                    Number=Number+'0' 
            Number=Number+'-'
        return AreaCode+'-'+Number[:-1]
        
    PhoNumber = input("Input number: ")
    print(PhoNumber)
    NewNum=PhNum(PhoNumber)
    print('New number:', NewNum)
    
main()