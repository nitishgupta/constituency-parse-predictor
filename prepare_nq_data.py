import gzip
import json
import glob

train_path = "/shared/nitishg/data/nq/v1.0/train/nq-train-??.jsonl.gz"

output_train = "/shared/nitishg/data/nq/train_questions.jsonl"


def write_questions(input_jsonlgz_glob, output_jsonl):
    input_paths = glob.glob(input_jsonlgz_glob)
    print(input_paths)

    lines_written = 0
    outf = open(output_jsonl, 'w')
    for input_path in input_paths:
        with gzip.open(input_path, 'rb') as f:
            for line in f:
                example = json.loads(line)
                question_tokens = example['question_tokens']
                question = " ".join(question_tokens)
                example_id = example['example_id']

                out_dict = {'sentence': question, 'sentence_id': example_id}
                outf.write(json.dumps(out_dict) + "\n")
                lines_written += 1
    outf.close()
    print("Lines written: {}".format(lines_written))


write_questions(train_path, output_train)









