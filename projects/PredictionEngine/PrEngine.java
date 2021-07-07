
import java.awt.Button;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.Label;
import java.awt.TextArea;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.LineBorder;
import javax.swing.border.TitledBorder;

public class PrEngine {

	private JFrame frmPredictionEngine;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					PrEngine window = new PrEngine();
					window.frmPredictionEngine.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public PrEngine() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmPredictionEngine = new JFrame();
		try {
			frmPredictionEngine.setIconImage(ImageIO.read(getClass().getResourceAsStream("emg.png")));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		// frmPredictionEngine.setIconImage(Toolkit.getDefaultToolkit().getImage("emg.png"));
		frmPredictionEngine.setTitle("Prediction Engine");
		frmPredictionEngine.setResizable(false);
		frmPredictionEngine.setBounds(100, 100, 838, 545);
		frmPredictionEngine.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmPredictionEngine.getContentPane().setLayout(null);

		Label label = new Label("Prediction Engine");
		label.setBounds(336, 7, 181, 33);
		label.setFont(new Font("Meiryo UI", Font.BOLD, 20));
		frmPredictionEngine.getContentPane().add(label);

		JPanel panel = new JPanel();
		panel.setBorder(new TitledBorder(new LineBorder(new Color(0, 0, 0), 1, true), "Input ", TitledBorder.LEADING,
				TitledBorder.TOP, null, new Color(0, 0, 0)));
		panel.setBounds(281, 46, 329, 64);
		frmPredictionEngine.getContentPane().add(panel);
		panel.setLayout(null);

		inputField = new TextField();
		inputField.setFont(new Font("Calibri", Font.PLAIN, 26));
		inputField.setBounds(10, 21, 202, 33);
		panel.add(inputField);

		Button button = new Button("Run");
		button.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				runEngine();
			}
		});
		button.setFont(new Font("Calibri", Font.BOLD, 23));
		button.setBounds(218, 21, 101, 33);
		panel.add(button);

		consoleArea = new TextArea();
		consoleArea.setText(
				"Hi!! welcome to prediction engine, \r\nPlease paste your training set into the right text area\r\nand enter you input from the top text field, and then click on run.");
		consoleArea.setEditable(false);
		consoleArea.setBackground(Color.BLACK);
		consoleArea.setForeground(Color.GREEN);
		consoleArea.setFont(new Font("Arial", Font.BOLD, 12));
		consoleArea.setBounds(10, 148, 409, 343);
		frmPredictionEngine.getContentPane().add(consoleArea);

		trainingSetArea = new TextArea();
		trainingSetArea.setFont(new Font("Arial", Font.BOLD, 16));
		trainingSetArea.setBounds(442, 148, 380, 343);
		frmPredictionEngine.getContentPane().add(trainingSetArea);

		label_1 = new Label("Welcome");
		// label_1.setBackground(Color.GRAY);
		label_1.setBounds(366, 116, 228, 22);
		frmPredictionEngine.getContentPane().add(label_1);
		label_1.setForeground(Color.GREEN);
		label_1.setFont(new Font("Arial", Font.BOLD, 16));
		
		textField = new TextField();
		textField.setFont(new Font("Calibri", Font.PLAIN, 26));
		textField.setBounds(392, 7, 73, 33);
		frmPredictionEngine.getContentPane().add(textField);
		
		iteration = new TextField();
		iteration.setText("500");
		iteration.setFont(new Font("Calibri", Font.PLAIN, 26));
		iteration.setBounds(620, 66, 64, 33);
		frmPredictionEngine.getContentPane().add(iteration);
	}

	TextArea consoleArea, trainingSetArea;
	Label label_1;
	TextField inputField;
	int itr = 500;

	void runEngine() {
		String tSet = trainingSetArea.getText();
		try {
			String itrText = iteration.getText();
			if(itrText==null || itrText.trim().length()==0){
				warn("Invalid Iteration");
				return;
			}
			itr = Integer.parseInt(itrText);
			
			String input = inputField.getText();
			if(input==null || input.trim().length()==0){
				warn("Invalid Input");
				return;
			}
			
			float xInput = Float.parseFloat(input);
			
			if (validateTrainingSet(tSet)) {
				consoleArea.setText("");
				String lines[] = tSet.replace("\r", "").split("\n");
				final int m = lines.length;
				log("====== No. of training sets: " + m);
				final float x[] = new float[m];
				final float y[] = new float[m];
				int i = 0, j = 0;
				for (String line : lines) {
					if (line.contains(" ")) {
						String parts[] = line.split(" ");
						x[i] = Float.parseFloat(parts[0]);
						y[i] = Float.parseFloat(parts[1]);
						i++;
					} else {
						warn("Invalid training set");
						return;
					}
				}
				
				T0 = T1 = y[0]/2;
				show("Processing!!");
				grad(x, y, m);	
				//String.format("%.2f", HXi(T0, T1, xInput))
				show(String.format("%.2f", HXi(T0, T1, xInput))+"");
				
			} else {
				warn("Invalid training set");
				return;
			}
		} catch (Exception e) {
			warn("Error : " + e.getMessage());
		}
	}

	void log(String msg) {
		consoleArea.append("\n" + msg);
	}

	void show(String msg) {
		label_1.setBackground(Color.BLACK);
		label_1.setForeground(Color.GREEN);
		label_1.setText(msg);
	}

	void warn(String msg) {
		label_1.setBackground(Color.RED);
		label_1.setForeground(Color.WHITE);
		label_1.setText(msg);
	}

	boolean validateTrainingSet(String s) {
		return s != null && s.length() > 1 && s.contains(" ") && s.contains("\n");
	}

	float T0, T1;
	private TextField textField;
	private TextField iteration;

	void grad(float X[], float Y[], int m) {
		Float JT = null;
		for (int i = 1; i <= itr; i++) {
			log("=========== Grad itr: " + i + " ============");
			float temp0 = temp0(T0, T1, X, Y, m);
			float temp1 = temp1(T0, T1, X, Y, m);
			float t0 = temp0;
			float t1 = temp1;
			log("----------------------------------");
			log("t0   = " + t0 + " [temp0=" + temp0 + "]");
			log("t1   = " + t1 + " [temp1=" + temp1 + "]");
			float jTheta = jTheta(t0, t1, X, Y, m);
			log("@@@@@ jTheta = " + jTheta + " [t0=" + t0 + ", t1=" + t1 + "]");
			log("OLD jTheta = " + JT);
			if (jTheta > 10000 || (JT != null && JT < jTheta && JT < 1)) {
				log("CONVERGED!!!  T0: " + T0 + ", T1: " + T1);
				break;
			}
			T0 = t0;
			T1 = t1;
			JT = jTheta;
		}
	}

	float temp0(float t0, float t1, float X[], float Y[], int m) {
		float sum = 0;
		for (int i = 0; i < m; i++) {
			// System.out.println("## i = " + i);
			float diff = diff(t0, t1, X[i], Y[i]);
			sum += diff;
			// System.out.println("sum = " + sum + " [diff=" + diff + "]");
		}
		float temp0 = t0 - (0.01f) * (1 / (float) m) * sum;
		//log("----------------------------------");
		//log("temp0 = " + temp0 + " [t0=" + t0 + ", sum=" + sum + ", m=" + m + "]");
		return temp0;
	}

	float temp1(float t0, float t1, float X[], float Y[], int m) {
		float sum = 0;
		for (int i = 0; i < m; i++) {
			// System.out.println("## i = " + i);
			float diff = diff(t0, t1, X[i], Y[i]);
			sum += diff * X[i];
			// System.out.println("sum = " + sum + " [diff=" + diff + ", X(" + i
			// + ")=" + X[i] + "]");
		}
		float temp1 = t1 - (0.01f) * (1 / (float) m) * sum;
		//log("----------------------------------");
		//log("temp1 = " + temp1 + " [t1=" + t1 + ", sum=" + sum + ", m=" + m + "]");
		return temp1;
	}

	float jTheta(float t0, float t1, float X[], float Y[], int m) {
		float sum = 0;
		for (int i = 0; i < m; i++) {
			// System.out.println("## i = " + i);
			float diff = diff(t0, t1, X[i], Y[i]);
			sum += diff * diff;
			// System.out.println("sum = " + sum + " [diff=" + diff + "]");
		}
		float jTheta = (1 / (float) m / 2f) * sum;
		//log("----------------------------------");
		//log("jTheta = " + jTheta + " [sum=" + sum + ", m=" + m + "]");
		return jTheta;
	}

	float diff(float t0, float t1, float xi, float yi) {
		float hxi = HXi(t0, t1, xi);
		float diff = hxi - yi;
		// System.out.println("diff = " + diff + " [HXi=" + hxi + ", yi=" + yi +
		// "]");
		return diff;
	}

	float HXi(float t0, float t1, float xi) {
		float hxi = t0 + t1 * xi;
		// System.out.println("HXi = " + hxi + " [t0=" + t0 + ", t1=" + t1 + ",
		// xi=" + xi + "]");
		return hxi;
	}
}
