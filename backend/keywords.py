from keybert import KeyBERT

kw_model = KeyBERT()

def keyword(script):
    
    keywords = kw_model.extract_keywords(script, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=5)
    return keywords