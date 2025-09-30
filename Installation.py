# # Block 1: Test pandas by creating a DataFrame and printing it
import pandas as pd
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print("Pandas DataFrame:")
print(df)
print("Pandas OK")

# # Block 2: Test numpy by creating an array and printing it
import numpy as np
arr = np.array([1, 2, 3])
print("Numpy array:")
print(arr)
print("Numpy OK")

# # Block 3: Test matplotlib by plotting a simple line and closing it
import matplotlib.pyplot as plt
plt.plot([0, 1], [0, 1])
plt.close()
print("Matplotlib OK")

# # Block 4: Test seaborn by plotting a histogram from a dummy DataFrame and closing it
import seaborn as sns
df_dummy = pd.DataFrame({'data': [1, 2, 2, 3, 3, 3]})
sns.histplot(df_dummy['data'])
plt.close()
print("Seaborn OK")

# # Block 5: Test scipy with a t-test using scipy.stats.ttest_1samp
import scipy.stats
t_stat, p_val = scipy.stats.ttest_1samp([1, 2, 3], 0)
print(f"Scipy t-test result: t_stat={t_stat}, p_val={p_val}")
print("Scipy OK")

# # Block 6: Test statsmodels with a small OLS regression
import statsmodels.api as sm
X = np.array([1, 2, 3])
y = np.array([2, 4, 6])
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(f"Statsmodels OLS params: {model.params}")
print("Statsmodels OK")

# # Block 7: Test scikit-learn with a LinearRegression on a small dataset
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2], [3]])
y = np.array([1, 2, 3])
model = LinearRegression().fit(X, y)
print(f"Scikit-learn LinearRegression coefficients: {model.coef_}")
print("Scikit-learn OK")