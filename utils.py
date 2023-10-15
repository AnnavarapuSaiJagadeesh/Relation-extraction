import json
def get_dataset(type="train", ds="semeval"):
    # texts = json.load(open(f"./{ds}/{type}_sentence.json", "r"))
    # /content/sample_data
    texts = json.load(open(f"/content/Relation-extraction/semeval/train_sentence.json","r"))
    # relations = json.load(open(f"./{ds}/{type}_label_id.json", "r"))
    relations = json.load(open(f"/content/Relation-extraction/semeval/train_label_id.json","r"))
    print(f"processing {type} dataset ...")
    return texts, relations