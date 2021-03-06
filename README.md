# spiderman

Bienvenidos al README del proyecto SPIDERMAN.


(...)

*Borrador para nosotros*

**Posibles datasets**:

- Bicis -> https://data.buenosaires.gob.ar/dataset/bicicletas-publicas/archivo/22.9

- Grafo de papers

- Stackoverflow + stackexchange (es un yahoo respuestas siglo 21, con subforos para todo lo que se te ocurra, con lo cuál podemos ver a usuarios en muchos contextos distintos).

**Visualizaciones**:

- https://preview.redd.it/mg9vjzibfuu21.png?width=960&crop=smart&auto=webp&s=a09bfd4c3132590ad9a791b045609a100ff45a12 

- Ademas de las estaciones como puntos en el mapa, pensar una forma de unirlas (ejes) de forma tal que la red quede graficada sobre un layer (mapa dinamico o estatico). En este link hay un ejemplo con networkX y mplleaflet (https://stackoverflow.com/questions/19915266/drawing-a-graph-with-networkx-on-a-basemap)
Tambien se puede ver algo aca (http://www.sociology-hacks.org/?p=67)


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

- Usar topological data analysis (https://arxiv.org/abs/1707.04041) para predecir género (https://arxiv.org/abs/1101.3291) de las personas en base a patrones de movimiento de cada persona. Tal vez tratar de entender por qué se predice esto? Comparar topological data analysis con redes neuronales. Pensar otros grafos posibles para esto.
Alternativa: comparar data de distintos días/meses usando TDA para clasificar la data, por ejemplo, en días de paro y días de no paro.


Más sarasa:

Che, podríamos ver qué pasa los días de paro de transporte, y findes.
Para ver la evolucion en el tiempo podriamos ir poniendo fotos para ver una especie de pelicula.

**Marchas** (Autor: Billy)

- Fijar nodos, curvar edges isométricamente para visualización (con networkx). La curvatura es simplemente la fraccioon entre el promedio usual de tiempo de un día normal, y el del día de hoy.
- Que los ejes sean resortes de la longitud adecuada, y "soltamos" el grafo en R3. Cuando se estabiliza, idealmente aparece una superficie con montañitas en los lugares problemáticos. Si esto pasa, es útil para la visualización.
Si no, igual podemos pensar los nodos como un sample de una superficie (variedad) y estudiar la topología (que no cambió) y/o la curvatura. Ni idea cómo calcular la curvatura.

"N-spring, M-point mass system. Such a system can be modeled in terms of a set of N 2nd order linear differential equations and further expressed as a linear state space system. In linear systems theory the observability and contollability of the the state space system can be determined and given the availability of sensors and actuators and synthesis of control laws, the ability to stabilize and control the object. These techniques are largely described under the discipline of control system engineering"

Temas de curvatura tal vez aparezcan en el campo PLANARIDAD (ver Knuth).
Tal vez también en multidimensional scaling:

Given a distance matrix with the distances between each pair of objects in a set, and a chosen number of dimensions, N, an MDS algorithm places each object into N-dimensional space such that the between-object distances are preserved as well as possible. If N is one or two, then 2D scatter plots of the resulting points are possible

Ver también https://towardsdatascience.com/why-is-ayasdi-topological-data-analyses-the-source-of-so-many-breakthroughs-in-science-5fdc6b8a6f57 (TDA)

y esto, por dios: https://people.clas.ufl.edu/peterbubenik/intro-to-tda/
