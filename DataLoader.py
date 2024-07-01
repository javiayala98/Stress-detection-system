import yaml
import os
import pandas as pd

class DataLoader:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        # load configuration file
        with open("./data_config.yaml") as f:
            #creamos la propiedad config y la rellenamos con los valores de data_config
            self.config = yaml.load(f, Loader=yaml.FullLoader)[dataset_name]

        self.users_chosen = self.config["users_chosen"]