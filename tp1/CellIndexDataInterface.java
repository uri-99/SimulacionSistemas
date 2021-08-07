/*
Implementar el algoritmo "Cell Index Method" que tome como inputs: las posiciones y radios de
las N partículas y los parámetros N, L, M y rc (ver punto 5):
N (Heading con el Nro. total de Partículas) 
L (Longitud del lado del área de simulación)
M*M cantidad de celdas
rc radio de las particulas

y cuyos outputs sean:
- Una lista tal que para cada partícula indique cuales son las vecinas que distan menos de rc.
- El tiempo de ejecución.
- Además se debe generar una figura que muestre las posiciones de todas las partículas, y que
identifique una de ellas (pasada como input) de un color y sus vecinos correspondientes de otro
color.
*/
public interface CellIndex {
    public void cellIndex(Particles[] particles, int N, int L, int M, int rc);
}