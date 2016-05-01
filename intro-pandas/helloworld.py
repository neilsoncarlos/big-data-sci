__author__ = 'neilson.ramalho'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.Series([1,3,5, np.nan, 23])
datas = pd.date_range('20160101', periods=6)

print("hi pandas")