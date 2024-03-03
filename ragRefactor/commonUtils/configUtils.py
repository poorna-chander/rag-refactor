import yaml

def loadGlobalConfig():
    with open('./globalConfig.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config