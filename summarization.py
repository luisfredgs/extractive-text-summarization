import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
import argparse

def summarization(args):

    with open(args.original_text, "r", encoding="utf-8") as f:
        text = " ".join(f.readlines())

    if args.language == 'portuguese':
        import pt_core_news_sm
        nlp = pt_core_news_sm.load()
    else:
        import en_core_web_sm
        nlp = en_core_web_sm.load()
    
    
    doc = nlp(text)


    corpus = [sent.text.lower() for sent in doc.sents ]
    
    cv = CountVectorizer(stop_words=list(STOP_WORDS))   
    cv_fit=cv.fit_transform(corpus)    
    word_list = cv.get_feature_names();    
    count_list = cv_fit.toarray().sum(axis=0)    

    """
    The zip(*iterables) function takes iterables as arguments and returns an iterator. 
    This iterator generates a series of tuples containing elements from each iterable. 
    Let's convert these tuples to {word:frequency} dictionary"""

    word_frequency = dict(zip(word_list,count_list))

    val=sorted(word_frequency.values())

    # Check words with higher frequencies
    higher_word_frequencies = [word for word,freq in word_frequency.items() if freq in val[-3:]]
    print("\nWords with higher frequencies: ", higher_word_frequencies)

    # gets relative frequencies of words
    higher_frequency = val[-1]
    for word in word_frequency.keys():  
        word_frequency[word] = (word_frequency[word]/higher_frequency)


    # SENTENCE RANKING: the rank of sentences is based on the word frequencies
    sentence_rank={}
    for sent in doc.sents:
        for word in sent :       
            if word.text.lower() in word_frequency.keys():            
                if sent in sentence_rank.keys():
                    sentence_rank[sent]+=word_frequency[word.text.lower()]
                else:
                    sentence_rank[sent]=word_frequency[word.text.lower()]
            else:
                continue

    top_sentences=(sorted(sentence_rank.values())[::-1])
    top_sent=top_sentences[:args.nb_sentences]

    # Mount summary
    summary=[]
    for sent,strength in sentence_rank.items():  
        if strength in top_sent:
            summary.append(sent)

    # return orinal text and summary
    return text, summary


if __name__ == '__main__':        

    parser = argparse.ArgumentParser(description='Extractive text summarization')

    parser.add_argument('--nb_sentences', dest='nb_sentences',
                    default=3, type=int, help='Number of sentences in summary (default: 3)')

    parser.add_argument('--original_text', dest='original_text',
                    default="original_text.txt", help='Path to original text')
    
    parser.add_argument('--language', dest='language',
                    default="portuguese", help='Language of summary. Supports portuguese or english')
    
    args = parser.parse_args()

    text, summary = summarization(args)

    # Print summary
    print("\n")
    print("Original text: \n", text)

    print("\nSummary:")

    for i in summary:
        print(i,end=" ")