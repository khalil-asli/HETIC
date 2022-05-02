from sklearn.linear_model import LinearRegression
from json import dumps

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

with open('input.data.json') as f:
  content=f.read()
  TRAIN_INPUT=loads(content)
with open('output.data.json') as f:
  content=f.read()
  TRAIN_OUTPUT=loads(content)
