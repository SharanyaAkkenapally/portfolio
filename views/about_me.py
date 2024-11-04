import streamlit as st
import streamlit.components.v1 as components
# from forms.contact import contact_form
from pathlib import Path
import time



# --- HERO SECTION ---
col1, col2 = st.columns([0.3, 0.7], gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/6.png", width=200)

with col2:
    st.title("Hello👋...I'm Sharanya Akkenapally", anchor=False)
    st.write("**🧠 AI Engineer | 👨🏻‍💻 Data Scientist  | 🤖 ML Engineer**")

    # Display social media icons    
    st.markdown("""
        <a href='https://www.linkedin.com/in/SharanyaAkkenapally/'>
        <img src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000" alt="LinkedIn Profile" style="width:42px;height:42px;">
        </a>  |
        <a href="https://github.com/SharanyaAkkenapally">
        <img src="https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg" alt="GitHub Profile" style="width:42px;height:42px;">
        </a>
    """, unsafe_allow_html=True)
    st.write("\n")
    # Create columns for buttons within the second column
    button_col1, button_col2 = st.columns([0.2  , 0.8], gap="small")

    # Resume download button in the first button column
    with button_col1:
        with open("assets/Sharanya_CV.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume",
                data=pdf_file,
                file_name="Sharanya's Resume.pdf",
                mime="application/pdf"
            )

st.write("**sharanyaakkenapally@gmail.com**")

st.write("\n")
st.write("\n")
st.write("\n")

# About Me Section
st.subheader("About Me 🌟", anchor=False)
st.markdown("""
    <hr style="margin-top: 1px; margin-bottom: 10px; border: 1px solid #ccc;">
""", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: justify;">
    I’m an enthusiastic Data Scientist with a strong foundation in Machine Learning, Deep Learning, Natural Language Processing (NLP), and Generative AI, including expertise in developing and deploying Large Language Models (LLMs). With a technical toolkit that includes Python, SQL, Data Visualization, and cloud platforms like AWS and Azure, I’m passionate about leveraging data science to drive impactful solutions. My experience spans across building predictive models, designing scalable data pipelines, and creating AI-driven applications that solve real-world challenges in innovative ways. My approach to data science is driven by curiosity and a commitment to continuous learning. I’m particularly excited about how Generative AI and cloud technologies are transforming industries and am eager to be part of that change by designing solutions that are both scalable and ethically responsible. <br> Outside of my technical work, I enjoy connecting with the AI and data science community, staying updated with the latest advancements, and sharing insights on how we can collectively advance the field. Whether it’s through collaboration or tackling new challenges, I’m always looking to make a meaningful impact with data and AI. As I grow in this field, I aim to be an active member of the AI community, sharing insights, contributing to open-source projects, and staying current with the latest advancements. Ultimately, I am driven by a vision to harness AI's potential to enhance understanding and create solutions that make a difference in the way we interact with data. Let’s connect if you’d like to discuss collaboration, data-driven innovation, or simply share insights on the future of AI!
    </div>
""", unsafe_allow_html=True)

st.write("\n")
st.write("\n")

# Education
st.subheader("Education 📚", anchor=False)
st.markdown("""
    <hr style="margin-top: 1px; margin-bottom: 10px; border: 1px solid #ccc;">
""", unsafe_allow_html=True)
st.write("""
         - **Master of Applied Computer Science**  -  Concordia University, Montreal, Canada (September 2022 - April 2024)
         - **B. Tech in Information Technology**  -  Sreenidhi Institute of Science and Technology, Hyderabad, India (August 2018 - July 2022)
         """)

# Skills
st.subheader("Skills ⚙️", anchor=False)
st.markdown("""
    <hr style="margin-top: 1px; margin-bottom: 10px; border: 1px solid #ccc;">
""", unsafe_allow_html=True)
st.write("""
- ***Programming languages***: C, Data Structures, C++, Python, R, Java, HTML, CSS, and JavaScript.
- ***Machine Learning***: PyTorch, Hugging Face, Deep learning, Transformers, LLM Fine Tuning, Keras, TensorFlow, Scikit-learn, SpeechBrain, MLOps, OpenCV, CUDA
- ***Data Visualization & Analysis***: Tableau, Power BI, R-Studio, Matplotlib, Scipy, Seaborn, Plotly, Pandas, Numpy
- ***Big Data & Databases***:  SQL, NoSQL (Couchbase, ElasticSearch)
- ***Cloud & DevOps***:  Azure AI, AWS (Sagemaker), Oracle cloud (OCI), Docker, Kubernetes, CI/CD, HQL, HBase, Pyspark, Git, Flask, Streamlit  
""")


# Work Experience
st.subheader("Work Experience 💼", anchor=False)
st.markdown("""
    <hr style="margin-top: 1px; margin-bottom: 10px; border: 1px solid #ccc;">
""", unsafe_allow_html=True)
# Cognizant
with st.expander("**Data Science Intern**, Hyderabad, India (Mar - Jun, 2022)"):
    st.write("""
- Collaborated cross-functionally with data engineers and product managers, ensuring scalable data pipelines for seamless integration and utilizing agile development methodologies, promoting iterative progress.
- Developed end-to-end fraud detection systems using LSTM-based RNNs with attention mechanisms, improving detection accuracy by 15%.
- Designed scalable ML pipelines for large-scale dataset, automated workflows using Python and SQL including,  reducing deployment time by 30%, conducting ongoing testing to ensure continuous optimization.
- Managed infrastructure with Docker, Kubernetes, and cloud-native tools, deploying and monitoring models at scale using CI/CD pipelines via Git.
- Implemented ETL processes and MLOps to streamline data flow, enhance scalability, and ensure real-time reporting for analytics.
- Created Power BI dashboards to communicate actionable insights to non-technical stakeholders and to monitor KPIs, enhancing data-driven decisions aligned with business needs.
""")


# Technocolabs Softwares Inc
with st.expander("**Technocolabs Softwares Inc, Data Science Intern**, Hyderabad, India (May - August, 2021)"):
    st.write("""
- Enhanced model accuracy by 15% through data augmentation techniques and temporal transformations.
- Developed feature engineering workflows using AWS and Pyspark to efficiently manage large-scale datasets.
- Achieved 85% classification accuracy in time series forecasting for stock price prediction using Logistic Regression, SVM, and optimized models via Grid/Random Search.
- Proficient in SQL for querying relational databases, data extraction, data wrangling, and performing complex aggregations, and EDA for identifying patterns. 
- Utilized Python and R for data preprocessing, data wrangling, data analytics, predictive modeling, feature engineering, and conducted statistical analysis and model evaluation to ensure accuracy and reliability.
- Built interactive dashboards with Tableau to support strategic decision-making and effectively communicate insights, and employed Bayesian inference models to enhance decision-making efficiency by 30%.
""")

# The Sparks Foundation
with st.expander("**The Sparks Foundation, Data Science and Analytics Intern**, Remote, India (January - August, 2022)"):
    st.write("""
- Processed text data using Natural Language Processing (NLP) techniques such as tokenization and word embeddings to generate high-quality feature vectors, enabling accurate classification.
- Performed descriptive analytics by extracting, exploring, and analyzing large datasets from multiple sources.
- Designed and implemented a spam detection model with Support Vector Machine (SVM), achieving a 92% accuracy rate by fine-tuning hyperparameters through Grid Search for optimal performance.
- Visualized performance metrics and model outcomes using Matplotlib and Seaborn, presenting clear insights into model effectiveness and identifying key areas for further optimization in spam detection.
""")

# SmartBridge Pvt Ltd
with st.expander("**SmartBridge Pvt Ltd, ML Engineer Intern**, Hyderabad, India     (May - August, 2020)"):
    st.write("""
- Developed a CNN-based algorithm for real-time skin disease detection using supervised models for classification, utilizing OpenCV for image preprocessing and feature extraction in healthcare data analysis.
- Engineered CNN architecture with Max-Pooling, Conv2D, Batch Normalization, and Dropout to enhance feature capture and prevent overfitting.
- Enhanced the model by integrating Transfer Learning, fine-tuning a ResNet-50 architecture, reducing training time by 22% and boosting model accuracy by 4%. 
- Deployed the CNN model using Flask, implementing RESTful APIs for real-time image analysis, and asynchronous processing to manage high user traffic, resulting in a scalable and responsive web application.
             """)
    

# Publications
st.subheader("Publications 📰", anchor=False)
st.markdown("""
    <hr style="margin-top: 1px; margin-bottom: 10px; border: 1px solid #ccc;">
""", unsafe_allow_html=True)
st.write("""
- **Co-authored book chapter**: *Post-COVID Impact on Skin Allergies* (Book Title: *[Data Science Applications of Post-COVID-19 Psychological Disorders](https://novapublishers.com/shop/data-science-applications-of-post-covid-19-psychological-disorders/)*)
- **An Intelligent TLDR Software for Summarization** – IJRASET ([DOI: 10.22214/ijraset.2022.44508](https://doi.org/10.22214/ijraset.2022.44508))
- **Predictive Analytics of BMI using CNN** – JMPAS ([DOI: 10.22270/jmpas.V10I6.1656](https://doi.org/10.22270/jmpas.V10I6.1656))
""")
    

# Function to create a project tile with justified text and buttons
def create_project_tile(column, image_path, title, description):
    with column:
        st.image(image_path, use_column_width=True)
        st.markdown(
            f"""
            <div style="background-color:#1e1e1e; padding:20px; border-radius:10px; color:white;">
                <h4 style="color:#66b2ff; margin-bottom: 10px;">{title}</h4>
                <p style="color:#e0e0e0; text-align: justify;">{description}</p>
            </div>
            <br>
            """, unsafe_allow_html=True
        )


# Projects Section
st.subheader("Projects 💻", anchor=False)
st.markdown("""
    <hr style="margin-top: 1px; margin-bottom: 10px; border: 1px solid #ccc;">
""", unsafe_allow_html=True)
st.write("\n")

# Creating a 3 by 3 grid for the project tiles
rows = [st.columns(3) for _ in range(3)]

# First Row
create_project_tile(rows[0][0], "assets/TTS.png", "Transformer based TTS System", 
    """Developed a Transformer-based Text-to-Speech (TTS) model with the LJSpeech dataset, improving speech quality and performance using the SpeechBrain framework. Accelerated training using CUDA, cuDNN, and GPU optimizations, achieving 2.5x faster speeds than Tacotron2. Experience in distributed training and optimization of language models to solve resource allocation to enhance model efficiency. Applied scaled positional encodings and teacher forcing, reducing Mel Error to 8.27e-02 and lowering Stop Error by 10%. Enhanced efficiency with dynamic batching and Noam Scheduler for more natural and fluid speech synthesis. """)

create_project_tile(rows[0][1], "assets/ds.jpg", "Dialogue Summarization: Fine Tuning LLM using Prompt Engineering and PEFT", 
    """I Explored and Fine-tuned FLAN-T5 Language Model from Hugging Face for  dialogue summarization using prompt engineering and zero/few-shot learning to improve adaptability for LLM-based solution. Applied PEFT (LoRA), updating just 2-12% of parameters, reducing model size for fine-tuning and optimizing the LLM. Improved ROUGE-1 by 17.47% and ROUGE-2 by 8.73% over human baseline summaries, ensuring efficient compression and accuracy. """)

create_project_tile(rows[0][2], "assets/retail-and-consumer-goods-mobile.gif", "Automated Retail Product Classification using CNN", 
    """I Designed CNN architectures (ResNet-18, GoogleNet, AlexNet) to classify grocery products, addressing class imbalance with weighting and oversampling. Performed data augmentation, model scaling and utilized grid search for hyperparameter optimization, fine-tuning learning rates, batch sizes, and dropout rates with focus on complexity analysis and enhancing performance metrics. Leveraged transfer learning by fine-tuning ResNet-18 with pre-trained ImageNet weights, resulting in an 8% increase in classification accuracy.""")

# Second Row
create_project_tile(rows[1][0], "assets/Image.jpg", "A Diagnostic Assistant for Post-Covid Skin Allergies",
    """I Led research on the predictive modeling of post-Covid skin allergies using image processing, focusing on forecasting disease severity. Employed a combination of ensemble methods with Neural Networks, including Gradient Boosting, AdaBoost, and XGBoost, to improve model accuracy and robustness. Achieved 89% classification accuracy, with XGBoost outperforming other models, offering a more reliable assessment of disease severity, thus significantly improving the model's and predictive capabilities.""")



st.write("\n")

# Certifications and Achievements
st.subheader("Certifications and Achievements 🏅", anchor=False)
st.markdown("""
    <hr style="margin-top: 1px; margin-bottom: 10px; border: 1px solid #ccc;">
""", unsafe_allow_html=True)
st.write("""
- Oracle Cloud Infrastructure Generative AI Professional certification – Oracle Cloud
- Machine Learning certification - Stanford University
- The Data Scientist toolbox - John Hopkins University
- AWS Academy- Cloud Foundations course - Amazon
- Generative AI with LLMs - Coursera
- Won the Silver Award at Ennovate - The International Innovation Show, Poland, 2021.
- Received the AWS Academy Graduate Badge for completing the AWS Academy Cloud Foundations course.
""")



# Extra-Curricular Activities
st.subheader("Activities and Societies 🌐🤝", anchor=False)
st.markdown("""
    <hr style="margin-top: 1px; margin-bottom: 10px; border: 1px solid #ccc;">
""", unsafe_allow_html=True)
# Volunteer Team Leader
with st.expander("**Volunteer Team Leader, ConUHacks VIII, Concordia University**,  (Jan 2024)"):
    st.write("""
    As a volunteer team leader at ConUHacks VIII, Quebec’s largest hackathon hosted by Concordia University, I effectively coordinated and managed activities, showcasing strong leadership, task assignment, and communication skills. I contributed significantly to the overall success of the event by fostering a collaborative team environment, addressing issues promptly, and ensuring a positive experience for participants, sponsors, and executives.
""")

# The Techvision Club
with st.expander("**The Techvision Club**,  (Aug 2020 – Sep 2022)"):
    st.write("""
    Served as the President of the Techvision Club. Spearheaded the Focus on Research (FOR) initiative, guiding students in enhancing research projects and facilitating research publication. Took an initiative and developed the club’s first website, organized technical events such as Workshops, Hackathons, and Quizzes by collaborating with organizations and hosted webinars on AI, Data Science and Web development with industry professionals.
""")

# AIESEC in Hyderabad
with st.expander("**AIESEC in Hyderabad**,  (Aug 2020 – Jan 2021)"):
    st.write(""" 
Volunteered as Junior Marketing Manager and Junior Manager for Incoming Social Sector. Contributed to content writing, partnership building, market research, graphic design, and data management. Facilitated business meetings with professionals and supported global internship exchange programs.
""")
