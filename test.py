X_TEST = [[10, 20, 30]]
with open ('model.json','r')as f:
  content=f.read()
  model= loads(content)
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))
