import sys
import yaml
from dispatch_model import load_plugin


if __name__ == "__main__":
    with open(sys.argv[1], "r") as plg_file:
        plg_dict = yaml.safe_load(plg_file)
    plg = load_plugin(plg_dict)
    print(plg.__class__)
    print(plg)
