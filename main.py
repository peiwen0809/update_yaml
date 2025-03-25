import configparser
from ruamel.yaml import YAML
import traceback

def set_nested_dict_value(data_dict, path, value):
    keys = path.split('.')
    for idx, key in enumerate(keys[:-1]):
        if key.isdigit():
            key = int(key)
        elif key == '*':
            # print(data_dict)
            for sub_key in range(len(data_dict)):
                # print(sub_key)
                set_nested_dict_value(data_dict[sub_key], '.'.join(keys[idx+1:]), value)
            return
        try:
            data_dict = data_dict[key]
        except KeyError as e:
            # print("Skip Key: " + str(e))
            # print("Current path: " + path)
            # traceback.print_exc()
            return
        
    last_key = keys[-1]
    if last_key.isdigit():
        last_key = int(last_key)
    data_dict[last_key] = value

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('settings.ini')

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 500

    for section in config.sections():
        yaml_file = section.split(".")[-1] + ".yml"
        with open(yaml_file, 'r') as file:
            yaml_data = yaml.load(file)

        for key, value in config.items(section):
            set_nested_dict_value(yaml_data, section + "." + key, value)

        # 回寫 YAML 文件
        with open(yaml_file, 'w') as file:
            yaml.dump(yaml_data, file)
    
        print(f"{yaml_file} 文件更新完成。")
    input("按任意鍵結束...")
