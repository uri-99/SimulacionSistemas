package tp1.arquitecture;
import java.io.FileWriter;
import java.io.IOException;

import tp1.bodies.Grid;
import tp1.bodies.Particle;

import java.util.Arrays;
import java.util.List;

import static java.lang.Math.*;

public class Config{
    int n, m, l, id=1;
    float rc;
    public Grid grid;

    public Config(String cantParticulas, String matrix, String planeLength, String radioInteraccion) {

        n = Integer.parseInt(cantParticulas);
        m = Integer.parseInt(matrix);
        l = Integer.parseInt(planeLength);
        rc = Float.parseFloat(radioInteraccion);
        grid = new Grid(l, m, rc); //nuevo plano y grilla con los datos pasados

        while(id<n+1){ //genero las n particulas, id arranca en 1 y se usa para el nombre de la particula
            if(grid.addParticle(generateParticle())) {
                id++;
            }
        }
    }

    public Particle generateParticle(){
        float x = (float)(Math.random() * l);
        float y = (float)(Math.random() * l);
        double r = (double)(Math.random() * 0.25) + 0.25;
        
        Particle newParticle = new Particle(x, y, r, id);
        //System.out.printf("particle generated: x:%f  y:%f\n", x, y);
        return newParticle;
    }

    public String toString() {
        String visualGrid[][] = new String[l+2][l+2];
        for(int i=0; i<l+2; i++){
            for(int j=0; j<l+2; j++){
                if(j==0 || j==l+1){
                    visualGrid[i][j] = "|";
                    System.out.printf("|");
                } else if(i==0 || i==l+1){
                    visualGrid[i][j] = "-";
                    System.out.printf("-");
                } else {
                    if(grid.grid[i-1][j-1].particles.isEmpty()){
                        visualGrid[i][j] = " ";
                        System.out.printf(" ");
                    } else {
                        System.out.printf("%d",grid.grid[i-1][j-1].particles.get(0).id);
                    }
                }
            }
            System.out.printf("\n");
        }
        return "printed";
    }

    public void exportToLAMMPSFile(String filename, int selectedID) {
        List<Particle> auxNeighbors = null;

        for(Particle particle : this.grid.particles){
            if(particle.id == selectedID)
            auxNeighbors = particle.neighbors;
        }

        try {
            FileWriter myWriter = new FileWriter(filename);
            myWriter.write(String.format("%b\n", this.grid.periodic));
            myWriter.write(String.format("%s\n", this.n));
            myWriter.write(String.format("%d\n%d\n%f", this.l, this.m, this.rc));

            for(Particle particle : this.grid.particles){
                myWriter.write(String.format("\n%d %f %f %f ", particle.id, particle.getX(), particle.getY(), particle.getR()));
                for(Particle neighbor : particle.neighbors){
                    myWriter.write(String.format("%d,", neighbor.id));
                }
                //myWriter.write(String.format("%s\n", particle.neighbors.toString()));

                /*
                if(particle.id == selectedID) {
                    myWriter.write("1 0 0\n");
                    auxNeighbors = particle.neighbors;
                } else if (auxNeighbors.contains(particle)) {
                    myWriter.write("0 1 0\n");
                } else {
                    myWriter.write("0 0 1\n");
                }
                 */
            }
            myWriter.close();
            System.out.println("Se creo el archivo.");
        } catch (IOException e) {
            System.out.println("Error al crear el archivo");
            e.printStackTrace();
        }
    }

    /*
    public void exportToMatplot() {
        List<Particle> auxNeighbors = null;

        for(Particle particle : this.grid.particles){
            if(particle.id == selectedID)
                auxNeighbors = particle.neighbors;
        }

        try {
            FileWriter particleWriter = new FileWriter("particles");
            FileWriter interactionWriter = new FileWriter("interaction");
            FileWriter configWriter = new FileWriter("config");configWritter.write()String.format()"%"%s,  %s %s %s. , n, m, l, rc;

            for(Particle particle : this.grid.particles){
                myWriter.write(String.format("%d %f %f 0 %f ", particle.id, particle.getX(), particle.getY(), particle.getR()));

                if(particle.id == selectedID) {
                    myWriter.write("1 0 0\n");
                    auxNeighbors = particle.neighbors;
                } else if (auxNeighbors.contains(particle)) {
                    myWriter.write("0 1 0\n");
                } else {
                    myWriter.write("0 0 1\n");
                }

            }

            myWriter.close();
            System.out.println("Se creo el archivo.");
        } catch (IOException e) {
            System.out.println("Error al crear el archivo");
            e.printStackTrace();
        }
*/
}
