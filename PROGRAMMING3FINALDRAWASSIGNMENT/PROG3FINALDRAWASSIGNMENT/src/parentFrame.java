import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.MenuItem;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.InputMethodEvent;
import java.awt.event.InputMethodListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;


import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.JTextArea;
import javax.swing.SwingConstants;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;


public class parentFrame extends JFrame {

	private DrawPan _drawpanel;
	private JSlider Red,Green,Blue;
	private JCheckBox fill;
	private JComboBox shapemenu;
	private JPanel controlpanel,sliderpanel;
	private JLabel slideRed,slideGreen,slideBlue;
	private JTextArea Redtex,Greentex,Bluetex;
	private JMenuBar mybar;
	
	public parentFrame()
	{
	   
		String[] shapes = {"LINE","OVAL","RECTANGLE"}; 
		Red = new JSlider(SwingConstants.HORIZONTAL,0,255,255);
		Green = new JSlider(SwingConstants.HORIZONTAL,0,255,255);
		Blue = new JSlider(SwingConstants.HORIZONTAL,0,255,255);
		Red.setValue(0);
		Green.setValue(0);
		Blue.setValue(0);
		
		shapemenu = new JComboBox(shapes);
		this.setSize(500,500);
		_drawpanel = new DrawPan();
		Color setcol = new Color(Red.getValue(),Green.getValue(),Blue.getValue());
		controlpanel = new JPanel();
		controlpanel.setLayout(new FlowLayout(FlowLayout.LEFT));
		sliderpanel = new JPanel();
		sliderpanel.setLayout(new GridLayout(3,2));
		Redtex = new JTextArea();
		Greentex = new JTextArea();
		Bluetex = new JTextArea();
		sliderpanel.add(Red);
		sliderpanel.add(Redtex);
		sliderpanel.add(Green);
		sliderpanel.add(Greentex);
		sliderpanel.add(Blue);
		sliderpanel.add(Bluetex);
		Redtex.setText(String.valueOf(Red.getValue()));
		Greentex.setText(String.valueOf(Green.getValue()));
		Bluetex.setText(String.valueOf(Blue.getValue()));
		fill = new JCheckBox("FILL");
		controlpanel.add(shapemenu);
		controlpanel.add(fill);
		controlpanel.setSize(100, 50);
		this.setLayout(new GridLayout(3,1));
		this.add(controlpanel);
		this.add(_drawpanel);
		this.add(sliderpanel);
		this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		mybar = new JMenuBar();
		JMenu mymenu = new JMenu("File");
		JMenu mywindow = new JMenu("Window");
		mybar.add(mymenu);
		this.setJMenuBar(mybar);
		this.setVisible(true);
		
		
		
		
		 Red.addChangeListener(new ChangeListener() {

			@Override
			public void stateChanged(ChangeEvent arg0) {
				// TODO Auto-generated method stub
				int colorpointred = Red.getValue();
				int colorpointblue = Blue.getValue();
				int colorpointgreen = Green.getValue();
				Redtex.setText(String.valueOf(colorpointred));
				Color mycol = new Color(colorpointred,colorpointgreen,colorpointblue);
				_drawpanel.setColor(mycol);
			}

	
					

			
	       	 
		       
		        });  
			 
		 
		 Green.addChangeListener(new ChangeListener() {

			@Override
			public void stateChanged(ChangeEvent arg0) {
				// TODO Auto-generated method stub
				int colorpointred = Red.getValue();
				int colorpointblue = Blue.getValue();
				int colorpointgreen = Green.getValue();
				Greentex.setText(String.valueOf(colorpointgreen));
				Color mycol = new Color(colorpointred,colorpointgreen,colorpointblue);
				_drawpanel.setColor(mycol);
				
			}

				
					

			
	       	 
		       
		        });  
		 
		 Blue.addChangeListener(new ChangeListener() {

			@Override
			public void stateChanged(ChangeEvent arg0) {
				// TODO Auto-generated method stub
				int colorpointred = Red.getValue();
				int colorpointblue = Blue.getValue();
				int colorpointgreen = Green.getValue();
				Bluetex.setText(String.valueOf(colorpointblue));
				Color mycol = new Color(colorpointred,colorpointgreen,colorpointblue);
				_drawpanel.setColor(mycol);
				
			}	       
		        });  
		 
		 
		 Bluetex.addKeyListener(new KeyListener() {

			@Override
			public void keyPressed(KeyEvent arg0) {
				
				;//ignore
			}

			@Override
			public void keyReleased(KeyEvent arg0) {
				
				;//ignore
			}

			@Override
			public void keyTyped(KeyEvent arg0) {
				
				//get to work
				Blue.setValue(Integer.parseInt(Bluetex.getText()));
			}

			
	
			
			
				       
		        });  
		
		 
		 Redtex.addKeyListener(new KeyListener() {

				@Override
				public void keyPressed(KeyEvent arg0) {
					
					;//ignore
				}

				@Override
				public void keyReleased(KeyEvent arg0) {
					
					;//ignore
				}

				@Override
				public void keyTyped(KeyEvent arg0) {
					
					//get to work
					Red.setValue(Integer.parseInt(Redtex.getText()));
				}

				
		
				
				
					       
			        });  
		 
		 
		 Greentex.addKeyListener(new KeyListener() {

				@Override
				public void keyPressed(KeyEvent arg0) {
					
					;//ignore
				}

				@Override
				public void keyReleased(KeyEvent arg0) {
					
					;//ignore
				}

				@Override
				public void keyTyped(KeyEvent arg0) {
					
					//get to work
					Green.setValue(Integer.parseInt(Greentex.getText()));
				}

				
		
				
				
					       
			        });  
		
		 shapemenu.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
			int shapeint = 0;
			String shapechoose = (String)shapemenu.getSelectedItem();
			if(shapechoose.equals("OVAL"))
			{shapeint = DrawPan.OVAL;}
			if(shapechoose.equals("LINE"))
			{shapeint = DrawPan.LINE;}
			if(shapechoose.equals("RECTANGLE"))
			{shapeint = DrawPan.SQUARE;}
			
			_drawpanel.setDrawType(shapeint);
				}//anon action listener

		
       	 
	       
	        });  
		 
		 fill.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
			if(fill.isSelected())
			_drawpanel.setFill(true);
			else{_drawpanel.setFill(false);}
				}//anon action listener

		
       	 
	       
	        });  
		
		
		
		
		
		
	}
}
