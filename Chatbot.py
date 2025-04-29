import openai
import tkinter as tk
from tkinter import scrolledtext

openai.api_key =("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")

def match_keywords(text, keywords):
    return any(keyword in text.lower() for keyword in keywords)

# ChatGPT integration
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Function to handle sending messages
def send_message():
    user_input = entry.get().strip()
    if not user_input:
        return

    if user_input.lower() == "exit":
        root.destroy()
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"< You > : {user_input}\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)
    entry.delete(0, tk.END)
    root.update_idletasks()

    # Hardcoded responses
    if match_keywords(user_input, ["what is artificial intelligence", "what is ai"]):
        bot_response = ("\n"
            "Artificial Intelligence (AI) refers to the development of computer systems "
            "that can perform tasks that typically require human intelligence, such as "
            "problem-solving, learning, and decision-making."
            "\n"
        )

    elif match_keywords(user_input, ["how does ai work", "how does artificial intelligence work"]):
        bot_response = ("\n"
            "AI works through algorithms and machine learning. Algorithms are step-by-step "
            "instructions for computers to follow, while machine learning enables systems to "
            "learn from data, identify patterns, and improve over time."
            "\n"
        )

    elif match_keywords(user_input, ["ai in healthcare", "how is ai used in healthcare"]):
        bot_response = ("\n"
            "AI is transforming healthcare by improving diagnostic accuracy, enabling predictive analytics, "
            "accelerating drug discovery, and personalizing treatment plans. Examples include AI in medical imaging, "
            "remote patient monitoring, and virtual health assistants."
            "\n"
        )

    elif match_keywords(user_input, ["how does ai benefit businesses", "ai in business"]):
        bot_response = ("\n"
            "AI helps businesses by automating tasks, analyzing data, enhancing customer service, "
            "improving decision-making, and enabling predictive analytics. Applications span retail, finance, "
            "manufacturing, and more."
            "\n"
        )

    elif match_keywords(user_input, ["ai in entertainment", "how is ai used in entertainment"]):
        bot_response = ("\n"
            "AI enhances entertainment through personalized recommendations, intelligent game characters, "
            "procedural content generation, automated content creation, and real-time subtitles or translations."
            "\n"
        )
        
    elif match_keywords(user_input, ["what are the ethical considerations in ai","what are the ethical considerations in artificial intelligence"]):
        bot_response = ("\n"
            "Ethical considerations in AI are crucial, and they revolve around addressing AI bias and "
            "privacy concerns.\n "
            "         AI systems can inadvertently reflect biases present in their training data. This bias can " 
            "lead to unfair or discriminatory outcomes. To tackle this, developers must implement robust bias "
            "detection and mitigation techniques. It involves carefully curating training data and continuously "
            "monitoring AI systems for bias.\n"
            "          Privacy concerns arise due to the vast amount of data AI systems process. Protecting individuals’ " 
            "privacy is vital. This involves implementing stringent data anonymization techniques, secure storage, " 
            "and adherence to data protection regulations like GDPR. "
            "\n"
        )
        
    elif match_keywords(user_input, ["what are the main challenges in ai development","what are the main challenges in artificial intelligence development"]):
        bot_response = ("\n"
            "AI development faces both technical challenges and societal impacts.\n"
            "         Technical challenges include achieving higher accuracy and efficiency in AI models, improving natural "
            "language understanding, and addressing issues related to scalability. Research and innovation in these areas "
            "drive AI progress.\n"
            "          Societal impacts encompass concerns about job displacement, transparency, and accountability. " 
            "As AI becomes more integrated into society, addressing these issues is essential. Developing policies "
            "and regulations, along with fostering ethical AI practices, is key to mitigating negative societal impacts. "
            "\n"
        )

    elif match_keywords(user_input, ["what are the emerging ai trends","what are the emerging artificial intelligence trends"]):
        bot_response = (
            "\n"
            "(1).Conversational AI: This involves using natural language processing (NLP), speech recognition, and machine " 
            "learning to create chatbots, virtual assistants, and voice interfaces that interact naturally with humans. " 
            "It benefits businesses in customer service, sales, marketing, and productivity.\n"
            "\n"
            "(2).Ethical AI: This focuses on developing AI systems that follow ethical principles like fairness, transparency, " 
            "accountability, and privacy. It ensures AI doesn’t harm humans or the environment and respects human rights and laws.\n"
            "\n"
            "(3).The Fusion of AI and IoT (AIoT): This integrates AI with the Internet of Things (IoT) to enable smart devices to " 
            "learn, make decisions, and act autonomously. AIoT impacts areas like smart cities, homes, healthcare, manufacturing, " 
            "and agriculture.\n"
            "\n"
            "(4).AI in Cybersecurity: AI is used to detect, prevent, and respond to cyberattacks by analyzing data, identifying patterns, " 
            "generating alerts, and automating responses.\n"
            "\n"
            "(5).Quantum AI: Quantum computing enhances AI algorithms and models, solving complex problems faster and more efficiently.\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["how can ai help solve global problems","how can artificial intelligence help solve global problems"]):
        bot_response = (
            "\nAI has a significant role in addressing global challenges:\n"
            "\n"
            "(1).Monitoring and measuring greenhouse gas emissions and environmental changes: AI collects and analyzes data "
            "from various sources to track and quantify climate change impacts, like carbon footprints, deforestation, air "
            "quality, and renewable energy projects.\n"
            "\n"
            "(2).Optimizing energy efficiency and reducing waste: AI improves energy systems, transportation, and manufacturing "
            "processes to reduce consumption and emissions through smart grids, thermostats, lighting, mobility, and recycling.\n"
            "\n"
            "(3).Developing and deploying low-carbon technologies: AI accelerates the adoption of clean energy sources by improving "
            "their performance, predicting energy demand, and integrating distributed energy resources.\n"
            "\n"
            "(4).Adapting and building resilience to climate impacts: AI enhances preparedness and response to climate change effects, "
            "such as extreme weather events and biodiversity loss, through early warning systems, disaster management tools, climate "
            "models, and adaptation strategies.g\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["what is machine learning, and how does it relate to ai","what is machine learning, and how does it relate to artificial intelligence"]):
        bot_response = ("\n"
            "Machine learning (ML) is the bedrock of artificial intelligence (AI). At its core, ML empowers AI systems to learn from "
            "data and improve their performance over time. Imagine it as teaching a computer to recognize patterns and make decisions, " 
            "much like a human brain, but with the advantage of processing vast amounts of data at lightning speed. \n"
            "\n"
            "In simpler terms, machine learning is a subset of AI that focuses on enabling computers to learn from experience. " 
            "AI, on the other hand, encompasses a broader spectrum of technologies that aim to simulate human intelligence, including "
            "problem-solving, reasoning, and decision-making.\n"
            "\n"
            "The connection between ML and AI is profound. ML algorithms enable AI systems to recognize images, understand spoken language, "
            "predict stock prices, and even drive autonomous vehicles. In essence, machine learning is the engine that powers AI’s ability "
            "to think and act intelligently.\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["how do ai neural networks function","how do artificial intelligence neural networks function"]):
        bot_response = ("\n"
            "AI neural networks are the building blocks of many modern AI systems. They draw inspiration from the human brain’s neural "
            "structure and are designed to process information in a similarly interconnected way. These networks consist of layers of "
            "artificial neurons, each responsible for specific computations.\n"
            "\n"
            "Here’s how it works: Input data is fed into the first layer of the neural network. Each neuron in this layer processes "
            "a piece of the input data and passes its output to the next layer. This process continues through multiple layers, with each layer "
            "performing increasingly complex computations. Finally, the output layer produces the network’s final prediction or decision.\n"
            "\n"
            "The magic lies in training these neural networks. During training, the network is exposed to a vast amount of labeled data, "
            "and it adjusts its internal parameters (weights and biases) to minimize errors. This fine-tuning process allows the network to make "
            "accurate predictions when presented with new, unseen data.\n "
            "\n"
            "In essence, AI neural networks function by simulating the interconnected processing of information, enabling them to " 
            "perform tasks like image recognition, natural language understanding, and more.\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["what is natural language processing in ai","what is natural language processing in artificial intelligence"]):
        bot_response = ("\n"
            "          Natural Language Processing (NLP) is a subset of artificial intelligence that focuses on the interaction between computers and " 
            "human language. Its goal is to enable computers to understand, interpret, and generate human language in a valuable way.\n"
            "\n"
            "          NLP plays a crucial role in various applications, from chatbots that converse with users in natural language to language translation " 
            "systems like Google Translate. At its core, NLP involves three key tasks:\n"
            "(1).Tokenization: Breaking down text into individual words or phrases, known as tokens.\n" 
            "(2).Syntax Analysis: Understanding the grammatical structure of sentences to identify relationships between words.\n"
            "(3).Semantics: Extracting the meaning and context from text to comprehend user intentions.\n"
            "\n"
            "          NLP leverages machine learning techniques and large language datasets to achieve these tasks. It allows AI systems to process and " 
            "respond to text or speech inputs in a way that feels natural to humans.\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["explain the concept of supervised learning in ai","explain the concept of supervised learning in artificial intelligence"]):
        bot_response = ("\n"
            "          Supervised learning is a fundamental concept in Artificial Intelligence (AI). It’s like teaching a computer to recognize patterns and make "
            "predictions based on labeled data. In this method, we provide the machine with a dataset containing both input and correct output, which acts as " 
            "a teacher guiding the algorithm. The AI system learns from this labeled data and makes predictions or classifications when given new, unseen data.\n"
            "\n"
            "          Supervised learning is widely used in various applications, such as image recognition, spam email filtering, and even autonomous driving. " 
            "It’s like training a dog to perform tricks – the more examples (data) and guidance (labels) you provide, the better the AI becomes at making " 
            "accurate predictions.\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["what are unsupervised learning and its applications in ai","what are unsupervised learning and its applications in artificial intelligence"]):
        bot_response = ("\n"
            "          Unsupervised learning is another branch of AI, but it’s a bit different. Here, the AI system learns from unlabeled data, meaning there " 
            "are no clear instructions or labels provided. It’s like asking the computer to find hidden patterns or structures in the data all by itself.\n"
            "\n"
            "Here are some key applications of unsupervised learning in AI:\n"
            "(1).Clustering: Unsupervised learning is often used for clustering data points into groups based on similarities. This is used in:\n"
            "(2).Dimensionality Reduction: Unsupervised learning techniques help reduce the dimensionality of data, making it easier to work with. This is used in:\n"
            "(3).Anomaly Detection: Unsupervised learning can detect unusual patterns or anomalies in data, which is crucial for:\n"
            "(4).Generative Models: Unsupervised learning is used to create generative models that can generate new data similar to the training data. Applications include:\n"
            "(5).Density Estimation: Unsupervised learning helps estimate the probability density function of a dataset, which has applications in:\n"
            "(6).Market Basket Analysis: In retail and e-commerce, unsupervised learning is used to discover associations between products frequently bought together. This enables:\n"
            "(7).Image and Video Processing: Unsupervised learning helps in tasks like:\n"
            "(8).Biomedical Data Analysis: Unsupervised learning is used to analyze biological and medical data for:\n"
            "\n"
        )
        
        
    elif match_keywords(user_input, ["can ai understand human emotions","can artificial intelligence understand human emotions"]):
        bot_response = ("\n"
            "          Yes, AI has made significant advancements in understanding human emotions. Emotion recognition technology uses various techniques, " 
            "including natural language processing and computer vision, to analyze human expressions, speech, and behavior. For instance, when it comes to " 
            "text-based emotion AI, tools like Grammarly are notable examples. Grammarly can help writers improve the tone and clarity of their writing based " 
            "on the intended emotion, making it a valuable asset for content creators and communicators.\n"
            "\n"
            "          In the realm of voice emotion AI, technologies are designed to analyze vocal tones and other cues that indicate the emotional state of the speaker. " 
            "Beyond Verbal, for example, is a company at the forefront of this field. They develop voice emotion analytics with applications spanning health, " 
            "education, and customer service. This technology enables businesses to better understand and respond to the emotional needs of their customers and clients.\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["what is computer vision, and how does ai use it","what is computer vision, and how does artificial intelligence use it"]):
        bot_response = ("\n"
            "          Computer vision is a field of artificial intelligence that enables machines to interpret and understand visual information from the world. " 
            "It involves the use of algorithms and deep learning models to analyze images and videos. AI systems use computer vision to replicate human vision and " 
            "make sense of visual data.\n"
            "\n"
            "          AI applications of computer vision are vast, ranging from object recognition and tracking to facial recognition and autonomous vehicles. " 
            "For example, self-driving cars use computer vision to perceive their surroundings and make real-time decisions.Affectiva is a leading player in this field, " 
            "providing emotion recognition software across diverse industries such as automotive, media, and education. Their technology can detect emotional cues from " 
            "individuals in real-time, making it invaluable for applications like automotive safety systems, media content optimization, and personalized education experiences.\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["how is ai used in recommendation systems","How is AI used in recommendation systems","how is artificial intelligence used in recommendation systems"]):
        bot_response = ("\n"
            "Artificial Intelligence (AI) has transformed various aspects of our lives, and one of its prominent applications is in recommendation systems. " 
            "These systems utilize AI algorithms to suggest products, services, or content tailored to individual preferences. In this article, we’ll delve into " 
            "the inner workings of recommendation systems, explore their types, and provide real-world examples of how AI enhances user experiences.\n"
            "\n"
            "Understanding Recommendation Systems\n"
            "\n"
            
            "At its core, a recommendation system employs machine learning algorithms to analyze user behavior and preferences. It then leverages this data to make " 
            "personalized suggestions. Here are the key types of recommendation systems:\n"
            "\n"
            "(1).Collaborative Filtering: This method recommends items based on the preferences and behaviors of similar users. For instance, if you enjoy watching the " 
            "same movies as someone else, the system will suggest movies they liked that you haven’t seen yet.\n"
            "(2).Content-Based Filtering: This approach suggests items similar to those a user has previously shown interest in. If you’ve been reading science fiction " 
            "books, the system may recommend more books in that genre.\n"
            "(3).Hybrid Approach: This combines the strengths of both collaborative and content-based filtering.\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["how does ai impact the automotive industry","how does artificial intelligence impact the automotive industry"]):
        bot_response = ("\n"
            "Artificial Intelligence (AI) has brought a revolution to the automotive industry. It’s not just about self-driving cars; AI’s influence " 
            "extends far beyond that. Here’s how AI is reshaping the automotive landscape:\n"
            "\n"
            "(1).AI in Autonomous Vehicles: AI plays a pivotal role in enabling self-driving cars to navigate, make decisions, and ensure passenger safety. " 
            "Through advanced sensors and machine learning algorithms, AI-powered vehicles can analyze their surroundings and react in real-time.\n"
            "(2).Enhanced Safety: AI-based driver-assistance systems are reducing accidents by providing features like lane-keeping assistance, adaptive " 
            "cruise control, and collision avoidance. These systems are like a digital co-pilot, making driving safer.\n"
            "(3).Predictive Maintenance: AI predicts when a vehicle needs maintenance, preventing breakdowns and reducing downtime. Sensors collect data "
            "on various parts of the vehicle, and AI algorithms analyze this data to schedule maintenance proactively.\n"
            "(4).Improved Fuel Efficiency: AI optimizes engine performance, transmission, and other vehicle systems to maximize fuel efficiency. " 
            "This not only saves money but also reduces emissions, making cars more environmentally friendly.\n"
            "(5).Personalized User Experience: AI tailors the in-car experience to individual preferences. From adjusting seat positions to selecting music "
            "and suggesting nearby restaurants, AI makes the driving experience more comfortable and enjoyable\n"
            "(6).Smart Traffic Management: AI helps in managing traffic by analyzing data from various sources, including GPS, traffic cameras, and sensors. " 
            "This data is used to optimize traffic flow, reduce congestion, and improve overall road efficiency.\n"
            "(7).Cost Reduction: Automakers are using AI-driven automation in manufacturing, leading to cost savings and increased productivity. Robots powered " 
            "by AI are performing tasks with precision and speed.\n"
            "\n"
        )
        
    elif match_keywords(user_input, ["can ai be used for predictive maintenance in manufacturing","can Artificial Intelligence be used for predictive maintenance in manufacturing"]):
        bot_response = ("\n"
            "Predictive maintenance is revolutionizing manufacturing processes. Artificial Intelligence (AI) plays a pivotal role in this transformative journey. " 
            "Here, we’ll explore how AI is reshaping predictive maintenance in the manufacturing sector.\n"
            "\n"
            "AI algorithms have the capability to analyze vast amounts of data generated by machinery and sensors. These algorithms can detect anomalies and predict when equipment " 
            "might fail. This proactive approach minimizes downtime and maintenance costs.\n"
            "\n"
        )
        
    else:
        try:
            bot_response = chat_with_gpt(user_input)
        except Exception as e:
            bot_response = f"Sorry! An error occurred: {e}"

    chat_area.config(state=tk.NORMAL)
    # Remove the typing indicator
    chat_area.delete("end-3l", "end-2l")
    chat_area.insert(tk.END, f"< Chatbot > : {bot_response}\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

# Set up the GUI
root = tk.Tk()
root.title("Chatbot with GPT and Tkinter")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_area.pack(padx=10, pady=10)
chat_area.insert(tk.END, "Chatbot: Hello How can I help you today? (Type 'exit' to quit)\n\n")
chat_area.config(state=tk.DISABLED)

entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(padx=10, pady=(0, 10))
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=(0, 10))

entry.focus()
root.mainloop()
