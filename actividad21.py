# Diseña un algoritmo que permita mostrar las
# tablas de multiplicar del 1 al 10
def multiplicar():
    for x in range(11):
        for y in range (11):
            print(f'{x} x {y} = {x*y}')

# multiplicar()
#lo he intentado hacer con declarativa pero no he encontrado manera
def mult():
    lista=range(11)
    print(list(map(lambda x: x*1,lista)))
mult()
