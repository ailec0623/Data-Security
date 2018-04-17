def IP_1(lt):
    c_n = [57, 49, 41, 33, 25, 17, 9 ,
           1 , 58, 50, 42, 34, 26, 18,
           10, 2 , 59, 51, 43, 35, 27,
           19, 11, 3 , 60, 52, 44, 36]
    d_n = [63, 55, 47, 39, 31, 23, 15,
           7 , 62, 54, 46, 38, 30, 22,
           14, 6 , 61, 53, 45, 37, 29,
           21, 13, 5 , 28, 20, 12, 4 ]
    c0 = []
    d0 = []
    for i in c_n:
        c0.append(lt[i-1])
    for i in d_n:
        d0.append(lt[i-1])
    return c0, d0

def sh(c0, d0):
    l_s = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    l_c = []
    l_d = []
    
    for i in l_s:
        for x in range(0,i):
            ct = c0[0]
            dt = d0[0]
            for j in range(0,27):
                c0[j] = c0[j+1]
                d0[j] = d0[j+1]
            c0[27] = ct
            d0[27] = dt

        l_c.append(c0[:])
        l_d.append(d0[:])

    return l_c, l_d

def key_gen(l_c,l_d):
    l = [14, 17, 11, 24, 1 , 5 , 3 , 28,
         15, 6 , 21, 10, 23, 19, 12, 4 ,
         26, 8 , 16, 7 , 27, 20, 13, 2 ,
         41, 52, 31, 37, 47, 55, 30, 40,
         51, 45, 33, 48, 44, 49, 39, 56,
         34, 53, 46, 42, 50, 36, 29, 32]
    l_k = []
    for i in range(0,len(l_c)):
        t = []
        for j in l:
            if j <29:
                t.append(l_c[i][j-1])
            else:
                t.append(l_d[i][j-29])
        l_k.append(t[:])
    return l_k