package tp1.bodies;

import java.util.*;

public class Grid{
    int l, m;
    List<Particle> particles;
    public Cell[][] grid;

    public Grid(int length, int mCantCells) {
        particles = new LinkedList<Particle>();
        l = length; //10
        m = mCantCells; //4
        double size = (double)l/(double)m; //2.5
        int largo = 0;
        int ancho = 0;
        boolean lastX = false;
        boolean lastY = false;

        grid = new Cell[m][m]; //20*20

        for(int i=0; i<m; i++) {
            for(int j=0; j<m; j++) {
                if(j==m)
                    lastY=true;
                grid[i][j] = new Cell(i*size, (i+1)*size, j*size, (j+1)*size, lastX, lastY);
            }
            lastY=false;
            if(i==m)
                lastX=true;
        }

        /*for(double i = 0; i < m; i = i + size){
            for(double j = 0; j < m; j = j + size){
                if(j + size == m){
                    last = true;
                }
                grid[largo][ancho] = new Cell(i, i + size, j, j + size, last);
                ancho++;
                last = false;
            }
            largo++;
        }*/

        System.out.println("grid generated");
        for(int ii=0; ii<m; ii++){
            for(int jj=0; jj<m; jj++){
                System.out.println(grid[ii][jj]);
            }
        }

    }

    public boolean addParticle(Particle particle){

        boolean flag=true;

        if(!particles.contains(particle)) {
            //if(checkProximity(particle)){
            //    return false;
            //}
            particles.add(particle);
            System.out.println("particle added to gridList");

            for(int i = 0; (i < m) && flag; i++){ //le agrego la particle a la cellList apropiada
                for(int j = 0; (j < m) && flag; j++){
                    flag = !grid[i][j].contains(particle);
                }
            }

            if(flag){
                System.out.println("no agregaste la particula a ninguna cell");
            }

            return true;
        } else {
            return false;
        }
    }

    /*
    private boolean checkProximity(Particle particle){
        boolean chocan = false;
        for(int i = 0; i < particles.size() && !chocan; i++){
            chocan = particle.isInDistance(particles.get(i), 0);
        }
        return chocan;
    }
    

    private void checkNeighboor(Cell cell) {
        for(Particle particle in cell.getParticles()) {
            
        }
    }

    public void exportToOvito() {

    }
 */


    public String toString() {
        StringBuilder data = new StringBuilder();
        data.append("Grid: ");
        for(int i=0; i<m; i++) {
            for(int j=0; j<m; j++) {
                data.append(grid[i][j].toString());
            }
        }
        return data.toString();
    }
}