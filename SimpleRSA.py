def GCD(a , b): 
    if b == 0 :
        return a
    return GCD( b, a%b )

def inv_ele(e , r): #Inverse element
    d = 2
    while (e * d)% r != 1 :
        d += 1
    return d

if __name__ == '__main__':
    p = int(input("Input p:"))
    q = int(input("Input q:"))
    pText = int(input("Input plainText(int):"))
    N = p * q
    r = (p - 1) * (q - 1)
    e = 2
    while GCD(e ,r) !=1 :
        e += 1
    print('e = ' + str(e))
    d = inv_ele(e , r)
    
    print('Plaintext = ' +str(pText))
    cText = (pText ** e) % N
    print('After Encryption, Ciphertext =' + str(cText))
    print('d = ' + str(d))
    print('Ciphertext = ' + str(cText))
    pText = (cText ** d) % N
    print('After Decryption, Ciphertext =' + str(pText))
