import java.awt.Color;
import java.awt.Graphics;


public class savestruct {
	
	private Color _color;
	private int DRAWTYPE;
	private boolean fill;
	int anchorx,anchory,currx,curry;
	
	public savestruct()
	{
		;
	}

	public void Setcoords(int anchx,int anchy,int curx,int cury)
	{
		anchorx = anchx;
		anchory = anchy;
		currx = curx;
		curry = cury;
	}
	
	public void SetColor(Color c)
	{
		_color = c;
	}
	
	public void setdrawtype(int p)
	{
		if(p>=0 && p <= 2)
		{
			DRAWTYPE = p;
		}
	}
	
	public void setFill(boolean _fill)
	{
		fill = _fill;
	}
	
	public boolean getFill()
	{
		return fill;
	}
	
	public int getdrawtype()
	{
		return DRAWTYPE;
	}
	
	public int[] Getcoords()
	{
		int[] coords ={anchorx,anchory,currx,curry};
		return coords;
	}
	
	public Color Getcolor()
	{
		return _color;
	}

	
}
