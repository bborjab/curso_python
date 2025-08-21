#Leer un archivo lÃ­nea por lÃ­nea
"""with open('caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las lÃ­neas en una lista
"""with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

#AÃ±adir texto
"""with open('caperucita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""

#Sobreescribir el texto
with open('caperucita.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")