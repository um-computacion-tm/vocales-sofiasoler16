

def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = ("a", "e", "i", "o", "u")
    resultado = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for letra in palabra:
        if letra in vocales:
            resultado[letra] += 1

    eliminar = [vocal for vocal,
                valor in resultado.items() if valor == 0]

    for clave in eliminar:
        del resultado[clave]
    
    return resultado

if __name__ == "__main__":
    string = input("Enter a string, please: ")
    print(contar_vocales(string))

#Ejercicio hecho en clase

# def contar_vocales(palabra):
#     palabra = palabra.lower()
#     vocales = ("a", "e", "i", "o", "u")
#     resultado = {}
#     for letra in palabra:
#         if letra in vocales:
#             # La letra es vocal
#             if letra in resultado.keys():
#                 # Sumar valor a diccionario ya existente
#                 resultado[letra] += 1
#             else:
#                 # Agregar letra por primera vez
#                 resultado[letra] = 1

#     return resultado
