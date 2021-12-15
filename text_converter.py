number = input('Enter number: ')
i = 0
hundreds = {1:'one hundred', 2:'two hundred', 3:'three hundred', 4:'four hundred',
5:'five hundred', 6:'six hundred', 7:'seven hundred', 8:'eight hundred', 9:'nine hundred'}
tens = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty',
7:'seventy', 8:'eighty', 9:'ninety'}
teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
ones = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
numArray = []
while i < len(number):
    print (i)
    numArray.append(int(number[i]))
    i = i+1
print (numArray)
numArray.reverse() #invert number to start from ones to higher digits
print (numArray)
#### Start Process Hundreds ####
try:
    if numArray[1] == 1: #find out if there are tEEns in the number
        for k,v in teens.items():
            if k == numArray[0]+10:
#            print (v)
                teen = v
    elif numArray[1] >= 2: #if second digit is not 0 or 1 go list the tens
        for k,v in tens.items():
            if k == numArray[1]:
#            print (v)
                ten = v
    for k,v in ones.items():
        if k == numArray[0]:
    #        print (v)
            one = v
except:
    for k,v in ones.items():
        if k == numArray[0]:
#        print (v)
            one = v

try:
    for k,v in ones.items():
        if k == numArray[2]:
#        print (v)
            hundred = v
except:
    hundred = ''
#### Finish Process Hundreds ####

#### Start Process Thousands ####
if len(number) > 3:
    try:
        if numArray[4] == 1: #find out if there are tEEns in the number
            for k,v in teens.items():
                if k == numArray[3]+10:
#            print (v)
                    teenThousand = v
        elif numArray[4] >= 2: #if second digit is not 0 or 1 go list the tens
            for k,v in tens.items():
                if k == numArray[4]:
#            print (v)
                    tenThousand = v
        else:
            for k,v in ones.items():
                if k == numArray[3]:
    #        print (v)
                    oneThousand = v
    except:
        for k,v in ones.items():
            if k == numArray[3]:
#        print (v)
                oneThousand = v

    try:
        for k,v in ones.items():
            if k == numArray[5]:
#        print (v)
                hundredThousand = v
    except:
        hundredThousand =''

    if len(number) < 5:
        thousandprint = (oneThousand + ' thousand')
    elif len(number) < 6:
        if numArray[4] == 1:
            thousandprint = (teenThousand + ' thousand')
        else:
            thousandprint = (tenThousand + ' ' + oneThousand + ' thousand')
    elif len(number) < 7:
        if numArray[4] == 1:
            thousandprint = (hundredThousand + ' hundred ' + teenThousand + ' thousand')
        elif numArray[4] == 0 and numArray[0] != 0:
            thousandprint = (hundredThousand + ' hundred ' + oneThousand + ' thousand')
        elif numArray[4] != 0 and numArray[4] != 1:
            thousandprint = (hundredThousand + ' hundred and ' + tenThousand + ' thousand')
        elif numArray[4] == 0:
            thousandprint = (hundredThousand + " hundred thousand")
        else:
            thousandprint = (hundredThousand + ' hundred ' + tenThousand + oneThousand + ' thousand ')
#### Finish Process Thousands ####

if len(number) < 2:
    oneprint = one
elif len(number) < 3:
    if numArray[1] == 1:
        oneprint = teen
    else:
        oneprint = (ten + ' ' + one)
elif len(number) < 4:
    if numArray[1] == 1:
        oneprint = (hundred + ' hundred and ' + teen)
    elif numArray[1] == 0 and numArray[0] != 0:
        oneprint = (hundred + ' hundred and ' + one)
    elif numArray[1] != 0 and numArray[1] != 1:
        oneprint = (hundred + ' hundred and ' + ten)
    elif numArray[0] == 0:
        oneprint = (hundred + ' hundred ')
    elif numArray[2] == 0 and numArray[1] == 0 and numArray[0] == 0:
        oneprint = ('')
    elif numArray[2] == 0 and numArray[1] == 0 and numArray[0] != 0:
        oneprint = (' and ' + one)
    elif numArray[2] == 0 and numArray[1] != 0 and numArray[1] != 1 and numArray[0] != 0:
        oneprint = (' and ' + ten + ' ' + one)
    elif numArray[2] == 0 and numArray[1] == 1:
        oneprint = (' and ' + teen)
    else:
        oneprint = (hundred + ' hundred and ' + ten + '' + one)
else:
    if numArray[1] == 1 and numArray[2] != 0:
        oneprint = (hundred + ' hundred and ' + teen)
    elif numArray[1] == 0 and numArray[0] != 0 and numArray[2] != 0:
        oneprint = (hundred + ' hundred and ' + one)
    elif numArray[0] == 0 and numArray[2] != 0:
        oneprint = (hundred + ' hundred ')
    elif numArray[2] == 0 and numArray[1] == 0 and numArray[0] == 0:
        oneprint = ('')
    elif numArray[2] == 0 and numArray[1] == 0 and numArray[0] != 0:
        oneprint = ('and ' + one)
    elif numArray[2] == 0 and numArray[1] != 0 and numArray[1] != 1 and numArray[0] != 0:
        oneprint = ('and ' + ten + ' ' + one)
    elif numArray[2] == 0 and numArray[1] == 1:
        oneprint = ('and ' + teen)
    else:
        oneprint = (hundred + ' hundred and ' + ten + '' + one)

try:
    print (thousandprint + ' ' + oneprint)
except:
    print (oneprint)
