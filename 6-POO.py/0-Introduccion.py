'''
Paradigmas de la programacion: -> POO
                               -> Programacion Orientada a Procedimientos

Desventajas de Programacion Orientada a Procedimientos:
1). Unidades de codigo my grandes.
2). En aplicaione complejas el codigo era dificil de descifrar.
3). Poco reutilizable.
4). Si exites un fallo en una linea de codio, es muy probable que todo el programa falle.
5). Es dificil de depurar por otros programadores en caso de necesidad o error.
6). Aparcion de codigo spaguetti (El codigo no se ejecuta de  forma lineal).

POO: Traslada el comportamiento que tienen los objetos de la vida real al codigo
     de programacion.
     Los objetos tienen un estado, un comportamiento y unas propiedades.

Ventajas de la POO:
1). Programas dividos en trozos, partes, modulos o clases
2). Muy reutilizable. Herencia
3). Si existe un fallo en una linea de codigo, el programa continuara su funcionamiento.
    Tratamiento de excepciones.
4). Encapsulamiento.


Vocabulario:

-> Clase: Modelo donde se redactan las caracteristicas comunes de un grupo de objetos.

-> Ejemplar de clase = Instancia de clase: Objeto pertenciente a una clase.

-> Modularizacion: Diferentes clases en un programa que hacen una labor especifica.

-> Encapsulacion: Funcionamiento interno de una clase

Si creamos metodos de acceso podemos hacer que las diferentes clases trabajen en equipo,
pero hay algunas caracteristicas encapsuladas para que no sea accesibles.

Ejemplo: 
    Objeto:
        Accediendo a propiedades del objeto:
            micoche.color = 'rojo'
            micoche.marca = 'Audi'
        Accediendo a comportamiento del objeto
            micoche.arranca()
            michoce.frena()
'''
