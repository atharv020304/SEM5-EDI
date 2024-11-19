import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer


with open('rf_classifier_job_recommendation.pkl', 'rb') as file:
    model = pickle.load(file)

with open('tfidf_vectorizer_job_recommendation.pkl', 'rb') as file:
    vectorizer = pickle.load(file)  


def cleanResume(txt):
    cleanText = re.sub(r'http\S+\s', ' ', txt)
    cleanText = re.sub(r'RT|cc', ' ', cleanText)
    cleanText = re.sub(r'#\S+\s', ' ', cleanText)
    cleanText = re.sub(r'@\S+', ' ', cleanText)
    cleanText = re.sub(r'[%s]' % re.escape(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub(r'\s+', ' ', cleanText)
    return cleanText


def job_recommendation(resume_text):
    clean_text = cleanResume(resume_text)
    resume_tfidf = vectorizer.transform([clean_text])
    prediction = model.predict(resume_tfidf)  
    return prediction



# input_text = '''
# Skills = [
#     'AWS', 'Azure', 'Google Cloud Platform', 'Docker', 'Kubernetes', 
#     'Terraform', 'Ansible', 'Chef', 'Puppet', 'Jenkins', 
#     'Git', 'GitLab', 'GitHub Actions', 'CircleCI', 
#     'Linux', 'Windows Server', 'Bash Scripting', 'PowerShell', 
#     'Python', 'Go', 'Ruby', 'JavaScript', 
#     'CI/CD Pipelines', 'Monitoring and Logging', 'Prometheus', 'Grafana', 
#     'ELK Stack', 'Splunk', 'CloudFormation', 
#     'Cloud Security', 'IAM', 'Firewall Management', 'Encryption', 
#     'Load Balancing', 'DNS', 'CDN', 'VPN', 'Virtual Private Cloud (VPC)', 
#     'Microservices Architecture', 'Service Meshes', 
#     'Configuration Management', 'Container Orchestration', 
#     'Serverless Architectures', 'API Management', 
#     'Relational Databases', 'NoSQL Databases', 
#     'Message Queues (RabbitMQ, Kafka)', 
#     'Performance Tuning', 'Disaster Recovery', 'Troubleshooting'
# ]

# Education = [
#     'Computer Science', 'Information Technology', 
#     'Software Engineering', 'Cloud Computing', 
#     'Networking', 'Cybersecurity', 'Data Science', 
#     'Systems Engineering', 'DevOps', 
#     'Applied Computing', 'IT Infrastructure Management', 
#     'Cloud Certifications (AWS, Azure, GCP)', 
#     'Database Management', 'Operations Research'
# ]

# '''


with open('resume_data.pkl','rb') as d :
    resume_data = str(pickle.load(d))



print((resume_data))
result = job_recommendation(resume_data)
print(result)



with open('models/rf_classifier_categorization.pkl','rb') as file1:
    model1 = pickle.load(file1)

with open('models/tfidf_vectorizer_categorization.pkl','rb') as file1:
    vectorizer1 = pickle.load(file1)




def predict_category(resume_text):
    clean_text = cleanResume(resume_text)
    resume_tfidf = vectorizer1.transform([clean_text])
    prediction = model1.predict(resume_tfidf)
    return prediction


input_text1 = ''' 
Skills = [
   Skills = [
    'Java', 'Kotlin', 'Android Studio', 'XML', 'Jetpack Compose', 
    'Firebase', 'REST APIs', 'SQLite', 'Room Database', 
    'UI/UX Design', 'Material Design', 'Version Control (Git)', 
    'Retrofit', 'Multithreading (Coroutines)', 'Android SDK', 
    'Google Play Store Deployment', 'Debugging', 'Performance Optimization'
]

Education = [
    'Computer Science', 'Software Engineering', 
    'Information Technology', 'Mobile App Development', 
    'Programming Certifications (Java, Kotlin)'
]

'''


res = predict_category(input_text1)
print(res)