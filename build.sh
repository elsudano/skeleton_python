#!/bin/bash
# aquí hace falta comprobar si tenemos instalado el
# pyinstall y si no es el caso instalarlo y preguntarle
# al usuario si quiere instalarlo
# También tiene que leer el primer parámetro que se
# encarga de añadir el nombre a la aplicación

pyinstaller --noconfirm --clean --onefile --name $1 skeleton_python.spec