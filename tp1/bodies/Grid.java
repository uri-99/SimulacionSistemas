import java.util;

public class Grid{
    int l, m;
    List<Particle> particles;
    Cells[][] grid;

    public Grid(int length, int mCantCells) {
        l = length; //10
        m = mCantCells; //20
        double size = l/m; //0.5
        int largo = 0;
        int ancho = 0;
        boolean last = false;

        grid = new Array[m][m]; //20*20
        for(double i = 0; i < m; i = i + size){
            for(double j = 0; j < m; j = j + size){
                if(j + size == m){
                    last = true;
                }
                grid[largo][ancho] = new Cell(i, i + size, j, j + size, last);
                ancho++;
                last = false;
            }
            largo++;
        }

    }

    public boolean addParticle(Particle particle){

        boolean flag=true;

        if(!particles.contains(particle)) {
            particles.add(particle);

            for(int i = 0; (i < m - 1) && flag; i = i++){
                for(int j = 0; (j < m - 1) && flag; j = j++){
                    flag = !grid[i][j].contains(particle);
                }
            }

            if(flag){
                println("no agregaste la particula a ningun cell");
            }

            return true;
        } else {
            return false;
        }
    }
    
    private void checkNeighboor(Cell cell) {
        for(Particle particle in cell.getParticles()) {
            
        }
    }

    public void exportToOvito() {

    }

}