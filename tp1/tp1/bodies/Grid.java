package tp1.bodies;

import java.util.*;

public class Grid{
    int l, m;
    public List<Particle> particles;
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
        //System.out.println("grid generated");
    }

    public List<Particle> getParticles() {
        return particles;
    }

    public boolean addParticle(Particle newParticle){

        boolean flag=true;

        if(checkProximity(newParticle)){
            return false;
        }

        particles.add(newParticle);

        for(int i = 0; (i < m) && flag; i++){ //le agrego la particle a la cellList apropiada
            for(int j = 0; (j < m) && flag; j++){
                flag = !grid[i][j].contains(newParticle);
            }
        }

        if(flag){
            System.out.println("no agregaste la particula a ninguna cell");
            particles.remove(particles.size()-1);
            return false;
        }

        return true;
    }


    private boolean checkProximity(Particle newParticle){
        boolean chocan = false;

        for(Particle particleIter : particles){
            if(particleIter.isNeighbor(newParticle, 0))
                chocan = true;
        }

/*
        for(int i = 0; i < particles.size() && !chocan; i++){
            chocan = newParticle.isNeighbor(particles.get(i), 0);
        }*/


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

    public void bruteForce(){
        System.out.println("\nSTART BRUTE FORCE--------------\n");
        for (Particle particle1: particles) {
           // System.out.printf("\nmirando id: %d\n", particle1.id);
            for(Particle particle2: particles) {
                //System.out.printf("\tsubid: %d\n", particle2.id);
                if(particle1.id < particle2.id && particle1.isNeighbor(particle2, rc)) {
                    //System.out.printf("\n%d es vecina de %d\n", particle1.id, particle2.id);
                    //System.out.printf("\n%d es vecina de %d\n", particle2.id, particle1.id);
                }
            }
        }
        System.out.println("\nEND BRUTE FORCE----------------\n");
    }

    // Sin condiciones periódicas de contorno
    public void CIM(){
        System.out.println("\nSTART CIM--------------\n");
        Cell celda, aux;
        int a2, b2;

        for(int x=0; x<m; x++){
            for(int y=0; y<m; y++){
                celda = grid[x][y];
               // System.out.printf("celda[%d][%d]\n",x,y);
                for(int a=-1; a<2; a++){ //X
                    for(int b=-1; b<2; b++){ //Y
                        if (x+a>-1 && x+a<m) {
                            a2 = x+a;
                        } else {
                            continue;
                        }

                        if (y+b>-1 && y+b<m) {
                            b2 = y+b;
                        } else {
                            continue;
                        }
                        aux = grid[a2][b2];

                        for(Particle particle1 : celda.particles){
                            //System.out.printf("\n\nmirando particula %d en celda[%d][%d]", particle1.id,x,y);
                            for(Particle particle2 : aux.particles){
                                //System.out.printf("\n\tla comparo con particula %d en aux[][]", particle2.id);
                                if(particle1.id < particle2.id && particle1.isNeighbor(particle2, rc)) {
                                    //System.out.printf("\n%d es vecinaa de %d", particle1.id, particle2.id);
                                    //System.out.printf("\n%d es vecinaa de %d\n", particle2.id, particle1.id);
                                    particle1.neighbors.add(particle2);
                                    particle2.neighbors.add(particle1);
                                }
                            }
                        }

                    }
                }
            }
        }
        System.out.println("\nEND CIM-----------------\n");
    }

    // Con condiciones periódicas de contorno.
    public void CIMP(){
        System.out.println("\nSTART CIMP--------------\n");
        Cell celda, aux;
        int a2, b2;

        for(int x=0; x<m; x++){
            for(int y=0; y<m; y++){
                celda = grid[x][y];
                // System.out.printf("celda[%d][%d]\n",x,y);
                for(int a=-1; a<2; a++){ //X
                    for(int b=-1; b<2; b++){ //Y
                        if (x+a>-1 && x+a<m) {
                            a2 = x+a;
                        } else if(x+a==-1){
                            a2=m-1;
                        } else if(x+a==m) {
                            a2=0;
                        } else {
                            a2=-69;
                        }

                        if (y+b>-1 && y+b<m) {
                            b2 = y+b;
                        } else if(y+b==-1){
                            b2=m-1;
                        } else if(y+b==m) {
                            b2=0;
                        } else {
                            b2=-420;
                        }

                        aux = grid[a2][b2];

                        for(Particle particle1 : celda.particles){
                            //System.out.printf("\n\nmirando particula %d en celda[%d][%d]", particle1.id,x,y);
                            for(Particle particle2 : aux.particles){
                                //System.out.printf("\n\tla comparo con particula %d en aux[][]", particle2.id);
                                if(particle1.id < particle2.id && particle1.isNeighbor(particle2, rc)) {
                                    //System.out.printf("\n%d es vecinaa de %d", particle1.id, particle2.id);
                                    //System.out.printf("\n%d es vecinaa de %d\n", particle2.id, particle1.id);
                                    particle1.neighbors.add(particle2);
                                    particle2.neighbors.add(particle1);
                                }
                            }
                        }

                    }
                }
            }
        }
        System.out.println("\nEND CIMP-----------------\n");
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

    public String toLAMMPS() {
        StringBuilder data = new StringBuilder();
        for(int i=0; i<m; i++) {
            for(int j=0; j<m; j++) {
                data.append(grid[i][j].toLAMMPS());
            }
        }
        return data.toString();
    }
}