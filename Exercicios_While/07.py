vr_digitado = int(input("Digite um valor entre 1 e 10.000: "))
mult =1

for count in range(2,vr_digitado):
    if (vr_digitado % count == 0):
        print("Multiplo de ",count)
        mult +=1

if (mult==0):
    print("é primo")

else
        
