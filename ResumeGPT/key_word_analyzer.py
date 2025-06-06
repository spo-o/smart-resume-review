from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text, top_n=30):
    vectorizer = CountVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    return set(vectorizer.get_feature_names_out())

def compare_keywords(resume_text, jd_text):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    missing_keywords = jd_keywords - resume_keywords
    common_keywords = resume_keywords & jd_keywords

    return {
        "resume_keywords": list(resume_keywords),
        "jd_keywords": list(jd_keywords),
        "common_keywords": list(common_keywords),
        "missing_keywords": list(missing_keywords),
    }
