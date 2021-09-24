def tarjetas(x,y):
    papel= (x*12)
    plumones= (y*35)
    if papel<plumones:
        return(papel)
    elif plumones<papel:
        return(plumones)
def main():
    #escribe tu código abajo de esta línea
    pliegos = int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones = int(input("Dame la cantidad de plumones: "))
    maxtarjetas = tarjetas(pliegos,plumones)
    print("El número máximo de tarjetas que se pueden hacer es: " + str(maxtarjetas))

if __name__=='__main__':
    main()
