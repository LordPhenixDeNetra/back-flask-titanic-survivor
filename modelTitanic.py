import numpy as np
import pandas as pd
from flask import jsonify
from sklearn.neighbors import KNeighborsClassifier


def learn_model():
    titanic = pd.read_excel("static/dataset/titanic_.xls")
    # return titanic.head()
    titanic = titanic[["pclass", "survived", "sex", "age"]]
    titanic.dropna(axis=0, inplace=True)
    titanic['sex'].replace(['male', 'female'], [0, 1], inplace=True)
    model = KNeighborsClassifier()
    y = titanic['survived']
    x = titanic.drop("survived", axis=1)
    model.fit(x, y)
    model.score(x, y)
    return model


def survie(pclass=1, sex=1, age=25):
    # model_ = learn_model()
    x_ = np.array([pclass, sex, age]).reshape(1, 3)
    #     print(model.predict(x))
    if learn_model().predict(x_)[0] == 0:
        # return "Tu ne surverait pas !"
        return jsonify({'survie': "No"})

    else:
        # return "Tu surverait !"
        return jsonify({'survie': "Yes"})
