public class Player
{
    private int numHits;
    private int pScore;
    private String ballType; 

    // Constructor for Player
    public Player()
    {
        pScore = 0;
        numHits = 0;
        ballType = "";
    }

    // get number of hits
    public int getHits()
    {
        return numHits;
    }

    public int isHit()
    {
        return numHits += 1;
    }

    // gets score
    public int getScore()
    {
        return this.pScore;
    }

    //returns the popular ball
    public String getBallType()
    {
        return this.ballType;
    }

    public void setType(String ball)
    {
        ballType = ball;
    }

    // add score
    public void addScore(int add)
    {
        pScore += add;
    }
}