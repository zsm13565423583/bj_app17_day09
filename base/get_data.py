import yaml, os


class GetData:

    def get_yaml_data(self,yaml_name):
        with open("./data" + os.sep + yaml_name, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
