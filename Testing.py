# Trial import and minimal usage for common data science libraries

# Pandas
try:
    import pandas as pd
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    print("Pandas DataFrame:\n", df)
    print("Pandas OK")
except ImportError as e:
    print("Pandas NOT installed:", e)
except Exception as e:
    print("Pandas error:", e)

# Numpy
try:
    import numpy as np
    arr = np.array([1, 2, 3])
    print("Numpy array:", arr)
    print("Numpy OK")
except ImportError as e:
    print("Numpy NOT installed:", e)
except Exception as e:
    print("Numpy error:", e)

# Matplotlib
try:
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("Matplotlib Test Plot")
    plt.close()  # Do not display plot in script, just ensure it works
    print("Matplotlib OK")
except ImportError as e:
    print("Matplotlib NOT installed:", e)
except Exception as e:
    print("Matplotlib error:", e)

# Seaborn
try:
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.DataFrame({'total_bill': [10, 20, 15, 30, 25, 18, 22]})
    _ = sns.histplot(df["total_bill"])
    plt.close()
    print("Seaborn OK")
except ImportError as e:
    print("Seaborn NOT installed:", e)
except Exception as e:
    print("Seaborn error:", e)

# Scipy
try:
    from scipy import stats
    t_stat, p_val = stats.ttest_1samp([1, 2, 3, 4, 5], 3)
    print("Scipy t-test:", t_stat, p_val)
    print("Scipy OK")
except ImportError as e:
    print("Scipy NOT installed:", e)
except Exception as e:
    print("Scipy error:", e)

# Statsmodels
try:
    import statsmodels.api as sm
    import numpy as np
    X = np.arange(10)
    y = X + np.random.normal(size=10)
    X_const = sm.add_constant(X)
    model = sm.OLS(y, X_const).fit()
    print("Statsmodels OLS params:", model.params)
    print("Statsmodels OK")
except ImportError as e:
    print("Statsmodels NOT installed:", e)
except Exception as e:
    print("Statsmodels error:", e)

# Scikit-learn
try:
    from sklearn.linear_model import LinearRegression
    import numpy as np
    X = np.array([[1], [2], [3]])
    y = np.array([1, 2, 3])
    lr = LinearRegression().fit(X, y)
    print("Scikit-learn coef:", lr.coef_)
    print("Scikit-learn OK")
except ImportError as e:
    print("Scikit-learn NOT installed:", e)
except Exception as e:
    print("Scikit-learn error:", e)