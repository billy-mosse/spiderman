# spiderman

**Posibles datasets**:

- Bicis -> https://data.buenosaires.gob.ar/dataset/bicicletas-publicas/archivo/22.9

- Grafo de papers

- Stackoverflow + stackexchange (es un yahoo respuestas siglo 21, con subforos para todo lo que se te ocurra, con lo cuál podemos ver a usuarios en muchos contextos distintos).

**Visualizaciones**:

- https://preview.redd.it/mg9vjzibfuu21.png?width=960&crop=smart&auto=webp&s=a09bfd4c3132590ad9a791b045609a100ff45a12 

**Paper Familiar Strangers**
https://www.aaai.org/ocs/index.php/ICWSM/09/paper/viewPaper/184

**Propuestas de analisis**:

 ***En general***
- Community Detection en el grafo en cuestion (qué grafo?)

- Distribuión de grados

- Analizar un grafo dinamico en el tiempo? Un grafo por cada t=i

- Si vamos a hacer una presentación, podemos hacer que la intro sea el pulso de la ciudad. Re cheto.

- Coeficiente de clustering (ejemplo: qué estaciones son importantes en el grafo dirigido de estaciones? Estas deberían tener más bicicletas, tal vez.)

***En particular (¿qué grafos usamos?)***
- Inferencia sobre alguna caracteristica de los nodos (ejemplo genero)

- Hacer topological data analysis para ver la "forma" de los grafos.
- Estudiar el grafo cuyo nodo son las estaciones, y las aristas dirigidas con peso son, tal vez, la cantidad de bicicletas que fluyen (entran y salen).

Sarasa:
- Calcular la cantidad de bicicletas por estación a partir del flujo (a través del tiempo), haciendo que cada estación empiece en cero, y cada vez que hay un movimiento se lo cuenta. Update: ya tenemos info de cantidad de bicis y espacios vacíos.

- ¿Hay agentes invisibles del gobierno que mueven bicicletas sin estar registrados? ¿Se roban bicicletas? ¿Se agregan bicicletas sin registrarlas?

- Hacer un grafo bipartito (nodos = personas, nodos = estaciones), y luego proyectar

**Preguntas sueltas**

- ¿Hay gente que deja una bici y la vuelve a sacar por el límite de tiempo? ¿Cuántos, dónde?

- Mutual information: para comparar redes parecidas. Para ver cómo va cambiando la red a través del tiempo
