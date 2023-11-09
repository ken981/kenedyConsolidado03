def convertir_a_base(z, b):
    if z == 0:
        return '0'

    digitos = "0123456789ABCDEF"

    resultado = ""
    while z > 0:
        resultado = digitos[z % b] + resultado
        z //= b

    return resultado
