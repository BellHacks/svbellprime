import javax.swing.JPanel;
import javax.swing.*;
import java.awt.CardLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.util.Random;

public class Quizzer extends JFrame{
	JPanel p = new JPanel();
	CardLayout cards = new CardLayout();
	int numQs;
	int wrongs=0;
	int total=0;
	
	String[][] answers={
		{"a) Litter from humans","b) Factory pollution","c) Burning of fossil fuels","d) Swimming"},
		{"a) Animals that eat plastic are eaten by us, which leads to disease","b) It makes us sad to see dead animals resulting in depression and reduced eating","c) It doesn't affect the food chain","d) Humans want start wanting to eat garbage when they see fishes which leads to bad eating habits"},
		{"a) Alan Webb","b) Boyan Slat","c) Jebron Lames","Mike Brown"},
		{"a) under 500","b) above 500 but below 1000","c) above 1000 but below 5000","d) above 5000"},
		{"a) 2030","b) 2019","c) 2020","2025"},
		{"a) 14 million","b) 10 million", "c) 6 million", "d) 18 million"},
		{"a) protecting storm drains","b) switching to renewable energy", "c) spreading awareness", "d) keeping the water running while brushing your teeth"},
		{"a) Great Pacific Garbage Patch","b) Great Barrier Reef","c) In the middle of the Atlantic Ocean","d) Atlantic Trash Zone"},
		{"100","1000","10000","10"},
      {"5", "10", "1000", "100"}
	};
	
	EnvQuestions questions[] = {
		
		new EnvQuestions(
			"1. Which of the following is not one of the causes of water pollution?",
			answers[0],
			3,this
		),
		new EnvQuestions(
			"2. How does water pollution affect the food chain?",
			answers[1],
			0,this
		),
		new EnvQuestions(
			"3. Who came up with the idea of the artificial coastline",
			answers[2],
			1,this
		),
		new EnvQuestions(
			"4. How many animals died from the oil spill in Britain in 2010?",
			answers[3],
			1,this
		),
		new EnvQuestions(
			"5. When is the Ocean Cleanup Organization planning on implement the floatation barrier?",
			answers[4],
			2,this
		),
		new EnvQuestions(
			"6. About how many million people drink contaminated water daily?",
			answers[5],
			0,this
		),
		new EnvQuestions(
			"7. Which is not a way to help reduce water pollution?",
			answers[6],
			3,this
		),
		new EnvQuestions(
			"8. Where is the Artificial Coastline going to be placed?",
			answers[7],
			1,this
		),
		new EnvQuestions(
			"9. How many times bigger will the final Artifical Coastline be than the coastline",
			answers[8],
			1,this
		),
      new EnvQuestions(
         "9. How many times bigger will the final Artifical Coastline be than the coastline",
         answers[9],
         2,this
      )
	};

	public static void main(String args[]){
		new Quizzer();
	}
	
	public Quizzer(){
		super("Quiz Game");
		setResizable(true);
		setSize(500,400);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		p.setLayout(cards);
		numQs=questions.length;
		for(int i=0;i<numQs;i++){
			p.add(questions[i],"q"+i);
		}
		Random r=new Random();
		int i=r.nextInt(numQs);
		cards.show(p,"q"+i);
		add(p);
		setVisible(true);
	}
	
	public void next(){
		if((total-wrongs)==numQs){
			showSummary();
		}else{
			Random r=new Random();
			boolean found=false;
			int i=0;
			while(!found){
				i=r.nextInt(numQs);
				if(!questions[i].used){
					found=true;
				}
			}
			cards.show(p,"q"+i);
		}
	}
	
	public void showSummary(){
		JOptionPane.showMessageDialog(null,"All Done :), here are your results"+
			"\nNumber of incorrect Answers: \t"+wrongs+
			"\nNumber of Correct Answers: \t"+(total-wrongs)+
			"\nAverage Incorrect Answers per Quesiotn: \t"+((float)wrongs/numQs)+
			"\nPercent Correct: \t\t"+(int)(((float)(total-wrongs)/total)*100)+"%"
		);
		System.exit(0);
	}
}

public class EnvQuestions extends JPanel implements ActionListener
{
   int correctAns;
   Quizzer quiz;
   int selected;
   boolean used;
   JPanel qPanel = new JPanel();
   JPanel aPanel = new JPanel();
   
   JRadioButton[] responses;
   ButtonGroup group = new ButtonGroup();
   
   JPanel botPanel = new JPanel();
   JButton next = new JButton("Next");
   JButton finish = new JButton("Finish");
         
   
   public EnvQuestions(String q, String[] options, int ans, Quizzer quiz)
   {
      this.quiz = quiz;
      setLayout(new BoxLayout(this,BoxLayout.Y_AXIS));
      correctAns = ans;
      qPanel.add(new JLabel(q));
      add(qPanel);
      
      responses = new JRadioButton[options.length];
      for (int i = 0; i<options.length; i++)
      { 
         responses[i] = new JRadioButton(options[i]);
         responses[i].addActionListener(this);
         group.add(responses[i]);
         aPanel.add(responses[i]);
         
      }
      add(aPanel);
      
      next.addActionListener(this);
      finish.addActionListener(this);
      botPanel.add(next);
      botPanel.add(finish);
      add(botPanel);
   }
   
   public void actionPerformed(ActionEvent e)
   {
      Object src = e.getSource();
      
      if(src.equals(next))
      {
         showResult();
         if(selected == correctAns)
         {
            used = true;
            quiz.next();
         }
      }
      
      if(src.equals(finish))
      {
         quiz.showSummary();
      }
      
      for(int i = 0; i < responses.length; i++)
      {
         if(src == responses[i])
         {
            selected = i;
         }
      }
   }
   
   public void showResult()
   {
      String text = responses[selected].getText();
      quiz.total++;
      if(selected == correctAns)
      {
         JOptionPane.showMessageDialog(null, text + " is correct \n Well Done:)");  
      }
      
      else
      {
			quiz.wrongs++;
			JOptionPane.showMessageDialog(null,text+" is wrong\nSorry :(");
		}
   }      
}

