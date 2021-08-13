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
        float distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(otherParticle.getX() - this.x, 2) + Math.pow(otherParticle.getY() - this.y, 2) ) - otherParticle.getR() - this.getR());
        /*System.out.printf(otherParticle.toString());
        System.out.printf(this.toString());
        System.out.printf("dist: %f\n", distanceBetweenBounds);
         */
        return distanceBetweenBounds <= rc;
    }

    public boolean isNeighborPeriodic(Particle otherParticle, float rc, int flagX, int flagY, int boardLength){
        float newx, newy, distanceBetweenBounds;

        float oldx = otherParticle.getX();
        float oldy = otherParticle.getY();
        if(flagX==1 && flagY==1){
            newx = this.x + boardLength;
            newy = this.y + boardLength;
            distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(otherParticle.getX() - newx, 2) + Math.pow(otherParticle.getY() - newy, 2) ) - otherParticle.getR() - this.getR());
        } else if(flagX==1 && flagY==0) {
            newx = this.x + boardLength;
            distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(otherParticle.getX() - newx, 2) + Math.pow(otherParticle.getY() - this.y, 2) ) - otherParticle.getR() - this.getR());
        } else if(flagX==1 && flagY==-1){
            newx = this.x + boardLength;
            newy = otherParticle.getY() + boardLength;
            distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(otherParticle.getX() - newx, 2) + Math.pow(newy - this.y, 2) ) - otherParticle.getR() - this.getR());
        } else if(flagX==-1 && flagY==1){
            newx = otherParticle.getX() + boardLength;
            newy = this.y + boardLength;
            distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(newx - this.x, 2) + Math.pow(otherParticle.getY() - newy, 2) ) - otherParticle.getR() - this.getR());
        } else if(flagX==-1 && flagY==0){
            newx = otherParticle.getX() + boardLength;
            distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(newx - this.x, 2) + Math.pow(otherParticle.getY() - this.y, 2) ) - otherParticle.getR() - this.getR());
        } else if(flagX==-1 && flagY==-1){
            newx = otherParticle.getX() + boardLength;
            newy = otherParticle.getY() + boardLength;
            distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(newx - this.x, 2) + Math.pow(newy - this.y, 2) ) - otherParticle.getR() - this.getR());
        } else if(flagX==0 && flagY==1){
            newy = this.y + boardLength;
            distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(otherParticle.getX() - this.x, 2) + Math.pow(otherParticle.getY() - newy, 2) ) - otherParticle.getR() - this.getR());
        } else if(flagX==0 && flagY==-1){
            newy = otherParticle.getY() + boardLength;
            distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(otherParticle.getX() - this.x, 2) + Math.pow(newy - this.y, 2) ) - otherParticle.getR() - this.getR());
        } else {
            distanceBetweenBounds = (float) ((float) Math.sqrt(Math.pow(otherParticle.getX() - this.getX(), 2) + Math.pow(otherParticle.getY() - this.getY(), 2) ) - otherParticle.getR() - this.getR());
        }

        return distanceBetweenBounds <= rc;
    }

    public String toLAMMPS() {
        return String.format("%n %n", x, y);
    }

    public String toString() {
        //return String.format("(%f;%f)\n", this.x, this.y);
        return String.format("%d", this.id);
    }
}

