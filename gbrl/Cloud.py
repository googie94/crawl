import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('카페글.csv')

df.head()

# # dimension
# df.shape

# # 결측치
# df.isnull().sum()

# # information
# df.info()

# # text 변수 확인
# df['text'][0]