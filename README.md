# AI-phishing-project-CTS
                                       
                                        AI PHISHING BLOCKERS
 
  <img src="https://tse3.mm.bing.net/th?id=OIP.HmyoLamVAal7Fm803oVoogHaE6&pid=Api&P=0&h=180">
 
Problem Statement:


  Phishing attacks have advanced to previously unheard-of levels of sophistication, focusing on weaknesses in both people and businesses. Cybercriminals utilize     deceptive strategies to push users into revealing personal information, banking credentials, and other sensitive data, which can result in financial loss, identity theft, and violations of privacy. Email filters and blacklists, which are common phishing detection tools, are ineffective against these constantly developing techniques.

  Additionally, phishing attempts have expanded beyond emails to include a variety of other communication methods, including text messages, phone calls, and social media websites. A complex and flexible solution is required since the enlarged landscape makes it difficult to thoroughly identify and stop phishing attempts.

  Our goal is to create a phishing blocker powered by AI that can detect phishing attacks across many channels in real-time. This system intends to precisely identify and stop phishing attempts across numerous communication channels by leveraging the capabilities of artificial intelligence, Generative Adversarial Network, machine learning, natural language processing, and pattern recognition. We want to significantly decrease the success rates of phishing attacks and strengthen the security posture of people as well as businesses through proactive detection and prevention.

  The goal of this project is to create a reliable defense against the changing phishing threat landscape, helping to create a secure digital environment, ensuring a safer online experience and reducing the risk of falling victim to cybercriminals.


Approach:

Our approach involves a three-fold strategy to tackle the pervasive issue of phishing attacks:
1. Real-time URL Analysis:
   Initiate proactive URL analysis during the rendering process to swiftly evaluate the legitimacy of websites as users navigate the online landscape.
2. AI-Powered Detection:
  Train our Machine Learning (ML) model on a diverse dataset containing both authentic and phishing URLs, utilizing features like domain age and URL structure.
Implement the GAN framework to generate synthetic examples, enriching our dataset and enabling the model to learn from a more extensive range of phishing scenarios.
3. Synthetic Dataset Creation with GAN:
  Leverage GANs to generate artificial phishing examples, addressing limitations associated with a potentially limited set of real-world labeled data.
This synthetic dataset augments the ML model's training process, enhancing its ability to recognize and adapt to subtle variations in phishing techniques.

Techstack:

Core Language:
           We use Python as the core programing language.

URL prasing:
            URL lib
            Request

Creating GAN:
            TensorFlow
            Keras

Classification:
          Pandas       
          Numpy
          Matplotlib
          sklearn

Solution:
  The proposed solution focuses on enhancing fraud detection through the development of a browser extension aimed at detecting phishing websites. 
  Leveraging the power of Generative Adversarial Networks (GANs), synthetic phishing URLs can be generated to create a diverse dataset of closely-identical websites.
  This dataset can be utilized to train and strengthen the machine learning classifier, improving its accuracy in distinguishing legitimate websites from fraudulent ones. 
  When a user visits a website, the browser extension will analyse the URL and provide real-time notifications by Blocking the webpage, clearly indicating whether the website is genuine or a phishing site.
  By utilizing this innovative approach, users can trust that their sensitive information is safeguarded, ensuring a safer online experience and reducing the risk of falling victim to cybercriminals.

Impact of our solution:

Recent Scam:
  In this scam the scammers send a text message to your phone that closely remembers e-challan alerts. The messages have a payment link. When the use click the link the device security is compromised, and the hackers get access to credit/debit card details. Before user know, our model can also predict it. 

Prospects:
SOCIAL ENGINEERING SOPHISTICATION: 
  Phishing attacks often rely on social engineering to manipulate individuals into divulging sensitive information. As technology improves, attackers may use more sophisticated and targeted social engineering techniques to craft convincing and personalized phishing messages.
DECEPTIVE TACTICS:
  Phishing attacks can take various forms, such as email phishing, smishing (SMS phishing), vishing (voice phishing), and more. Attackers may combine these tactics to create multi-channel phishing campaigns, making it harder for individuals and organizations to defend against them.
EVOLUTION OF ATTACK VECTORS:
  Phishing attacks adapt to new technologies and communication channels. As people increasingly use messaging apps, social media, and other platforms, attackers may exploit these channels to launch phishing campaigns.
TARGETED ATTACKS:
  While generic phishing campaigns are widespread, targeted phishing attacks (spear phishing) are becoming more prevalent. Attackers may gather information about specific individuals or organizations to create highly personalized and convincing phishing messages.


  




