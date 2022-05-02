from sklearn.linear_model import LinearRegression

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)
X_TEST = [[10, 20, 30]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))
with open('input.data.json') as f:
  content=f.read()
  TRAIN_INPUT=loads(content)
with open('output.data.json') as f:
  content=f.read()
  TRAIN_OUTPUT=loads(content)
