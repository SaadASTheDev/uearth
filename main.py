# Import libraries
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns  # for data visualization
import matplotlib.pyplot as plt  # to plot charts
from collections import Counter
import os
import netCDF4 as nc
import pandas as pd

'''
# Modeling Libraries
from sklearn.preprocessing import QuantileTransformer
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold, learning_curve, train_test_split
'''





datasetNetCDF = nc.Dataset(
    "/Users/surfaceLaptop2/Downloads/3B-DAY-E.MS.MRG.3IMERG.20000601-S000000-E235959.V06.nc4.nc4")

# convert netcdf file into csv
print(datasetNetCDF['precipitationCal'][:])
df = pd.DataFrame(datasetNetCDF['d'][:][0])
# df.to_csv('precipitationCal.csv', index=False)



