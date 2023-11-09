def convertir_a_base(z, b):
    if z == 0:
        return '0'

    digitos = "0123456789ABCDEF"

    resultado = ""
    while z > 0:
        resultado = digitos[z % b] + resultado
        z //= b

    return resultado

def main():
    z = int(input("Introduce el número natural z (z >= 0): "))
    b = int(input("Introduce la base b (2 <= b <= 16): "))

    if not (2 <= b <= 16):
        print("La base debe estar entre 2 y 16.")
        return

    resultado_conversion = convertir_a_base(z, b)
    print(f"{resultado_conversion} representa al entero {z} en base {b}.")

if __name__ == '__main__':
    main()
