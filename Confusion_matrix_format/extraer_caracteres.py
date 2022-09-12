import os 
  
path = r"D:\Convertir\pred"
os.chdir(path) 
def read_text_file(file_path): 
    with open(file_path, 'rt') as f: 
        print(f.read())

  
  
for file in os.listdir(): 
    
    if file.endswith(".txt"): 
        file_path = f"{path}\{file}"
        print(file_path)

        archivo = open(file_path, "rt")
        texto = archivo.read()
        texto = texto.replace('"frame_id"', '')
        texto = texto.replace(',', '')
        texto = texto.replace('"filename"', '')
        texto = texto.replace('"class_id"', '')
        texto = texto.replace('"name"', '')
        texto = texto.replace('"relative_coordinates"', '')
        texto = texto.replace('{', '')
        texto = texto.replace('}', '')
        texto = texto.replace('"center_x"', '')
        texto = texto.replace('"center_y"', '')
        texto = texto.replace('"width"', '')
        texto = texto.replace('"height"', '')
        texto = texto.replace('"confidence"', '')
        texto = texto.replace(']', '')
        texto = texto.replace('[', '')
        texto = texto.replace(':', '')
        texto = texto.replace('"Sobremaduro"', '')
        texto = texto.replace('"Inmaduro"', '')
        texto = texto.replace('"Pinton"', '')
        texto = texto.replace('"Maduro"', '')
        texto = texto.replace('"objects"', '')
        texto = texto.replace('  ', ' ')
        archivo.close()
        archivo = open(file_path, "wt")
        archivo.write(texto)
        archivo.close()
