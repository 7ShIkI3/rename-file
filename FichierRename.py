import os

def lancer():
    if __name__ == "__main__":
        main()

def affichage():
    print("_" * 80)

def saut_de_ligne(n:int):
    for _ in range(n):
        print()

def rename_file(destination:str, type_de_fichier:str, file_name:str):
    i = 0
    path = destination
    type = type_de_fichier
    name = file_name
    fichier = os.listdir(path)
    
    for filename in fichier:
        img_rename = name + str(i) + type
        source = os.path.join(path, filename)
        img_rename = os.path.join(path, img_rename)
        print("Source:", source)
        print("Destination:", img_rename)
        if os.path.exists(source):
            os.rename(source, img_rename)
            i += 1
    return True

def main():
    affichage()
    saut_de_ligne(1)
    print("Bienvenue sur FileRename !!")
    saut_de_ligne(1)
    print("Choissisez le type de fichier a renommer !")
    saut_de_ligne(1)
    print("[A] pour les fichiers .png")
    print("[B] pour les fichiers .jpg")
    print("[C] pour les fichiers .txt")
    print("[D] pour les fichiers a type personnaliser")
    
    saut_de_ligne(1)
    filetype = str(input("> "))
    
    if filetype == "A":
        name = "img"
        type = ".png"
    elif filetype == "B":
        name = "img"
        type = ".jpg"
    elif filetype == "C":
        name = "txt"
        type = ".txt"
    elif filetype == "D":
        name = str(input("Donnez un nom générique : "))
        type = str(input("Donnez un type de fichier ex '.txt' : "))
    else:
        exit(0)
    
    path_1 = str(input("Destination du fichier : "))
    path = path_1.replace("\\","/")
    affichage()
    rename_file(path, type, name)
    affichage()
    new = str(input("Tapez 'YES' pour recommencer : "))
    if new == "YES":
        print("\033c")
        lancer()
    else:
        exit(0)

lancer()