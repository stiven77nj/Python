'''
Son archivos con extension .py o .pyc(Python Compilado) o archivo escrito en
C para CPython que posee su propio espacio de nombres y que puede contener variables,
funciones, clases e incluso otros modulos.

Sirven para organizar y reutilizar el codigo.

En python cada uno de nuestros archivos .py se denominan modulos. Estos modulos
pueden formar paquetes. Un paquete es una cadena que contiene archivos .py.
Pero para que una carpeta pueda ser conisderada un paquete, debe contener un archivos
--init--.py. Este archivo no necesita contener ninguna instruccion.

        |--paquete
            |-- __init__.py
            |-- modulo1.py
            |-- modulo2.py
            |-- modulo3.py

Los paquetes a su vez pueden contener subpaquetes. Y los modulos no necesariamente
deben permancer a un paquete.
'''
'''
El contenido de cada modulo se puede usar en otros modulos. Entonces debemos importar
los modulos que deseamos importar. Para importar un modulo:

        import nombre_modulo (sin el .py) -> Importa un modulo que no pertence al paquete
        import paquete.nombre_modulo -> Importa un modulo que esta dentro de un paquete
        import paquete.subpaquete.nombre_modulo

La instrucción import seguida de nombre_del_paquete.nombre_del_modulo, nos
permitirá hacer uso de todo el código que dicho módulo contenga.

Python tiene sus propios módulos, los cuales forman parte de su librería de módulos estándar,
que también pueden ser importados.

'''
