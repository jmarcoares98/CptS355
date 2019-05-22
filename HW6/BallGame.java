/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;

public class BallGame { 
    public static void main(String[] args) {
  
    	// number of bouncing balls
    	int numBalls = Integer.parseInt(args[0]);
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
        double ballSizes[] = new double[numBalls];
        // number of bounces
        int numBounces = 0;
        boolean isSplit = false;
        double splitRadius = 0;
        Color splitColor = Color.WHITE;
        String splitType = "";
    	
    	//retrieve ball types
    	int index = 1;
    	for (int i=0; i<numBalls; i++) {
    		ballTypes[i] = args[index];
    		index = index+2;
    	}
    	//retrieve ball sizes
    	index = 2;
    	for (int i=0; i<numBalls; i++) {
    		ballSizes[i] = Double.parseDouble(args[index]);
    		index = index+2;
    	}
     
        //TO DO: create a Player object and initialize the player game stats.  
        Player player = new Player();

    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        // create colored balls 
        //TO DO: Create "numBalls" balls (of types given in "ballTypes" with sizes given in "ballSizes") and store them in an Arraylist
        ArrayList<BasicBall> arrBall = new ArrayList<BasicBall>(numBalls);

        for(int k = 0; k < numBalls; k++){
            if(ballTypes[k].equals("bas.ic")){
                BasicBall basic = new BasicBall(ballSizes[k],Color.RED, ballTypes[k]);
                arrBall.add(basic);
            }
            else if(ballTypes[k].equals("bounce")){
                BounceBall bounce = new BounceBall(ballSizes[k], Color.BLUE, ballTypes[k], numBounces);
                arrBall.add(bounce);
            }
            else if(ballTypes[k].equals("shrink")){
                ShrinkBall shrink = new ShrinkBall(ballSizes[k], Color.GREEN, ballTypes[k]); 
                arrBall.add(shrink);
            }
            else if(ballTypes[k].equals("split")){
                SplitBall split = new SplitBall(ballSizes[k], Color.YELLOW, ballTypes[k]);
                arrBall.add(split);
            }
            else{
                continue;
            }
        } 
        
        // gets the numbers of balls from the size of the arrList
        numBallsinGame = arrBall.size();

        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {
            // TO DO: move all balls
            for(int h = 0; h < numBalls; h++){
                arrBall.get(h).move();
            }

            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();

                for(int g = 0; g < numBallsinGame; g++){
                    if(arrBall.get(g).isHit(x,y)){
                        if(arrBall.get(g).getType().equals("split")){
                            isSplit = true;
                            splitRadius = arrBall.get(g).getRadius();
                            splitColor = arrBall.get(g).getColor();
                            splitType = arrBall.get(g).getType();
                        }
                        arrBall.get(g).reset();
                        player.addScore(arrBall.get(g).getScore());
                        player.isHit();
                    }
                }

                if(isSplit == true){
                    SplitBall split2 = new SplitBall(splitRadius, splitColor, splitType);
                    arrBall.add(split2);
                    numBallsinGame++;
                    numBalls++;
                    isSplit = false;
                }
                
                int basicC = 0;
                int bounceC = 0;
                int shrinkC = 0;
                int splitC = 0;
                //checks the most popular ball
                for(int d = 0; d < numBalls ; d++){
                    switch(arrBall.get(d).getType()){
                        case "basic": basicC += arrBall.get(d).getHits();
                            break;
                        case "bounce": bounceC += arrBall.get(d).getHits();
                            break;
                        case "shrink": shrinkC += arrBall.get(d).getHits();
                            break;
                        case "split": splitC += arrBall.get(d).getHits();
                            break; 
                    }
                }
                if(basicC > bounceC && basicC > shrinkC && basicC >shrinkC){
                    player.setType("Basic Ball");
                }
                else if(bounceC > basicC && bounceC > shrinkC && bounceC > splitC){
                    player.setType("Bounce Ball");
                }
                else if(shrinkC > basicC && shrinkC > bounceC && shrinkC > splitC){
                    player.setType("Shrink Ball");
                }
                else if(splitC > basicC && splitC > bounceC && splitC > shrinkC){
                    player.setType("Split Ball");
                }
            }
                
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.MAGENTA);
            StdDraw.setPenColor(StdDraw.BLACK);

            //check each ball and see if they are still visible. numBallsinGame should hold the number of visible balls in the game. 
            for(int f = 0; f < numBalls; f++)
            {
                if(arrBall.get(f).isOut == false)
                {
                    arrBall.get(f).draw();
                    numBallsinGame++;
                }
            } 
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.55, 0.70, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            StdDraw.text(-0.55, 0.65, "Player Score: " + String.valueOf(player.getScore()));
            StdDraw.text(-0.55, 0.60,"Player Hits: : "+ String.valueOf(player.getHits()));
            StdDraw.text(-0.55, 0.55, "Popular Ball: " + String.valueOf(player.getBallType()));
            //TO DO: print the rest of the player statistics

            StdDraw.show();
            StdDraw.pause(20);
        }

        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            //TO DO: print the rest of the player statistics
            StdDraw.text(0, -0.15, "Player Score: " + String.valueOf(player.getScore()));
            StdDraw.text(0, -0.30, "Player Hits: " + String.valueOf(player.getHits()));
            StdDraw.text(0, -0.45, "Popular Ball: " + String.valueOf(player.getBallType()));
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}
