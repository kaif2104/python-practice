import keyword


def rev(a=""):

    a=list(a)
    n = len(a)
    b=''

    i=0
    while i<n-1-i:
        a[i],a[n-1-i]=a[n-1-i],a[i]
        b+=a[i]
        i+=1
    while i<n:
        b+=a[i]
        i+=1

    return b


def revwrd(a):
    a = list(a)
    n = len(a)
    s = 0

    for i in range(n):
        if i==n-1 or a[i+1]==' ':
            e=i
            while(s<e):
                a[s],a[e]=a[e],a[s]
                s+=1
                e-=1
            s=i+2
    i=0
    s=''
    while i<n:
        s+=a[i]
        i+=1
    return s


def count(a,sub,start=0,end=0):

    j=0
    c=0
    y=0
    k=len(sub)
    if end==0:
        end=len(a)
    i=start
    while i<end:

        if(a[i]==sub[j]):


            for x in range(i,i+k):
                if a[x]==sub[j]:
                    j += 1
                    y += 1
                else:
                    y=0
                    j=0

            if(y==len(sub)):
                c+=1
                j=0
                i+=k
                y=0
            else:
               y=0

        else:
            j=0
        i+=1

    return c
# print(count("maulikchutiyomaulik","li",0,16))





def index(a,sub,start=0,end=0):

    j=0
    c=0
    k=len(sub)
    if end==0:
        end=len(a)
    for i in range(start,end):

        if(a[i]==sub[j]):
            j+=1
            if(j==len(sub)):
                c=i+1-k
                return c
        else:
            j=0

    raise ValueError("substring not found")


# print(index('lekhankh','kh',4,6))



def find(a,sub,start=0,end=0):

    j=0
    c=0
    k=len(sub)
    if end==0:
        end=len(a)
    for i in range(start,end):

        if(a[i]==sub[j]):
            j+=1
            if(j==len(sub)):
                c=i+1-k
                return c
        else:
            j=0

    return -1
#
# print(find('lekhankh','kh',4,6))

s='lekhan'

def startswith(a,sub,start=0,end=0):
    i=0
    j=0
    k=len(sub)
    if end==0:
        end=len(a)
    for i in range(start,end):
        if (a[i] == sub[j]):
            j += 1
            if (j == len(sub)):
                return True

        else:
            return False



def endswith(a,sub,start=0,end=0):
    i=0
    j=0
    k=len(sub)
    if end==0:
        end=len(a)

    for i in range(end-k,end):
        if (a[i] == sub[j]):
            j += 1
            if (j == len(sub)):
                return True

        else:
            return False

# print(endswith(s,'ha',1,5))

def isdigit(a):
    for i in a:
        if not (ord(i)>=48 and ord(i)<=57):
            return False
    return True


# print(isdigit('1234123'))

def isalpha(a):
    for i in a:
        if not ((ord(i)>= 65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
            return False
    return True
# print(isalpha('abh545cj'))

def isalnum(a):
    for i in a:
        if not(isdigit(i) or isalpha(i)):
            return False
    return True

def isidentifier(a):
    if a in keyword.kwlist:
        return False
    if not(a[0]=="_" or isalpha(a[0])):
        return False


    for i in a:

        if not (isalnum(i) or i=="_"):
            return False

    return True
# print(isidentifier("async"))

def upper(a):
    s=''
    tem=0
    for i in a:
        if(ord(i)>=97 and ord(i)<=122):
            tem=ord(i)-32
            s+=chr(tem)
        else:
            s+=i

    return s

def lower(a):
    s=''
    tem=0
    for i in a:
        if(ord(i)>=65 and ord(i)<=90):
            tem=ord(i)+32
            s+=chr(tem)
        else:
            s+=i

    return s
# print(upper("lekHan"))
# print(lower("lekHan"))


def title(a):
    c=0
    s=''
    for i in a:
        if (isalpha(i)):
            if(c==0):
                s+=upper(i)
                c=1
            else:
                s+=lower(i)
        else:
            c=0
            s+=i
    return s

# s="hi_i am mangalya"
# print(title(s))

def isupper(a):
    for i in a:
        if not (ord(i)>=65 and ord(i)<=90):
            return False
    return True

def islower(a):
    for i in a:
        if not (ord(i)>=97 and ord(i)<=122):
            return False
    return True
# s='lekhAn'
# print(islower(s))

def istitle(a):
    c=0

    for i in a:
        if (isalpha(i)):
            if(c==0):
                if (not isupper(i)):
                    return False
                c=1
            else:
                if(not islower(i)):
                    return False



        else:
            c=0

    return True

def capitalize(a):
    s=""
    c=0
    for i in a:
        if c==0:
            s+=upper(i)
            c=1
        else:
            s+=lower(i)

    return s



# s='i 1m ABC'
# print(capitalize(s))

# def split(a,sp=' '):
#     s=''
#     a=list(a)
#     j=0
#     l=[0]
#     n=len(a)
#
#
#     countsp=count(a,sp)
#     if a[n-1]==sp and a[0]==sp:
#         for i in range(countsp-2):
#             l = l + [0]
#     elif a[n-1]==sp :
#         for i in range(countsp-1):
#             l = l + [0]
#     elif a[0]==sp:
#         for i in range(countsp-1):
#             l = l + [0]
#     else:
#         for i in range(countsp):
#             l = l + [0]
#
#     i=0
#     while i<=n:
#         if i==0 and a[i]==sp:
#             i+=1
#             pass
#         else:
#             if i == n - 1 and a[i] == sp:
#                 l[j] = s
#                 return l
#
#             if not (a[i] == sp):
#
#                 s += a[i]
#                 i += 1
#                 if i == n:
#                     l[j] = s
#                     return l
#             else:
#                 l[j] = s
#                 j += 1
#                 i += 1
#                 s = ''
#     return l

def split(a,sp=' '):
    s=''

    a=list(a)
    l=[0]
    f=0

    y=0


    countsp=count(a,sp)
    if startswith(a,sp) and endswith(a,sp):
        for i in range(0,countsp-2):
            l=l+[0]
    elif startswith(a,sp):
        for i in range(0,countsp-1):
            l=l+[0]
    elif endswith(a,sp):
        for i in range(0,countsp-1):
            l=l+[0]
    else:
        for i in range(0,countsp):
            l=l+[0]
    i=0
    sp=list(sp)

    j=0
    while i<len(a):
        if(a[i]==sp[j]):
            z = i
            for x in sp:

                if not a[z] == x:
                    y = 0
                    z += 1
                    break


                else:
                    y = 1
                    z += 1

            if y:
                if not s == '':
                    l[f] = s
                    s = ''
                    f += 1

                else:
                    pass
                i = i + len(sp) - 1
            else:
                s += a[i]



        else:
            s+=a[i]
        i+=1

    if not endswith(a,sp):
        l[f]=s
    return l

# s='khlekkhkkkhan'
#
# print(split(s,'kh'))


def join(a,sub):
    s=''
    i=0
    j=0
    while i<len(sub)-1:
        s+=sub[i]
        for j in a:
            s+=j
        i+=1
    s+=sub[i]
    return s

s='lekhan'
c=['21','12','33']
print(s.join(c))
print(join(s,c))




def replace(a,sp,re):
    s=""
    for i in a:
        if i==sp:
            s+=re
        else:
            s+=i
    return s




# def format(a,*b):
#     s=''
#     t=''
#     c=0
#     i=0
#     n=len(a)
#
#     while i<n:
#         if(a[i]=='{'):
#             while i<n-1:
#
#                 if (a[i+1] == '}'):
#                     c += 1
#                     break
#
#                 elif i == '{':
#                     raise ValueError("unexpected '{' in field name")
#                 else:
#                     raise ValueError("expected '}' before end of string")
#                 i+=1
#
#         elif i=='}':
#             raise ValueError("Single '}' encounter in format string")
#         i+=1
#
#     if(len(b)<c):
#         raise IndexError("Replacement index out of range for positional args tuple")
#     i=0
#     j=0
#
#     while i<n:
#         if(a[i]=='{' and a[i+1]=='}'):
#             s += chr(b[j])
#             j += 1
#         elif a[i]=='{' and a[i+1]!='}':
#             i+=1
#             while i < n and a[i] != "}":
#                 t += i
#                 i += 1
#             raise KeyError(t)
#         else:
#             s+=a[i]
#             i+=1
#     return s
def format(a,*b):
    s=''
    j=-1
    i=0
    l=split(a,'{}')


    if startswith(a,'{}'):
        j+=1
        s+=str(b[j])



    while i<len(l):
        for x in l[i]:
            if x=='{':
                raise ValueError("unexpected '{' in field name")
            elif x=='}':
                raise ValueError("Single '}' encounter in format string")

        if j<len(l)-1:

            s+=l[i]
            s+=str(b[j])
        else:
            s+=l[i]


        i+=1
        j+=1

    if endswith(a,'{}'):
        s+=str(b[j])

    return s

# s="{}i am lek{}h{}an{}"
# print(format(s,10,20,30,40))


s='What is your name'
def s1(a):
    i=0
    s=''
    l=split(a,' ')
    while i<len(l):
        if len(l[i])>=2:
            s+='@'
            x=1
            while x<len(l[i])-1:
                s+=l[i][x]
                x+=1
            s+='#'

        else:
            s+='@'

        s+=' '
        i+=1
    return s



def s2(a):
    i=0
    s=''
    l=split(a,' ')
    while i<len(l):
        if len(l[i])>=2:
            s+=upper(l[i][0])
            x=1
            while x<len(l[i])-1:
                s+=l[i][x]
                x+=1
            s+=upper(l[i][(len(l[i])-1)])

        else:
            s += upper(l[i][0])

        s+=' '
        i+=1
    return s


def s3(a):
    i = 0
    s = ''
    l = split(a, ' ')
    while i < len(l):
        if len(l[i]) >= 2 and len(l[i])%2==0 :
            x = 0
            while x < len(l[i]):
                s+=l[i][x+1]
                s+=l[i][x]
                x+=2

        elif len(l[i]) >= 2 and len(l[i])%2!=0:
            x = 0
            while x < (len(l[i])-1):
                s += l[i][x + 1]
                s += l[i][x]
                x += 2
            s+=l[i][x]

        else:
            s += l[i]

        s += ' '
        i += 1
    return s


def s4(a):
    s=''
    i=0
    while i <len(a):
        if i%2==0:
            s+=lower(a[i])
        else:
            s+=upper(a[i])
        i+=1
    return s



def s5(a):
    i = 0
    s = ''
    l = split(a, ' ')
    while i < len(l):
        x = 0
        while x < len(l[i]) - 1:
            s += l[i][x]
            x += 1
        s+=str(len(l[i]))
        s += ' '
        i += 1
    return s

def s6(a):
    i = 0
    s = ''
    l = split(a, ' ')
    while i < len(l):
        x=0
        if i%2==0:
            while x < len(l[i]):
                if x%2==0:
                    s+=l[i][x]
                else:
                    s+=str(x)
                x+=1

        else:
            while x < len(l[i]):
                if x%2!=0:
                    s+=l[i][x]
                else:
                    s+=str(x)
                x+=1


        s += ' '
        i += 1
    return s
print(s6(s))

def s7(a):
    i = 0
    s = ''
    for i in a:
        if(a=='o' or a=='O'):
            s+=str(0)


    return s

def clockwizerotate(a,r):
    n=len(a)
    i=0


    while i<r:
        t=a[-1]
        j=n-1
        while j>0:
            a[j]=a[j-1]
            j-=1
        a[j]=t
        i+=1
    return a

def clockwizerotate(a,r):
    n=len(a)
    m=n-(r%n)
    print(m)
    i=0
    e=m-1
    while i<e:
        a[i], a[e] = a[e], a[i]
        i+=1
        e-=1
    i=m
    e=n-1
    while i<e:
        a[i], a[e] = a[e], a[i]
        i+=1
        e-=1

    i=0
    e=n-1
    while i<e:
        a[i], a[e] = a[e], a[i]
        i += 1
        e -= 1
    return a


# s=[3,9,6,5,4,2,1,3]
# print(clockwizerotate(s,3))
def rotatelist(a):
    i=0
    j=0
    m=0
    x=0
    n=len(a)
    for i in range(0,n//2):
        for j in range(i,n-1-i):

            t = a[i][j]
            while x < len(a):
                a[i][j] = a[n - 1 - j][i]
                i, j = n - 1 - j, i
                x += 1
            a[i][j] = t
            x=0

    return a

# print(rotatelist([[1,2,3],[4,5,6],[7,8,9]]))



s='substringsubsubstring'
print(s.split('sub'))
print(split(s,'sub'))

























