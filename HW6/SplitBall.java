import java.awt.Color;

public class SplitBall extends BasicBall{

    public SplitBall(double r, Color c, String type) {
        super(r,c, type);
    }

    public int getScore() {
    	return 10;
    }

}