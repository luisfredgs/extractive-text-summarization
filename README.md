Extractive text summarization based on word frequencies and spacy.

# Starting

Firstly, you need download the general-purpose spacy pretrained models. Type this command for that: ```./download.sh```

Further, to makes a summary type the command: ```python summarization.py --language=portuguese --nb_sentences=2```

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