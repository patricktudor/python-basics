# followed from AAAMLP by Abhishek Thakur

import pandas as pd
from sklearn import model_selection

if __name__ == "__main__":
    # training dataset is called train.csv
    df = pd.read_csv("train.csv")

    # new column filled with -1
    df["kfold"] = -1

    # randomise the rows
    df = df.sample(frac=1).reset_index(drop=True)

    # initiate kfold class from model_selection module
    kf = model_selection.KFold(n_splits=5)

    # populate new column
    for fold, (trn_, val_) in enumerate(kf.split(X=df)):
        df.loc[val_, 'kfold'] = fold

    # save file
    df.to_csv("train_folds.csv", index=False)
    