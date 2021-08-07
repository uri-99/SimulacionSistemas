import java.lang.Math;

public class Config{
    int n, m, l:
    float rc;
    Grid grid;

    public Config(int cantParticulas, int matrix, int planeLength, float radioInteracción) {
        n = cantParticulas;
        m = matrix;
        l = planeLength;
        rc = radioInteracción;
        grid = new Grid(l, m);

        int i=0;
        while(i<n){
            if(grid.addParticle(generateParticle())) {
                i++;
            }
        }
    }

    public particle generateParticle(){
        float x = (float)(Math.random() * l);
        float y = (float)(Math.random() * l);
        float r = (float)(Math.random() * 0.025) + 0.25;
        
        Particle newParticle = new Particle(x, y, r);
        return newParticle;
    }
}