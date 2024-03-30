# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Load datasets
# train_dataA = pd.read_csv('Dataset/comp_datasets_train/region_A_train.csv')
# train_dataB = pd.read_csv('Dataset/comp_datasets_train/region_B_train.csv')
# train_dataC = pd.read_csv('Dataset/comp_datasets_train/region_C_train.csv')
# train_dataD = pd.read_csv('Dataset/comp_datasets_train/region_D_train.csv')
# train_dataE = pd.read_csv('Dataset/comp_datasets_train/region_E_train.csv')
#
# test_dataA = pd.read_csv('Dataset/comp_datasets_test/region_A_test.csv')
# test_dataB = pd.read_csv('Dataset/comp_datasets_test/region_B_test.csv')
# test_dataC = pd.read_csv('Dataset/comp_datasets_test/region_C_test.csv')
# test_dataD = pd.read_csv('Dataset/comp_datasets_test/region_D_test.csv')
# test_dataE = pd.read_csv('Dataset/comp_datasets_test/region_E_test.csv')
#
# solution_train = pd.read_csv('Dataset/comp_datasets_train/solution_train.csv')
#
# solution_format = pd.read_csv('Dataset/comp_datasets_train/solution_format.csv')
#
# all_train_data = pd.concat([test_dataA, test_dataB, test_dataC, test_dataD, test_dataE])
#
# all_train_data.info()  # Data types, missing values
# all_train_data.describe()  # Statistics for each feature
#
# all_train_data.hist(figsize=(10, 6))  # Creates histograms for all numerical columns
# plt.show()
#
#
# from sklearn.metrics import accuracy_score
#
# y_true = validation_set['label']  # Assuming 'label' is the true weather
# y_pred = model.predict(validation_set[features])
#
# accuracy = accuracy_score(y_true, y_pred)
# print(accuracy)
#
#
#
#
#
#
#
#
#
#
