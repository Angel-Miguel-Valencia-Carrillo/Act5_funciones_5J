print("Ejemplo de funciones")
# daclarando funciones
def hola():
    print("Alguien uso la funcion hola")
def chat(mensa):
    print(f"chat {mensa}")
def ellacontesta(mensa):
        print(f"chat {mensa}")
def escribenombre(ap,n):
    print(f"tu nombre es :{n} {ap}")
def suma(a,b):
    s=a+b 
    return s
def resta(a,b):
    r=a-b 
    return r
def multiplicacion(a,b):
    m=a*b 
    return m
def division(a,b):
    d=a/b 
    return d
# llamadas a funciones
hola()
chat("Que bonita estas")
ellacontesta("gracias")
escribenombre("Valencia", "Angel")
print("Operaciones suma")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damesuma=suma(c1,c2)
print(f"la suma de {c1} + {c2} ={damesuma}")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
dameresta=resta(c1,c2)
print(f"la resta de {c1} - {c2} ={dameresta}")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damemulti=multiplicacion(c1,c2)
print(f"la multiplicacion de {c1} * {c2} ={damemulti}")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damedivision=division(c1,c2)
print(f"la division de {c1} / {c2} ={damedivision}")