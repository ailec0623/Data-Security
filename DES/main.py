import ReadFile
import Funct

d = {"0000":'0', "0001":'1', "0010":'2', "0011":'3', "0100":'4', "0101":'5', "0110":'6', "0111":'7', 
     "1000":'8', "1001":'9', "1010":'A', "1011":'B', "1100":'C', "1101":'D', "1110":'E', "1111":'F'}

p0,k0 = ReadFile.readf("E:\\class\\data security\\Project\\Data-Security\\DES\\p.txt","E:\\class\\data security\\Project\\Data-Security\\DES\\k.txt")

c0,d0 = Funct.PC_1(k0) 

l_c, l_d = Funct.sh(c0, d0)

l_k = Funct.key_gen(l_c, l_d)

c = Funct.cipher(p0, l_k)

r_c = []
for i in range(0,16):
    s = ''
    s+=str(c[i*4])
    s+=str(c[i*4+1])
    s+=str(c[i*4+2])
    s+=str(c[i*4+3])
    r_c.append(d[s])
print(r_c)