# AllenNLP Constituency Parser Predictor

This runs from the branch `conparse`,
 in the fork `nitishgupta/allennlp:conparse`
 
To use this, the data is to be provided in a jsonl format with keys:

1. "sentence": str containing white-space tokenized text
2. "sentence_id": int (optional) the id for the sentence

Output will be written in a Jsonl file with keys:
1. "tokens": list of tokens in the sentence
2. "sentence_id": sentence id of the input
3. "spans": List of 4-tuple, (start, exclusive-end, span_str, label-str)

Example command to run:
```
allennlp predict --output-file output.jsonl \
    --batch-size=1 --predictor my-constituency-parser \
    --include-package predictor --silent \
    https://allennlp.s3.amazonaws.com/models/elmo-constituency-parser-2018.03.14.tar.gz \
    sample.jsonl
```