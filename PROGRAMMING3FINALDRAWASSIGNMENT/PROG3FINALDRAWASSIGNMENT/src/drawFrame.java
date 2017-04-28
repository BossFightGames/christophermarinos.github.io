import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JInternalFrame;
import javax.swing.JPanel;


public class drawFrame extends JInternalFrame {
	
	
	private DrawPan _drawpan;
	private boolean clickedupon;//whether the mouse is down. this changes how the mousepressed events are handled
	
	public drawFrame(String name)
	{
		this.setName(name);
		this.setResizable(true);
		this.setClosable(true);//or it never goes away
		this.setSize(100,100);
		_drawpan = new DrawPan();
		this.add(_drawpan);
		this.setVisible(true);
		
	}



	
		
	}


