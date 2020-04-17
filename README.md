Extractive text summarization based on word frequencies and spacy.

# Starting

Firstly, a necessary step is downloading the general-purpose spacy pre-trained models. Type this command: ```./download.sh```

Next, type the following command to makes a summary:   
```python summarization.py --language=portuguese --nb_sentences=2```

# Usage

```
usage: summarization.py [-h] [--nb_sentences NB_SENTENCES]
                        [--original_text ORIGINAL_TEXT] [--language LANGUAGE]

Extractive text summarization

optional arguments:
  -h, --help            show this help message and exit
  --nb_sentences NB_SENTENCES
                        Number of sentences in summary (default: 3)
  --original_text ORIGINAL_TEXT
                        Path to original text
  --language LANGUAGE   Language of summary. Supports portuguese or english
```