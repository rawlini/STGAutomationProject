damageCount=[0,0,0,0,0]

def RearEnd():
    damageCount[0]+=1
def FrontEnd():
    damageCount[1]+=1
def DentScratches():
    damageCount[2]+=1
def Undercarriage():
    damageCount[3]+=1
def Misc():
    damageCount[4]+=1

switcher={'REAR END': RearEnd,'FRONT END': FrontEnd, 'MINOR DENT/SCRATCHES':DentScratches,'UNDERCARRIAGE':Undercarriage}

def switch(damage):
    return switcher.get(damage, Misc)()