package tp1.bodies;

public class Particle{
    float x;
    float y;
    double r;
    public int id;

    public Particle(float xPos, float yPos, double radius, int idNum) {
        x = xPos;
        y = yPos;
        r = radius;
        id = idNum;
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
        System.out.printf("dist: %f", distanceBetweenBounds);
        return distanceBetweenBounds <= rc;
    }

    public String toLAMMPS() {
        return String.format("%n %n", x, y);
    }

    public String toString() {
        return String.format("(%n;%n;%n)", x, y, r);
    }
}