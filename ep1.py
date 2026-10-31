print("Modos de operacao: ")
print("1 - Valor presente de um financiamento")
print("2 - Valor minimo da prestacao para valor presente cobrir pagamento a vista")
print("3 - Comparacao de opcoes de pagamento")
print("4 - Tabela comparativa de opcoes de pagamento para taxas variadas")

#modo 1
m = int(input("Numero do modo desejado: "))
if m == 1:
    prestacao = int(input("Valor da prestacao: "))
    i = int(input("Taxa de juros: "))
    n = int(input("Numero de prestacoes: "))
    
    prestacao >= 0
    i = i/1000
    
    v1 = (prestacao / i)
    v2 = (1 + (i) - 1 /((1 + (i)) **(n - 1)))
    VP = int( (v1) * (v2))
    print("Valor presente: ", VP )
    
#modo 2
if m == 2:
    a = int(input("Valor a vista: "))
    i = int(input("Taxa de juros: "))
    n = int(input("Numero de prestacoes: "))

    i = i/1000

    v1 = (i * a)
    v2 = (1 + (i) - 1 /((1 + (i)) **(n - 1)))
    P = ( (v1) / (v2) )
    PT = int(P + 0.999) #0.9999 é a mesma coisa que 1
    print("Menor prestacao cujo valor presente do financiamento cobre o valor a vista: ",(PT))

#modo 3
elif m == 3:
    a = int(input("Valor a vista: "))
    i = int(input("Taxa de juros: "))
    u = int(input("Valor da prestacao em 12 vezes: "))
    d = int(input("Valor da prestacao em 24 vezes: "))

    i = i/1000

    VPA = a
    
    v1 = (u / i)
    v2 = (1 + (i) - 1 /((1 + (i)) **(11)))
    VPU = int( (v1) * (v2) )
    print("Valor presente em 12 vezes: ", VPU )

    v1 = (d / i)
    v2 = (1 + (i) - 1 /((1 + (i)) **(23)))
    VPD = int( (v1) * (v2) )
    print("Valor presente em 24 vezes: ", VPD )

    if VPA < VPU:
        print("Numero de parcelas da melhor opcao de pagamento: 1" )
    elif VPA < VPD:
        print("Numero de parcelas da melhor opcao de pagamento: 1" )
    elif VPA == VPD and VPA == VPU:
        print("Numero de parcelas da melhor opcao de pagamento: 1" )
    elif VPD < VPU:
        print("Numero de parcelas da melhor opcao de pagamento: 24" )
    elif VPD > VPU:
            print("Numero de parcelas da melhor opcao de pagamento: 12" )
    elif VPD == VPU:
        print("Numero de parcelas da melhor opcao de pagamento: 12" )

#modo 4
elif m == 4:
    a = int(input("Valor a vista: "))
    u = int(input("Valor da prestacao em 12 vezes: "))
    d = int(input("Valor da prestacao em 24 vezes: "))
    s = int(input("Inicio da sequencia das taxas: "))
    t = int(input("Numero de taxas: "))
    p = int(input("Incremento de uma taxa para a proxima: "))
    
    VPA = a

    PA = (s + ( t - 1) * p)
    
    i = s / 1000
        
    v1 = (u / i)
    v2 = (1 + (i) - 1 /((1 + (i)) **(11)))
    VPU = int( (v1) * (v2) )
        
    v1 = (d / i)
    v2 = (1 + (i) - 1 /((1 + (i)) **(23)))
    VPD = int( (v1) * (v2) )
        
    if VPA < VPU and VPA < VPD:
        b = 1
    elif VPA == VPD and VPA == VPU:
        b = 12
    elif VPD < VPU:
        b = 24
    elif VPD > VPU:
        b = 12
    elif VPD == VPU:
        b = 12

    print("taxa | a  vista | 12 vezes | 24 vezes | decisao")
    print(" %3d | %8d | %8d | %8d | %2d" %(s, a, VPU, VPD,b))

    PA = (s + ( t - 1) * p)

    while (s + p) <= PA:

        s = s + p
        
        VPA = a
        i = s / 1000
        
        v1 = (u / i)
        v2 = (1 + (i) - 1 /((1 + (i)) **(11)))
        VPU = int( (v1) * (v2) )

        v1 = (d / i)
        v2 = (1 + (i) - 1 /((1 + (i)) **(23)))
        VPD = int( (v1) * (v2) )
        
        if VPA < VPU and VPA < VPD:
            b = 1
        elif VPU == VPA:
            b = 1
        elif VPD < VPU:
            b = 24 
        elif VPD > VPU:
            b = 12
        elif VPU < VPA:
            b = 12
        elif VPD == VPU:
            b = 12
        
        print(" %3d | %8d | %8d | %8d | %2d" %(s, a, VPU, VPD,b))
