import java.awt.Color;

public class ShrinkBall extends BasicBall{

    public double initialR;
    public ShrinkBall(double r, Color c, String type) {
        super(r,c, type);
        initialR = r;
    }

    public int reset() {
        rx = 0.0;
        ry = 0.0; 	
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        radius *= (0.66);
        double check = initialR * (0.25);
        if (radius <= check){
            radius = initialR;
        }
        return 1;
    }

    public int getScore() {
    	return 20;
    }
}