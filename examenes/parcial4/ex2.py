"""
    Francisco Oro @ FI UNAM
    Estructura de Datos y Algoritmos II
    Examen Parcial 3
    Problema 2
"""

def IdenticalFiles(file1:str, file2:str, encoding_system:str)->bool:
    f1 = open(file1, mode='r', encoding=encoding_system)
    f2 = open(file2, mode='r', encoding=encoding_system)

    while True:
        l1 = f1.readline()
        l2 = f2.readline()

        # End of comparision: Both files are identical
        if not l1 and not l2:
            f1.close()
            f2.close()
            return True

        # End of comparision: one line is empty and the other is not
        elif not l1 or not l2:
            f1.close()
            f2.close()
            return True
        
        else: 
            l1 = l1.strip()
            l2 = l2.strip()

            if l1 != l2:
                f1.close()
                f2.close()
                return False

if __name__ == '__main__':
    print(f'Are AlanTuring.txt and AlanTuring-copy.txt indentical? \n {IdenticalFiles("AlanTuring.txt", "AlanTuring-copy.txt", "utf-8")}')
    print(f'Are AlanTuring.txt and test.txt indentical? \n {IdenticalFiles("AlanTuring.txt", "test.txt", "utf-8")}')
