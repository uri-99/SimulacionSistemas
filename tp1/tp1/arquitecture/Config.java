package tp1.arquitecture;

import tp1.bodies.Grid;
import tp1.bodies.Particle;

import java.util.Arrays;

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
        grid = new Grid(l, m); //nuevo plano y grilla con los datos pasados
        int i=0;
        while(i<n){ //genero las n particulas
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
        System.out.printf("particle generated: x:%f  y:%f\n", x, y);
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
                        System.out.printf(".");
                    }
                }
            }
            System.out.printf("\n");
        }
        return "printed";
    }
}

/*
|----------|
|       .  |
| .        |
|          |
|    .     |
|          |
|          |
|   .      |
|          |
|          |
|       .  |
|----------|
 */
