import random as rd
import string as st

def nueva_contrasena(longitud, mayusculas, minusculas, numeros, simbolos):
    """
    Genera una nueva contraseña basada en las preferencias del usuario.
    
    Parámetros:
    - longitud (int): Longitud de la contraseña a generar.
    - mayusculas (bool): Si se deben incluir letras mayúsculas.
    - minusculas (bool): Si se deben incluir letras minúsculas.
    - numeros (bool): Si se deben incluir números.
    - simbolos (bool): Si se deben incluir símbolos.
    
    Retorna:
    - str: La contraseña generada.
    """
    caracteres = ''
    if mayusculas:
        caracteres += st.ascii_uppercase
    if minusculas:
        caracteres += st.ascii_lowercase
    if numeros:
        caracteres += st.digits
    if simbolos:
        caracteres += st.punctuation

    # Verifica que al menos un tipo de carácter haya sido seleccionado
    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")

    # Genera la contraseña aleatoria
    contrasena = ''.join(rd.choice(caracteres) for _ in range(longitud))
    return contrasena

def obtener_longitud():
    """
    Solicita al usuario ingresar una longitud válida para la contraseña.
    
    Retorna:
    - int: La longitud de la contraseña ingresada por el usuario.
    """
    while True:
        try:
            longitud = int(input('Ingrese la longitud para la nueva contraseña: '))
            if longitud <= 0:
                print('El valor debe ser superior a cero, ingrese otro valor.')
            else:
                return longitud
        except ValueError:
            print('Error: debe ingresar un número válido.')

def main():
    """
    Función principal que solicita las preferencias del usuario y genera la contraseña.
    """
    print("Bienvenido al Generador de Contraseñas")
    longitud = obtener_longitud()
    mayusculas = input('Desea que su contraseña contenga mayúsculas? (s/n): ').strip().lower() == 's'
    minusculas = input('Desea que su contraseña contenga minúsculas? (s/n): ').strip().lower() == 's'
    numeros = input('Desea que su contraseña contenga números? (s/n): ').strip().lower() == 's'
    simbolos = input('Desea que su contraseña contenga símbolos? (s/n): ').strip().lower() == 's'
    
    try:
        contrasena = nueva_contrasena(longitud, mayusculas, minusculas, numeros, simbolos)
        print(f'Su nueva contraseña es: {contrasena}')
    except ValueError as e:
        print(e)
        print('Por favor, intente de nuevo.')

if __name__ == '__main__':
    main()
