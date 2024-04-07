import yaml


def load_yaml(path=r'D:\huace\webauto\data\user_data.yaml'):
    file = open(path, encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data
