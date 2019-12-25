import yaml

with open("./values02.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print(data)

