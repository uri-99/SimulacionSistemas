package tp1.arquitecture;

import tp1.bodies.Grid;
import tp1.bodies.Particle;

import static java.lang.Math.*;

public class Config{
    int n, m, l;
    float rc;
    Grid grid;

    public Config(String cantParticulas, String matrix, String planeLength, String radioInteraccion) {

        n = Integer.parseInt(cantParticulas);
        m = Integer.parseInt(matrix);
        l = Integer.parseInt(planeLength);
        rc = Float.parseFloat(radioInteraccion);
        grid = new Grid(l, m);

        int i=0;
        while(i<n){
            if(grid.addParticle(generateParticle())) {
                i++;
            }
        }
    }

    public Particle generateParticle(){
        float x = (float)(Math.random() * l);
        float y = (float)(Math.random() * l);
        double r = (double)(Math.random() * 0.025) + 0.25;
        
        Particle newParticle = new Particle(x, y, r);
        return newParticle;
    }

    public String toString() {
        return grid.toString();
    }
}