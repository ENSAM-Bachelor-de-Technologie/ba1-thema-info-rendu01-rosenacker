#!/bin/bash

cd src/

mv 2dNyuUs catpic_01.jpg

mv DaUjFXP catpic_02.jpg

mv jXR9j55 catpic_03.jpg

mv lNWZim1 catpic_04.jpg

mv s9hO9SP catpic_05.jpg

cd ..

mkdir picnathan

cd src/

mv catpic_0* /home/pi/ba1_thema_info/SHELL_SHOCKED/rendu01/picnathan/

rm .hi*

cd ..

mv picnathan .picnathan

mv src .src

touch favorite.txt

echo {"My name is "nathan" and my favorite cat pic is catpic_04.jpg"} > favorite.txt

cat favorite.txt


