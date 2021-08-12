package tp1.bodies;

import java.util.ArrayList;
import java.util.List;

public class Particle{
    float x;
    float y;
    double r;
    public int id;
    public List<Particle> neighbors;

    public Particle(float xPos, float yPos, double radius, int idNum) {
        x = xPos;
        y = yPos;
        r = radius;
        id = idNum;
        this.neighbors = new ArrayList<>();
    }

    public float getX(){
        return x;
    }

    public float getY(){
        return y;
    }

    public double getR(){
        return r;
    }

    public boolean isNeighbor(Particle otherParticle, float rc) {
        float distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(otherParticle.getX() - this.getX(), 2) + Math.pow(otherParticle.getY() - this.getY(), 2) ) - (otherParticle.getR() - this.getR()));
        /*System.out.printf(otherParticle.toString());
        System.out.printf(this.toString());
        System.out.printf("dist: %f\n", distanceBetweenBounds);
         */
        return distanceBetweenBounds <= rc;
    }


/*
    // en que formato guardamos las particulas?
    public String toFormat() {

    }
    */

    public String toString() {
        //return String.format("(%f;%f)\n", this.x, this.y);
        return String.format("%d", this.id);
    }
}