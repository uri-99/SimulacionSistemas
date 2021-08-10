package tp1.bodies;

import java.util.*;

public class Grid{
    int l, m;
    List<Particle> particles;
    public Cell[][] grid;
    float rc;

    public Grid(int length, int mCantCells, float radioInteracicion) {
        rc=radioInteracicion;
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
            //System.out.println("particle added to gridList");

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

    public void bruteForce(){
        System.out.println("\nSTART BRUTE FORCE--------------\n");
        for (Particle particle1: particles) {
           // System.out.printf("\nmirando id: %d\n", particle1.id);
            for(Particle particle2: particles) {
                //System.out.printf("\tsubid: %d\n", particle2.id);
                if(particle1.id < particle2.id && particle1.isNeighbor(particle2, rc)) {
                    System.out.printf("\n%d es vecina de %d\n", particle1.id, particle2.id);
                    System.out.printf("\n%d es vecina de %d\n", particle2.id, particle1.id);
                }
            }
        }
        System.out.println("\nEND BRUTE FORCE----------------\n");
    }

    public void CIM(){
        System.out.println("\nSTAART CIM--------------\n");
        Cell celda, aux = null;
        for(int x=0; x<m; x++){
            for(int y=0; y<m; y++){
                celda = grid[x][y];
               // System.out.printf("celda[%d][%d]\n",x,y);
                for(int a=0; a<3; a++){ //X
                    for(int b=0; b<3; b++){ //Y
                        if(a==0 && b==0){ //0 es +0, 1 es +1, 2 es -1
                                aux = grid[x][y];
                              //  System.out.printf("\taux[%d][%d]\n", x, y);
                        } else if (a==0 && b==1){
                            if(y<m-1) {
                                aux = grid[x][y + 1];
                              //  System.out.printf("\taux[%d][%d]\n", x, y+1);
                            }
                        } else if (a==0 && b==2){
                            if(y>0) {
                                aux = grid[x][y - 1];
                              //  System.out.printf("\taux[%d][%d]\n", x, y-1);
                            }
                        } else if (a==1 && b==0){
                            if(x<m-1) {
                                aux = grid[x + 1][y];
                              //  System.out.printf("\taux[%d][%d]\n", x+1, y);
                            }
                        } else if (a==1 && b==1){
                            if(x<m-1 && y<m-1) {
                                aux = grid[x + 1][y + 1];
                              //  System.out.printf("\taux[%d][%d]\n", x+1, y+1);
                            }
                        } else if (a==1 && b==2){
                            if(x<m-1 && y>0) {
                                aux = grid[x + 1][y - 1];
                               // System.out.printf("\taux[%d][%d]\n", x+1, y-1);
                            }
                        } else if (a==2 && b==0){
                            if(x>0) {
                                aux = grid[x - 1][y];
                               // System.out.printf("\taux[%d][%d]\n", x-1, y);
                            }
                        } else if (a==2 && b==1){
                            if(x>0 && y<m-1) {
                                aux = grid[x - 1][y + 1];
                               // System.out.printf("\taux[%d][%d]\n", x-1, y+1);
                            }
                        } else if (a==2 && b==2){
                            if(x>0 && y>0) {
                                aux = grid[x - 1][y - 1];
                                //System.out.printf("\taux[%d][%d]\n", x-1, y-1);
                            }
                        }

                        for(Particle particle1 : celda.particles){
                          //  System.out.printf("\n\nmirando particula %d en celda[%d][%d]", particle1.id,x,y);
                            for(Particle particle2 : aux.particles){
                               // System.out.printf("\n\tla comparo con particula %d en aux[][]", particle2.id);
                                if(particle1.id < particle2.id && particle1.isNeighbor(particle2, rc)) {
                                    System.out.printf("\n%d es vecinaa de %d", particle1.id, particle2.id);
                                    System.out.printf("\n%d es vecinaa de %d\n", particle2.id, particle1.id);
                                }
                            }
                        }

                    }
                }
            }
        }
        System.out.println("\nEND CIM-----------------\n");
    }
    


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