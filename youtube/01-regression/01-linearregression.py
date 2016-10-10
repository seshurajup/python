import ConfigParser
import quandl
import pandas as pandas
import math as math
import numpy as numpy

from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

config = ConfigParser.ConfigParser()
config.readfp(open("config/config.ini"))
quandlKey = config.get("quandl", "key")

quandl.ApiConfig.api_key = quandlKey
googleStock = quandl.get("WIKI/GOOGL")

# columns
# date  Open    High     Low    Close      Volume  Ex - Dividend   Split Ratio  Adj. Open  Adj. High   Adj. Low  Adj. Close

googleStock = googleStock[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

googleStock["HL_PCT"] = (googleStock["Adj. High"] - googleStock["Adj. Close"])/googleStock["Adj. Close"] * 100.0
googleStock["PCT_change"] = (googleStock["Adj. High"] - googleStock["Adj. Open"])/googleStock["Adj. Open"] * 100.0

googleStock = googleStock[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

#missing data 
googleStock.fillna(-99999, inplace = True)


#set label for regression 
daysToPredict = int(math.ceil(0.01 * len(googleStock)))
forecastColumn = "Adj. Close"
googleStock['label'] = googleStock[forecastColumn].shift( - daysToPredict)



features = numpy.array(googleStock.drop(['label'], 1))
#scale the values
features = preprocessing.scale(features)
featurePredict = features[-daysToPredict:]
features = features[:-daysToPredict]
#remove rows if empty data
googleStock.dropna(inplace = True)

labels = numpy.array(googleStock['label'])

print(len(features),len(labels))
#build train and validation set for model
featureTrain, featureTest, labelTrain, labelTest = cross_validation.train_test_split(features, labels, test_size=0.2)
print(len(featureTrain),len(featureTest),len(labelTrain),len(labelTest))

print(numpy.isnan(featureTrain).any(),numpy.isnan(labelTrain).any(),numpy.isnan(featureTest).any(),numpy.isnan(labelTest).any())

#build linear regression model
linearRegressionModel = LinearRegression(n_jobs=-1)
linearRegressionModel.fit(featureTrain, labelTrain)
accuracy = linearRegressionModel.score(featureTest, labelTest) * 100.0
print("linear regression model with accuracy ",accuracy," by predicting future ",daysToPredict," days")
print("linear predict ",linearRegressionModel.predict(featurePredict))

#build svn linear model
svnModel = svm.SVR()
svnModel.fit(featureTrain, labelTrain)
accuracy = svnModel.score(featureTest, labelTest) * 100.0
print("svn linear model with accuracy ",accuracy," by predicting future ",daysToPredict," days")
print("svn linear predict ",svnModel.predict(featurePredict))

#build svn polynomial model 
svnModel = svm.SVR(kernel='poly')
svnModel.fit(featureTrain, labelTrain)
accuracy = svnModel.score(featureTest, labelTest) * 100.0
print("svn polynomial model with accuracy ",accuracy," by predicting future ",daysToPredict," days")
print("svn polynomial  predict ",svnModel.predict(featurePredict))