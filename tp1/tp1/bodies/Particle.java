package tp1.bodies;

public class Particle{
    float x;
    float y;
    double r;

    public Particle(float xPos, float yPos, double radius) {
        x = xPos;
        y = yPos;
        r = radius;
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

    public boolean isInDistance(Particle particle, float distance) {
        float distanceBetweenBounds = Math.sqrt(
            (particle.getX() - this.getX())^2 +
            (particle.getY() - this.getY())^2
        ) - (particle.getR() - this.getR());
        return distance >= distanceBetweenBounds;
    }

    // en que formato guardamos las particulas?
    public String toFormat() {

    }

    public String toString() {
        return String.format("(%n;%n;%n)", x, y, r);
    }
}