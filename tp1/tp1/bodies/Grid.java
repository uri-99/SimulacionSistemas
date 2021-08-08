package tp1.bodies;

import java.util.*;

public class Grid{
    int l, m;
    List<Particle> particles;
    Cell[][] grid;

    public Grid(int length, int mCantCells) {
        l = length; //10
        m = mCantCells; //20
        double size = l/m; //0.5
        int largo = 0;
        int ancho = 0;
        boolean last = false;

        grid = new Cell[m][m]; //20*20
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
            if(checkProximity(particle)){
                return false;
            }
            particles.add(particle);

            for(int i = 0; (i < m - 1) && flag; i = i++){
                for(int j = 0; (j < m - 1) && flag; j = j++){
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

    private boolean checkProximity(Particle particle){
        boolean chocan = false;
        for(int i = 0; i < particles.size() && !chocan; i++){
            chocan = particle.isInDistance(particles.get(i), 0);
        }
        return chocan;
    }
    
    /*
    private void checkNeighboor(Cell cell) {
        for(Particle particle in cell.getParticles()) {
            
        }
    }

    public void exportToOvito() {

    }
    */

    public String toString() {
        StringBuilder data = new StringBuilder();
        for(int i=0; i<m; i++) {
            for(int j=0; j<m; j++) {
                data.append(grid[i][j].toString());
            }
        }
        return data.toString();
    }
}