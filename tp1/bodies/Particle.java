

public class Particle{
    float x;
    float y;
    float r;

    public Particle(float xPos, float yPos, float radius) {
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

    public float getR(){
        return r;
    }

    public boolean isInDistance(Particle particle, float distance) {
        float distanceBetweenBounds = Math.sqrt(
            (particle.getX() - this.particle.getX())^2 +
            (particle.getY() - this.particle.getY())^2
        ) - (particle.getR() - this.particle.getR());
        return distance >= distanceBetweenBounds;
    }

    // en que formato guardamos las particulas?
    public String toFormat() {

    }
}