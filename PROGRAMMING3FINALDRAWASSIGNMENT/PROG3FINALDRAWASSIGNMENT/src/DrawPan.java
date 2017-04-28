import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.util.ArrayList;

import javax.swing.JPanel;


public class DrawPan extends JPanel implements MouseMotionListener, MouseListener {

	ArrayList <savestruct> savelist;
	private boolean mousedown;
	private int currdraw;
	private Color currcolor;
	private int anchorx,anchory;
	private int currx,curry;
	private boolean fill;
	final static int OVAL   = 0;
	final static int SQUARE = 1;
	final static int LINE   = 2;
	
	
	public DrawPan()
	{
	
		currdraw = this.LINE;
		mousedown = false;
		savelist = new ArrayList<savestruct>();
		this.setSize(500, 500);
		this.addMouseMotionListener(this);
		this.addMouseListener(this);
	}
	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		//if mouse not pressed set new anchor point
		//if mouse pressed call paint which draws via switch
		System.out.println("TEST");
		mousedown = true;
		anchorx = e.getX();
	    anchory = e.getY();
	    currx = anchorx;
	    curry = anchory;
	    
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		
		System.out.println("MOUSE UP");
		// TODO Auto-generated method stub
		//if mouse pressed false do nothing
		//if true write whatever we were drawing to array store (draw type, xcoord, ycoord)
		if(mousedown == true)//dont handle this event unless the mouse was pressed down in here
		{
			mousedown = false;
			savestruct _savestruct = new savestruct();
			_savestruct.SetColor(currcolor);
			_savestruct.Setcoords(anchorx, anchory, currx, curry);
			_savestruct.setdrawtype(currdraw);
			_savestruct.setFill(fill);
			savelist.add(_savestruct);
			//repaint
		}
	}
	

	
	public void setDrawType(int _drawtype)
	{
		if(_drawtype >= 0 && _drawtype <= 2)//disregard bad values which shouldnt reach the func anyway
		currdraw = _drawtype;
	}//no get draw type; doesnt matter what the draw type is
	
	public void setColor(Color _color)
	{
		this.currcolor = _color;
	}
	@Override
	public void mouseDragged(MouseEvent e) {
		// TODO Auto-generated method stub

		currx = e.getX();
	    curry = e.getY();
	    System.out.println(currx + " " + curry);
	    repaint();
	}
	@Override
	public void mouseMoved(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	
	public void paint(Graphics g)
	{
		g.clearRect(0, 0, this.getWidth(), this.getHeight());//always start w this
		//todo: loop thru array list and draw each type
		
		boolean lessthanzero = false;
		int vecx = currx-anchorx;
		int vecy = curry-anchory;
		int[] xlist = {anchorx,currx,currx,anchorx,anchorx};
		int[] ylist = {anchory,anchory,curry,curry,anchory};
		if(vecx < 0)
		{
			vecx*=-1;
			lessthanzero = true;
		}
		if(vecy< 0)
		{
			vecy*=-1;
			lessthanzero = true;
		}
		System.out.println("vecx : "+vecx +" vecy:  "+vecy);
		System.out.println("currx : "+currx +" curry:  "+curry);
		System.out.println("anchorx : "+anchorx +" anchory:  "+anchory);
		//and here bad planning led to me repeating a ton of code because i didnt modularize and put all the draw calls in functions. i had considered "pushing" whatever the user was currently drawing onto savestruct, drawing it, and then "popping" it off after the draw but in the end said why deviate from a path that works, especially with not having to worry about me or anyone else having to maintain this code
		if(!savelist.isEmpty())//if the user has drawn at least one shape
		{
			for(int i = 0; i < savelist.size();i++)
			{
				savestruct currsave = savelist.get(i);
				boolean fill;
				int mycurrdraw = 0;
				int mycurrx=0;
				int mycurry = 0;
				int myanchorx = 0;
				int myanchory = 0;
				int[] getcoords = currsave.Getcoords();
				myanchorx = getcoords[0];
				myanchory = getcoords[1];
				mycurrx   = getcoords[2];
				mycurry   = getcoords[3];
				mycurrdraw=currsave.getdrawtype();
				fill = currsave.getFill();
				g.setColor(currsave.Getcolor());
				if(mycurrdraw == DrawPan.LINE)
				{
					g.drawLine(myanchorx,myanchory,mycurrx,mycurry);
				}
				
				if(mycurrdraw == DrawPan.SQUARE)
				{
					int myvecx = mycurrx-myanchorx;
					int myvecy = mycurry-myanchory;
					int[] myxlist = {myanchorx,mycurrx,mycurrx,myanchorx,myanchorx};
					int[] myylist = {myanchory,myanchory,mycurry,mycurry,myanchory};
					if(!fill)
					{g.drawPolygon(myxlist,myylist,4);}
				else{g.fillPolygon(myxlist,myylist,4);}
				
				}
				
				if(mycurrdraw == DrawPan.OVAL)
				{
					int myvecx = mycurrx-myanchorx;
					int myvecy = mycurry-myanchory;
					if(myvecx < 0)
					{myvecx *=-1;}
					if(myvecy < 0)
					{myvecy*=-1;}
				
						if(!fill)
						{g.drawOval(myanchorx,myanchory, myvecx,myvecy);}
						else{g.fillOval(myanchorx, myanchory, myvecx, myvecy);}
				
						
					
					
				}
				
				
			}
		}
		
		g.setColor(currcolor);
		if(currdraw == LINE)
		{g.drawLine(currx, curry, anchorx, anchory);}
		if(currdraw == OVAL)
		{
			if(!lessthanzero){
			if(!fill)
			{g.drawOval(anchorx,anchory, vecx,vecy);}
			else{g.fillOval(anchorx, anchory, vecx, vecy);}
			}//wrong will needs vector shit}
			else
			{
				if(!fill)
				{g.drawOval(anchorx,anchory, Math.abs(vecx),Math.abs(vecy));}
				else{g.fillOval(anchorx, anchory, vecx, vecy);}
				}//wrong will needs vector shit}
				
			}
		
		if(currdraw == SQUARE)
		{
			if(!fill)
			{g.drawPolygon(xlist,ylist,4);}
		else{g.fillPolygon(xlist,ylist,4);}
		}//wrong will needs vector shit
	}
	
	public void setFill(boolean _fill)
	{
		fill = _fill;
	}

}
