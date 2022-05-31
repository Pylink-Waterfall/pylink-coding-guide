import yaml
from dacite import from_dict

from config_dataclass import ConfigModel


if __name__ == '__main__':
    config_file_name = "example_config.yaml"
    with open(config_file_name) as f:
        config_file = yaml.load(f, Loader=yaml.FullLoader)

    config_model = from_dict(data_class=ConfigModel, data=config_file)
    print(config_model)

