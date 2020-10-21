# MCOC2020_P2_G8_Entrega5
## 1. Diseño Original:

  Se usó un diseño parecido al de la entrega 4 donde se “copió” el modelo de la imagen y se prolongó por los 230 metros que tenía el puente. Se debió partir y terminar el puente con barras horizontales de 4 metros y entremedio se colocaron barras de 6 y la altura de la punta de a estructura eran 13,5 metros más que la del tablero, quedando de la siguiente manera:

![alt text](https://github.com/EduardoGM98/MCOC2020_P2_G8_Entrega5/blob/main/IMAGEN.png)<br>

![alt text](https://github.com/EduardoGM98/MCOC2020_P2_G8_Entrega5/blob/main/IMAGEN2.png)
![alt text](https://github.com/EduardoGM98/MCOC2020_P2_G8_Entrega5/blob/main/IMAGEN3.png)
Las propiedades de las barras fueron las siguientes:

Barras del tablero: R = 8 cm, t = 5 mm, E = 200*GPa, Densidad = 7600 kg/m3, Tension de fluencia = 420 MPa

Barras diagonales superiores: props2 = R = 8 cm, t = 1 cm, E = 200*GPa, Densidad = 7600 kg/m3, Tension de fluencia = 420 MPa

Barras horizontales superiores: props3 = R = 8 cm, t = 3 cm, E = 200*GPa, Densidad = 7600 kg/m3, Tension de fluencia = 420 MPa


También se implementaron 3 pilares ubicados en lugares estratégicos del espacio (donde calzaran con los nodos del tablero del puente). Originalmente estos pilares tenían las mismas propiedades que las barras del tablero. Como era de esperarse ninguna barra cumplía con las condiciones de diseño, esto es (FU > 0.95 si se puede), (FU <=1), (Fn*ϕ >= Fu), (lamda < 300).

![alt text](https://github.com/EduardoGM98/MCOC2020_P2_G8_Entrega5/blob/main/IMAGEN4.png)<br>

Peso del modelo original:   1243,769 toneladas. (Sin cumplir condiciones de diseño)

## 2. Cambios en el reticulado:

Inicialmente el modelo fue estructurado con un tablero mostrado en la parte anterior, el cual era soportado por 3 grandes reticulados (con barras R = 8*cm, t = 5mm) que cumplian la funcion de pilares. Nos dimos cuenta que esto no era eficiente, ya que agregaba cerca de 300 barras a la estructura. 
Para solucionar este problema retiramos estos reticulados y colocamos 6 pilares largos, más unas barras cruzadas de nodo del suelo a nodo del tablero, con propiedades R = 24 cm y t = 5 cm, el cual aumentó de manera consistente el peso a 30.781 ton, lo cual cumplía con las condiciones de diseño. 

![alt text](https://github.com/EduardoGM98/MCOC2020_P2_G8_Entrega5/blob/main/IMAGEN5.png)<br>

Una vez alcanzado el cumplimiento de todas las restricciones para cada barra y para cada combinación de cargas, se procedió a ir bajando paulatinamente las medidas de las propiedades de todas las barras, a esto lo llamaremos iteraciones las cuales fueron las siguientes:


### - Primera iteración:

Las propiedades de las barras fueron las siguientes:

Barras del tablero: R= 20 cm, t = 1 cm 

Barras diagonales superiores: R = 20 cm, t = 1 cm

Barras horizontales superiores y pilares: R = 25 cm, t = 3 cm

Peso: 20.514,27 toneladas <br>
Se debe agregar que incluir los desplazamientos de los casi 120 nodos para cada iteracion no tiene sentido por lo que se dara un breve resumen alfinal de este informe con los desplazamientos finales.

### - Segunda iteración:

Al tener estas dimensiones absurdas, nos dimos cuenta que no era útil tener las mismas propiedades para los pilares que para las barras horizontales del tablero, así que decidimos separarlas para obtener mejores valores del peso.

Las propiedades de las barras fueron las siguientes:

Barras del tablero: R= 12 cm, t = 1 cm 

Barras diagonales superiores: R = 15 cm, t = 1 cm

Barras horizontales superiores: R = 15 cm, t = 2 cm

Barras pilares: R = 25 cm, t = 3 cm

Peso: 5.973,67 toneladas


### - Tercera iteración:

Para esta iteración seguimos disminuyendo las propiedades de las barras.

Las propiedades de las barras fueron las siguientes:

Barras del tablero: R= 10 cm, t = 5 mm 

Barras diagonales superiores: R = 12 cm, t = 1 cm

Barras horizontales superiores: R = 12 cm, t = 5 mm

Barras pilares: R = 25 cm, t = 3 cm

Peso: 3.128,90 toneladas


### - Cuarta iteración:
Para esta iteración se cambiaron las propiedades de la tercera iteración, pero nos dimos cuenta de que la altura de la punta del puente era excesiva por lo que se cambió de 13 metros a 8 metros. Todas las condiciones se cumplieron y se obtuvo un peso de: 2371,142 toneladas

Las propiedades de las barras fueron las siguientes:

Barras del tablero: R= 8 cm, t = 5 mm 

Barras diagonales superiores: R = 12 cm, t = 1 cm

Barras horizontales superiores: R = 10 cm, t = 5 mm

Barras pilares: R = 20 cm, t = 3 cm

Peso: 2.371,142 toneladas


### - Quinta iteración:
De la misma manera que la iteración pasada, reducimos la altura de la punta del puente ahora a 5 metros en comparación con el tablero, nuevamente todas las condiciones se cumplieron y el peso fue de: 2114,33 toneladas.

Las propiedades de las barras fueron las siguientes:

Barras del tablero: R= 8 cm, t = 8 mm 

Barras diagonales superiores: R = 10 cm, t = 8 mm

Barras horizontales superiores: R = 10 cm, t = 8 mm

Barras pilares: R = 20 cm, t = 3 cm

Peso: 2.114,33 toneladas


### -Sexta iteración:
En esta iteración, nos interesamos en los pilares donde probamos distintos espesores para llegar a su peso ideal, de tal forma que se sigan cumpliendo las condiciones de diseño.
Las propiedades de las barras fueron las siguientes:

Barras del tablero: R= 8 cm, t = 8 mm 

Barras diagonales superiores: R = 10 cm, t = 8 mm

Barras horizontales superiores: R = 10 cm, t = 8 mm

Barras pilares: R = 20 cm, t = 2 cm

Peso: 1.668,15 toneladas


### -Séptima iteración:
En esta iteración, nos interesamos en optimizar los espesores de las barras principales del reticulado. Al iterar nos dimos cuenta que el espesor de las barras diagonales superiores podia disminuir. Las propiedades de las barras fueron las siguientes:

Barras del tablero: R= 8 cm, t = 8 mm 

Barras diagonales superiores: R = 10 cm, t = 2 mm

Barras horizontales superiores: R = 10 cm, t = 8 mm

Barras pilares: R = 20 cm, t = 2 cm

Peso: 1.423,65 toneladas 

Por ultimo al calcular los desplazamientos nodales del ultimo modelo ultilizado (septima iteracion), el promedio de estos desplazamientos para los 121 nodos del reticulado fue: 3 mm aproximadamente.<br>
También, el promedio de los FU de todas las barras antes de rediseñar para el caso 1 era de 0,02, mientras que para el caso 2 era de 0,37

Podemos ver que el peso de nuestro modelo inicialmente era de 1.243,769 toneladas sin cumpir las condiciones de diseño para traccion y compresion. Pero a traves de las iteraciones y modificaciones en el modelo se llegó a un peso de 1.423,65 toneladas, lo cual es bastante cercano al peso inicial. Con esto podemos decir que gracias a los cambios realizados logramos un modelo de un peso similar, pero que cumple con las restricciones de modelo y con el material de acero optimizado


