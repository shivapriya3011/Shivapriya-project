resume_text = """
python machine learning data analysis numpy pandas sql deep learning
"""

job_description = """
looking for python developer with machine learning experience
knowledge in sql data analysis and deep learning required
"""
def preprocess(text):
    text = text.lower()
    words = text.split()
    return words
def word_frequency(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
def cosine_similarity(freq1, freq2):
    all_words = set(freq1.keys()).union(set(freq2.keys()))
    
    dot_product = 0
    magnitude1 = 0
    magnitude2 = 0
    
    for word in all_words:
        x = freq1.get(word, 0)
        y = freq2.get(word, 0)
        
        dot_product += x * y
        magnitude1 += x * x
        magnitude2 += y * y
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    return dot_product / ((magnitude1 ** 0.5) * (magnitude2 ** 0.5))
resume_words = preprocess(resume_text)
job_words = preprocess(job_description)

resume_freq = word_frequency(resume_words)
job_freq = word_frequency(job_words)

similarity_score = cosine_similarity(resume_freq, job_freq)

print("Similarity Score:", similarity_score)
missing_skills = []
for word in job_freq:
    if word not in resume_freq:
        missing_skills.append(word)

print("Missing Skills:", missing_skills)
