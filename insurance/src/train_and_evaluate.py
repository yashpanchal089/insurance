from distutils.command.config import config
from email import header
import encodings
import os
# from insurance.src.get_data import read_params
import yaml
import pandas as pd
import numpy as np
import argparse
from pkgutil import get_data
import configparser
from get_data import read_params, get_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, meadn_squared_error, r2_score
from sklearn.linear_model import ElasticNet
import joblib

def train_and_evaluate(config_path):
    config=read_params(config_path)
    test_data_path=config["split_data"]["test_path"]
    train_data_path=config["split_data"]["train_path"]
    random_state=config["base"]["random_state"]
    model_dir=config["model_dir"]
    alpha=config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio=config["estimators"]["ElasticNet"]["params"]["l1_ratiom"]
    target=[config["base"]["target_col"]]
    train=pd.read_csv(train_data_path,sep=",")
    test=pd.read_csv(test_data_path,sep=",")
    train_y=train[target]
    test_y=test[target]

    train_x=train.drop(target, axis=1)
    test_x=train.drop(target, axis=1)

    lr=ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)

    lr.fit(train_x, train_y)

    predicted_quality=lr.predict(test_x)

    (rmse,mae,r2) = eval_metrics(test_y, predicted_quality)

    print("ElasticNet Model(alpha=%f, l1_ratio=%f):"%(alpha,l1_ratio))
    print("RMSE:%s", %rmse)
    print("MAE:%s", %mae)
    print("R2_score:%s",%r2)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args=args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)