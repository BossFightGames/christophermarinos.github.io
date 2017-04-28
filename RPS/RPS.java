// Program: Rock Paper Scissors
// Written by: Chris Marinos
// Description: plays rock paper scissors
// Challenges: none
// Time Spent: twenty minutes
// Given Input:  player: rock computer: scissors                Expected Output: player wins
// player: paper computer: rock                                 output: player wins
// player: scissors computer: scissors                          output: tie
//
//
//
//
//
//                                                  
// --------------------          -------------------------
//                   Revision History
// Date: 7/25/14                  By:  chris m             Action:
// ---------------------------------------------------
//                        CPM                Created







import java.util.Random;
import javax.swing.JOptionPane;



public class RPS extends JOptionPane {//open class
	//all static methods means this class can be called without instantiation
	private RPS()
	{;}//make sure this class is never instantiated
	private final static int Rock = 0;//i chose to map integers to rock/paper/scissors
	private final static int Paper = 1;
	private final static int Scissors = 2;
    public static final int win= 0;//these populate the enum
    public static final int lose = 1;
    public static final int draw = 2;
	private static enum winlosetie  {win,lose,draw}
	
	private static String getchoice(int choice)//easy retrieval of RPS data
	{//open func
		if(choice == 0)
		{
			return "ROCK";
		}
		if(choice == 1)
		{
			return "PAPER";
		}
		if(choice == 2)
		{
			return "SCISSORS";
		}
		
			return null;//this way if a bad value sneaks through the program will probably show due diligence by crashing
	}//close func
	
	public static void play()
	{//open func
		
		winlosetie results = null;//initialize
		int playerwins = 0,compwins = 0,rounds = 0;
		Random p = new Random();//uses random, per instructions
		boolean done = false;//control the while loop
		while(!done)
		{//open while
			int playerchoice = 0;//record player choice
			boolean validinput = false;
			while(!validinput)
			{//pen while
				
			String strplayerchoice = JOptionPane.showInputDialog("ENTER 0 FOR ROCK 1 FOR PAPER 2 FOR SCISSORS PLEASE");
			playerchoice = Integer.parseInt(strplayerchoice);
			if(playerchoice < 0 || playerchoice > 2)
			{JOptionPane.showMessageDialog(null,"INVALID ENTRY; INTEGER FROM 0 TO 2 PLEASE");}
			else{validinput = true;}
			
			}//close while
			
			int compchoice = p.nextInt(3);
			
			if(playerchoice == compchoice)//neaten up the decision tree by treating all ties the same
			{
				
				JOptionPane.showMessageDialog(null,"TIE: PLAYER CHOSE "+ getchoice(playerchoice)+ " AND COMP CHOSE "+getchoice(compchoice));//there was a tie
				results = winlosetie.draw;
			}//optimization: test for draw
			
			if(playerchoice == Rock)//the next 3 if statements handle game logic
			{
				if(compchoice == Paper)
				{results = winlosetie.lose;
				JOptionPane.showMessageDialog(null,"YOU LOSE: PLAYER CHOSE "+ getchoice(playerchoice)+ " AND COMP CHOSE "+getchoice(compchoice));}//
				if(compchoice == Scissors)
				{results = winlosetie.win;
				JOptionPane.showMessageDialog(null,"YOU WIN: PLAYER CHOSE "+ getchoice(playerchoice)+ " AND COMP CHOSE "+getchoice(compchoice));}//rock crushes scissors
			}
			
			if(playerchoice == Paper)
			{
				if(compchoice == Rock)//paper covers rock
				{results = winlosetie.win;
				JOptionPane.showMessageDialog(null,"YOU WIN: PLAYER CHOSE "+ getchoice(playerchoice)+ " AND COMP CHOSE "+getchoice(compchoice));}
				if(compchoice == Scissors)//scissors cuts paper
				{results = winlosetie.lose;
				JOptionPane.showMessageDialog(null,"YOU LOSE: PLAYER CHOSE "+ getchoice(playerchoice)+ " AND COMP CHOSE "+getchoice(compchoice));}
			}
			
			if(playerchoice == Scissors)
			{
				if(compchoice == Paper)//scissors cuts paper
				{results = winlosetie.win;
				JOptionPane.showMessageDialog(null,"YOU WIN: PLAYER CHOSE "+ getchoice(playerchoice)+ " AND COMP CHOSE "+getchoice(compchoice));}
				if(compchoice == Rock)//rock crushes scissors
				{results = winlosetie.lose;
				JOptionPane.showMessageDialog(null,"YOU LOSE: PLAYER CHOSE "+ getchoice(playerchoice)+ " AND COMP CHOSE "+getchoice(compchoice));}
			}

		 if(results == winlosetie.lose)
		 {compwins++;}
		 if(results == winlosetie.win)
		 {playerwins++;}
		 rounds++;	
		 if(rounds > 2)//per instructions:after 3 rounds we quit and tabulate winners, if any
		 {done = true;}
		}//end while
		if(playerwins == 2||playerwins == 3)//calculate results
		{JOptionPane.showMessageDialog(null,"CONGRATULATIONS, YOU BEAT THE COMPUTER! THANKS FOR PLAYING.");}//player won
		else if(compwins == 2||compwins == 3)
		{JOptionPane.showMessageDialog(null,"YOUR WEAK HUMAN MIND WAS NO MATCH FOR THE COMPUTER. YOU LOST THE GAME. THANKS FOR PLAYING.");}//skynet won
		else{JOptionPane.showMessageDialog(null,"DRAW, NEITHER SIDE REACHED TWO WINS WITHIN THREE ROUNDS. THANKS FOR PLAYING.");}

	
	}
	
	
	public static void main(String[] args)//driver program
	{//open func
		boolean done = false;
		while(!done)
		{//open while
			String strplayerchoice = JOptionPane.showInputDialog("ENTER Y TO PLAY ROCK, PAPER SCISSORS OR N TO QUIT");
		if(strplayerchoice.equals("Y"))
			{RPS.play();}
		else if(strplayerchoice.equals("N"))
		{done = true;}
		else{JOptionPane.showMessageDialog(null,"INVALID INPUT Y OR N, CASE SENSITIVE PLEASE.");}
		
		}//close while
	}//close func
	
	
}//close class
