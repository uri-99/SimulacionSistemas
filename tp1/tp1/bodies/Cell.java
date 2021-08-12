package tp1.bodies;

import java.util.*;

public class Cell{
    double xMin, xMax;
    double yMin, yMax;
    boolean lastXcell, lastYcell;

    public List<Particle> particles;
    
    public Cell(double x1, double x2, double y1, double y2, boolean lastX, boolean lastY) {
        xMin = x1;
        xMax = x2;
        yMin = y1;
        yMax = y2;
        lastXcell = lastX;
        lastYcell = lastY;
        particles = new LinkedList<Particle>();
    }


    public boolean contains(Particle particle){
        float x = particle.getX();
        float y = particle.getY();
/*
        if(lastXcell){
            if(lastYcell){
                if(x >= xMin  &&  x <= xMax  &&  y >= yMin  &&  y <= yMax)
                {
                    particles.add(particle);
                    System.out.println("particle added in cell list");
                    return true;
                }
            } else {
                if(x >= xMin  &&  x <= xMax  &&  y >= yMin  &&  y < yMax)
                {
                    particles.add(particle);
                    System.out.println("particle added in cell list");
                    return true;
                }
            }

        } else {
            if(lastYcell){
                if(x >= xMin  &&  x < xMax  &&  y >= yMin  &&  y <= yMax)
                {
                    particles.add(particle);
                    System.out.println("particle added in cell list");
                    return true;
                }
            } else {
                if(x >= xMin  &&  x < xMax  &&  y >= yMin  &&  y < yMax)
                {
                    particles.add(particle);
                    System.out.println("particle added in cell list");
                    return true;
                }
            }
        }
        */
        if(x > xMin && x<xMax && y>yMin && y<yMax){
            particles.add(particle);
            //System.out.println("particle added in cell list: ");
            //System.out.printf("x entre:%f y %f, y entre: %f y %f\n", xMin, xMax, yMin, yMax);
            return true;
        }
        //System.out.println("particle not added in this cell list");
        return false;

        /*
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
        */
    }


    public String toString() {

        StringBuilder data = new StringBuilder();
        data.append("Celda:  xmax:");
        data.append(xMax);
        data.append("  ymax:");
        data.append(yMax);
        for(Particle particle : particles) {
            data.append(particle.toString());
        }

        //return data.toString();
        return ".";
    }
    public String toLAMMPS() {
        StringBuilder data = new StringBuilder();
        for(Particle particle : particles) {
            data.append(String.format("%s\n", particle.toLAMMPS()));
        }
        return data.toString();
    }
}