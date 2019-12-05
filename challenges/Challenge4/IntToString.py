class IntToString:

    singledigits = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    
    teens= ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    
    doubledigits= [None,None,"Twenty ","Thirty ","Forty ","Fifty ","Sixty ","Seventy ","Eighty ","Ninety "]
    
    def intToString(self,integer):
        intArray=[int(x) for x in str(integer)]
        intArray.reverse()
        arrayLength=len(intArray)
        if (arrayLength==0):
            print ("No Number Inserted")
        if (arrayLength==1):
            firstDigit=self.singledigits[intArray[0]]
            print (firstDigit)
        if (arrayLength==2 and intArray[1]!=1):
            firstDigit=self.singledigits[intArray[0]]
            if (intArray[1]==1):
                teensDigit=self.teens[intArray[0]]
                print(teensDigit)
                exit
            else:
                secondDigit=self.doubledigits[intArray[1]]
            print(secondDigit + firstDigit)
        if (arrayLength==3 and intArray[1]!=1):
            firstDigit=self.singledigits[intArray[0]]
            if (self.doubledigits[intArray[1]]!=None):
                secondDigit=(" "+self.doubledigits[intArray[1]]) 
            else:
                secondDigit=" "
            thirdDigit=self.singledigits[intArray[2]]
            print(thirdDigit+" hundred and"+secondDigit+firstDigit)
        if (arrayLength==3 and intArray[1]==1):
            teensDigit=self.teens[intArray[0]]
            thirdDigit=self.singledigits[intArray[2]]
            print(thirdDigit+" hundred and "+teensDigit)
