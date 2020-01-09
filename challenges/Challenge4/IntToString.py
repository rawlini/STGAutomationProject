class IntToString:
    from math import log10, ceil

    underTwenty = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    
    tens= ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

    hundreds={0:"",1:"One Hundred",2:"Two Hundred",3:"Three Hundred",4:"Four Hundred",5:"Five Hundred",6:"Six Hundred",7:"Seven Hundred",8:"Eight Hundred",9:"Nine Hundred"}

    bigDigits={0:"",1:"",2:"",3:"",4:"Thousand",5:"",6:"",7:"Million",8:"",9:"",10:"Billion",11:"",12:"",13:"Trillion",14:"",15:"",16:"Quadrillion",17:"",18:"",19:"Quintillion"}

    def intToString(self,integer):
        intArray=[int(x) for x in str(integer)]
        arrayLength=len(intArray)
        if (arrayLength==0):
            print ("No Number Inserted")
            exit
        if (integer==0):
            print("Zero")
        if (integer<=20):
            Digit=self.underTwenty[integer]
            print (Digit)
        if (integer<100 and integer > 20):
            firstDigit=self.underTwenty[intArray[1]]
            secondDigit=self.tens[intArray[0]]
            print(secondDigit + firstDigit)
        if (arrayLength >= 3) :
            countdown=0
            countdownArray=[]
            while countdown < arrayLength :
                if ((arrayLength-countdown)%3==0) :
                    countdownArray.append(self.hundreds[intArray[countdown]])
                if ((arrayLength-countdown)%3!=0 and intArray[countdown]==1 and self.bigDigits[(arrayLength-countdown)]=="" and (arrayLength-countdown!=1)) :
                    countdown=countdown+1
                    countdownArray.append(self.underTwenty[intArray[countdown]+10] + " " + self.bigDigits[(arrayLength-countdown)])
                    countdown=countdown+1
                if ((arrayLength-countdown)%3!=0 and intArray[countdown]!=1 and self.bigDigits[arrayLength-countdown]=="" and (arrayLength-countdown!=1)) :
                    countdownArray.append(self.tens[intArray[countdown]])
                if ((arrayLength-countdown)%3!=0 and intArray[countdown]!=1 and self.bigDigits[arrayLength-countdown]=="" and (arrayLength-countdown==1)) :
                    countdownArray.append(self.underTwenty[intArray[countdown]])
                if ((arrayLength-countdown)%3!=0 and self.bigDigits[(arrayLength-countdown)]!="" and intArray[countdown!=1]) :
                    countdownArray.append(self.underTwenty[intArray[countdown]] + " " + self.bigDigits[arrayLength-countdown])
                countdown = countdown + 1
            return " ".join(countdownArray)
            
                    

                