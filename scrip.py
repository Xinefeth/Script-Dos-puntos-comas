# Puedes poner la ruta absoluta o relativa aquí
ruta_entrada = r"C:/Users/Usuario\Desktop\winequality-red 1.csv" # ← CAMBIA ESTO
ruta_salida = r"C:/Users/Usuario\Desktop\winequality-red 1.csv"  # ← Y ESTO

# Abrir el archivo original con separador ;
with open(ruta_entrada, 'r', encoding='utf-8') as archivo_original:
    lineas = archivo_original.readlines()

# Reemplazar ; por ,
lineas_convertidas = [linea.replace(';', ',') for linea in lineas]

# Guardar en el nuevo archivo con separador ,
with open(ruta_salida, 'w', encoding='utf-8') as nuevo_archivo:
    nuevo_archivo.writelines(lineas_convertidas)

print(f"Conversión completada. Archivo guardado en: {ruta_salida}")
