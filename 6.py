def string_convert(s,numRows):
    a = (int(numRows)-1)*2
    i = 0 
    j = 0
    b = 0
    li = []
    while j <numRows:
        a -= j*2
        b += j*2
        temp = ''
        i = j
        k = 0 
        while i<len(s):
            temp +=s[i]
            if k % 2==0 and a!=0:
                i+=a
            else:
                if b!=0:
                    i+=b
                else:
                    i+=a
            k += 1        
            li.append(temp)
        j += 1
    print(li)
string_convert('PAYPALISHIRING',3)