mochila = ["navaja","sable de luz","brujula","lentes","celular","guantes","manzana"]
def busqueda(vector,buscado):
    if(len(vector) == 0):
        return -1
    elif(buscado == vector[-1]):
        return len(vector) - 1
    else:
        print("Se encontro",vector[-1],"en la mochila.")
        return busqueda(vector[:-1],buscado)



busquedaObjetos = busqueda(mochila,"sable de luz")
if(busquedaObjetos = -1):
    print("Se encontro el sable de luz")
    print("Se tuvieron que sacar",len(mochila)-busquedaObjetos,"objetos de la mochila para encontrarlo")
else:
    print("No se encontro el sable de luz en la mochila que contiene ",len(mochila),"objetos")

