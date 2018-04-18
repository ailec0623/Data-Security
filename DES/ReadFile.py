d = {'0':"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", 
     "8":"1000", "9":"1001", "a":"1010", "b":"1011", "c":"1100", "d":"1101", "e":"1110", "f":"1111"}

def readf(fp, fk):
    l_p = []
    l_k = []
    f_p = open(fp)
    f_k = open(fk)
    p = f_p.read()
    k = f_k.read()
    if len(p) != 16 or len(k) != 16:
        print("Length of plaintext or key is wrong!")
        exit()
    
    for i in p:
        if i.lower() in d.keys():
            for j in d[i.lower()]:
                l_p.append(j)
        else:
            print("Unknow char!")
            exit()
    for i in k:
        if i.lower() in d.keys():
            for j in d[i.lower()]:
                l_k.append(j)
        else:
            print("Unknow char!")
            exit()
    return l_p, l_k