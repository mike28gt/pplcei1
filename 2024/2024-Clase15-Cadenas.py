'''
Tipo de dato texto
    Tambien es llamado cadena de caracteres o simplemente cadena.
    Las cadenas son secuencias de caracteres.

Caracteres
    Cualquier símbolo que pueda ser escrito a través del teclado de la 
    computadora es llamado cadena.

Cadenas literales
    El tipo de dato texto (también llamado cadena) debe tener un delimitador
    de inicio y un delimitador de final.
    El símbolo de delimitador puede ser:
        Comilla simple: '
            Ejemplo: 'Esto es una cadena'
        Comilla doble: "
            Ejemplo: "Esto es una cadena"
        
Caracteres de escape y secuencias de escape
    Existen símbolos que requieren ser representados de una forma espacial.
    Para esto se utiliza el caracter de escape.

    \ este símbolo detro de Python representa el caracter de escape.

    Las secuencias de escape son conjunto de símbolos que inician con el
    caracter de escape seguido de uno o mas caracteres, los cuales en conjunto
    representan un solo caracter. Los más utilizados son:
        \n representar un salto de línea (Enter)
        \t representa una tabulación de izquierda a derecha

Cadenas multilínea
    En alguna situaciones se requiere poder representar texto que
    contengan saltos de línea. Una forma de lograr esto es utilizando
    tes comillas (simples o dobles) como delimitador de inicio y 
    delimitador de fin de una cadena.
    Ejemplo:
        """Un párrafo está formado por oraciones o frases y se generan bajo
        una misma idea o tema, es decir, no se producen cambios temáticos 
        dentro de un mismo párrafo. Para ello deberíamos finalizar el
        párrafo actual y comenzar con uno nuevo marcando ese nuevo tema."""

Operaciones básicas con cadenas

    Longitud de una cadena: en situaciones es útil conocer cuantos caracteres
    conforman una cadena. Para esto se utiliza la funcion len(). Tenga en
    considieración que los espacios en blanco son considerados caracteres
    al igual, así también tenga en considieración que las secuencias de escape
    son consideradas como un único caracter.

    Ejemplo 1:  len("Hola mundo")
    Ejemplo 2:  s = "Esto es una cadena"
                len(s)

    Concatenación de cadenas:
        Es la unión de dos o más cadenas formando una nueva cadena compuesta
        por las cadenas concatenadas.
        El operador de concatenación es el símbolo +
        IMPORTANTE: cuando se utiliza el símbolo + con operandos de tipo
                    numérico, este representa la operación de adición (suma); 
                    y cuando se utiliza con operandos de tipo texto representa
                    la concatenación de cadenas.

        Ejemplo 1:  nueva_cadena = "Esto es " + "una nueva cadena"
        Ejemplo 2:  primer_nombre = 'Juan '
                    segundo_nombre = " Carlos"
                    nombres = primer_nombre + segundo_nombre
        
    Repetición de cadenas: En Python es posible repetir una misma cadena
    una determinada cantidad de veces utilizando el símbolo *.
    IMPORTANTE: Al igual que con el operador +, el operador * tiene dos
    usos diferentes dependiendo del tipo de dato de sus operandos.

    Ejemplo: '-' * 8 # repite 8 veces la cadena -

'''