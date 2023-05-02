romans = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}

def ConvertToDecimal(nRomano,acumulador = 0):
    if(len(nRomano) > 1):
        if(romans.get(nRomano[0]) >= romans.get(nRomano[1])):
            acumulador = acumulador + romans.get(nRomano[0])
            return ConvertToDecimal(nRomano[1:len(nRomano)],acumulador)
        else:
            acumulador = acumulador - romans.get(nRomano[0])
            return ConvertToDecimal(nRomano[1:len(nRomano)],acumulador)
    elif(len(nRomano)==1):
       return  acumulador + romans.get(nRomano[0])
    else:
        return acumulador
 

num = "MMMCCXXIV"
res = ConvertToDecimal(num)
print("nuermo romano",num)
print("numero a decimal",res)