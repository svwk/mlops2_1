#!python3

from catboost.datasets import titanic

train, test = titanic()

train.to_csv("/home/data-eng/projects/mlops2_1/data/raw/train.csv", index=False)

test.to_csv("/home/data-eng/projects/mlops2_1/data/raw/test.csv", index=False)
