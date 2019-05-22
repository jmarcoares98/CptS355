import java.awt.Color;

public class BounceBall extends BasicBall{

    public int numBounces;
    public BounceBall(double r, Color c, String type, int bounces) {
        super(r,c, type);
        numBounces = bounces;
    }

    public void move() {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) 
            if(numBounces >= 3){
                isOut = true;
            }
            // where it will bounce
            else if (numBounces < 3){
                // left down wall
                if((rx < -1.0) && (ry < 0)){
                    vx = Math.abs(vx);
                    vy = StdRandom.uniform(-0.01, 0);
                    rx = rx + vx;
                    ry = ry + vy;
                    numBounces++;
                }
                //left up wall
                else if((rx < -1.0) && (ry > 0)){
                    vx = Math.abs(vx);
                    vy = StdRandom.uniform(0, 0.01);
                    rx = rx + vx;
                    ry = ry + vy;
                    numBounces++;
                }
                //right down wall
                else if((rx > 1.0) && (ry < 0)){
                    vx = -vx;
                    vy = StdRandom.uniform(-0.01, 0);
                    rx = rx + vx;
                    ry = ry + vy;
                    numBounces++;
                }
                //right up wall
                else if((rx > 1.0) && (ry > 0)){
                    vx = -vx;
                    vy = StdRandom.uniform(0, 0.01);
                    rx = rx + vx;
                    ry = ry + vy;
                    numBounces++;
                }
                //up left wall
                else if((rx < 0) && (ry > 1.0)){
                    vx = StdRandom.uniform(-0.01, 0);
                    vy = -vy;
                    rx = rx + vx;
                    ry = ry + vy;
                    numBounces++;
                }
                //up right wall
                else if((rx > 0) && (ry > 1.0)){
                    vx = StdRandom.uniform(0, 0.01);
                    vy = -vy;
                    rx = rx + vx;
                    ry = ry + vy;
                    numBounces++;
                }
                //down left wall
                else if((rx < 0) && (ry < -1.0)){
                    vx = StdRandom.uniform(-0.01, 0);
                    vy = Math.abs(vy);
                    rx = rx + vx;
                    ry = ry + vy;
                    numBounces++;
                }
                //down right wall
                else if((rx > 0) && (ry < -1.0)){
                    vx = StdRandom.uniform(0, 0.01);
                    vy = Math.abs(vy);
                    rx = rx + vx;
                    ry = ry + vy;
                    numBounces++;
                }
            }
    }

    public int getScore() {
    	return 15;
    }
}