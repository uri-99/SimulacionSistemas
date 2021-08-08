package tp1.bodies;

import java.util.*;

public class Cell{
    double xMin;
    double xMax;
    double yMin;
    double yMax;
    boolean lastCell;

    List<Particle> particles;
    
    public Cell(double x1, double x2, double y1, double y2, boolean last) {
        xMin = x1;
        xMax = x2;
        yMin = y1;
        yMax = y2;
        lastCell = last;
        particles = new ArrayList();
    }

    public boolean contains(Particle particle){
        float x = particle.getX();
        float y = particle.getY();
        
        if(lastCell){
            if(x >= xMin  &&  x <= xMax  &&  y >= yMin  &&  y <= yMax)
            {
                particles.add(particle);
                return true;
            }
        } else {
            if(x >= xMin  &&  x < xMax  &&  y >= yMin  &&  y < yMax)
            {
                particles.add(particle);
                return true;
            }
        }
        return false;
    }

    public String toString() {
        StringBuilder data = new StringBuilder("Celda: ");
        for(Particle particle : particles) {
            data.append(particle.toString());
        }
        return data.toString();
    }
}