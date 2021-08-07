public class Cell{
    int xMin;
    int xMax;
    int yMin;
    int yMax;
    boolean lastCell;

    List<Particle> particles;
    
    public Cell(int x1, int x2, int y1, int y2, boolean last) {
        xMin = x1;
        xMax = x2;
        yMin = y1;
        yMax = y2;
        lastCell = last;
        particles = new ArrayList();
    }

    public boolean contains(Particle particle){
        float x = particle.getX;
        float y = particle.getY;
        
        if(lastCell){
            if(x => xMin  &&  x <= xMax  &&  y> = yMin  &&  y <= yMax)
            {
                particles.add(particle);
                return true;
            }
        } else {
            if(x => xMin  &&  x < xMax  &&  y> = yMin  &&  y < yMax)
            {
                particles.add(particle);
                return true;
            }
        }
        return false;
    }
}