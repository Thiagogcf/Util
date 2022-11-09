x=1
z=0
falta = 10
while x!=0:
    x = float(input("insira a nota"))
    if x == 0:
        break
    y = float(input("insira o peso"))
    falta = falta-y
    z = z + (x * (y/10))
    print("Nota até o momento =",z)

if falta > 0:
    precisa = 7-z
    nf = precisa/(falta/10)
    mediaprecisa = precisa/(falta/10)
    if nf < 4:
        nf = 4
    print("Voce precisa de ",precisa," ponto para passar sem exame, ou seja",mediaprecisa,"com peso 10")
    print("nota",nf ,"na prova")