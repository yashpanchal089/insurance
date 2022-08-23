from distutils.command.config import config
import os
import yaml
import pandas as pd
import numpy as np
import argparse
from pkgutil  import get_data
import configparser

from insurance.src.get_data import read_params

def load_and_save(config_path):
    config=read_params(config_path)
    df=get_data(config_path)
    new_cols=[col.replace(" ","_") for col in df.columns]
    print(new_cols)





if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    data=get_data(config_path=parsed_args.config)
