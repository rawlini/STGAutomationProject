class Fibonnaci:
    output=None
    def fibonnaciSequence(self,Number):
        a=0
        b=1
        i=1
        while (i<= Number):
            a,b= b+a,a
            i=i+1
        return b