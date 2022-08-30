from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

#funcion para obtener el id de la patente
@app.route('/patente/<patente>')
def getIdPatente(patente):
    #transformar patente a Mayusculas, y creacion diccionario de Abecedario
    patente = patente.upper()
    caracteres = {
        'A' : 0,
        'B' : 1,
        'C' : 2,
        'D' : 3,
        'E' : 4,
        'F' : 5,
        'G' : 6,
        'H' : 7,
        'I' : 8,
        'J' : 9,
        'K' : 10,
        'L' : 11,
        'M' : 12,
        'N' : 13,
        'O' : 14,
        'P' : 15,
        'Q' : 16,
        'R' : 17,
        'S' : 18,
        'T' : 19,
        'U' : 20,
        'V' : 21,
        'W' : 22,
        'X' : 23,
        'Y' : 24,
        'Z' : 25,
    }
    #auxiliares para calculo de id
    letras = 0
    numeros = 0;
    #validar tamaño de la patente
    if len(patente) == 7:
            #para obtener el id hay que trabajar las letras y numeros por separado
        for i in range(4):#recorrer primeros 4 caracteres
            if patente[i] in caracteres:#validadr si caracter es una letra del abecedario
                #al haber 26 letras se calcular la "probabilidad" de cada caracter segun su posicion
                letras += caracteres[patente[i]] * (26**(3-i))
                # print(str(caracteres[patente[i]]) + " * " + str((26**(3-i))) + " = " + str(caracteres[patente[i]] * (26**(3-i))))
                # print(str(letras))
            else:
                return 'Patente Invalida'
        if patente[4:7].isnumeric():
            #se valida si los ultimos 3 caracteres son un numero y se transforma
            numeros = int(patente[4:7])
        else:
            return 'Patente Invalida'
        #finalmente el valor dado por la letra se multipica por 1000, ya que las posibilidades de los numeros son 1000
        #y se le suma el valor de los numeros, y se le adiciona 1 ya que el 000 es de id 1
        return str((letras *1000) + numeros +1)
    else: 
        return "patente invalida"

#funcion para obtener el la patente en base la id
@app.route('/id/<int:id_patente>')
def getPatenteId(id_patente):
    #creacion diccionario de Abecedario
    caracteres = {
        'A' : 0,
        'B' : 1,
        'C' : 2,
        'D' : 3,
        'E' : 4,
        'F' : 5,
        'G' : 6,
        'H' : 7,
        'I' : 8,
        'J' : 9,
        'K' : 10,
        'L' : 11,
        'M' : 12,
        'N' : 13,
        'O' : 14,
        'P' : 15,
        'Q' : 16,
        'R' : 17,
        'S' : 18,
        'T' : 19,
        'U' : 20,
        'V' : 21,
        'W' : 22,
        'X' : 23,
        'Y' : 24,
        'Z' : 25,
    }
    #a la patente se le resta 1 para empezar desde el 0
    #para saber los numeros de patente se calcula el resto de la division por 1000
    numero_patente = ((id_patente - 1) % 1000)
    #para el calculo de de las letras de la patente se calcula el cuociente al dividir por 1000 
    letras_patente = (id_patente - 1) // 1000
    
    #variable aux para ir guardando lo que queda al restar el valor de cada letra
    resto = 0
    patente = ""
    if letras_patente>0:
        for e in range(4):#ciclo para las letras de la patente
            for i, caracter in reversed(list(enumerate(caracteres))):#recorrer el array de letras e ir restando su respectivo valor
                #se calcula cada "probabilidad"
                letra = i * (26 ** (3-e))
                resto = letras_patente - letra
                if resto >= 0:#si el valor que me queda post resta es mayor a 0 asigno la letra y continuo con la siguiente posicion
                    # print(str(i) + " 26 ** " + str(3-e) + " == " + str(letra))
                    # print(str(letras_patente) + " - " + str(letra) + " == " + str(resto))
                    patente += str(caracter)
                    letras_patente = resto
                    break
    else:#si el cuociente de las letras es menor que 0 las letras de la patente son AAAA
        patente = "AAAA"
    
    #concatenacion de el numero de la patente, y se valida si se necesita anteponer 0s
    if numero_patente<10:
        patente += "00" + str(numero_patente)
    else:
        if numero_patente < 100:
            patente += "0" + str(numero_patente)
        else:
            patente += str(numero_patente)


    return patente


if __name__ == '__main__':
    app.run(debug=True)