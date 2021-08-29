import numpy as np
import matplotlib.pyplot as plt

x = np.array([ 0.        ,  0.20408163,  0.40816327,  0.6122449 ,  0.81632653,
        1.02040816,  1.2244898 ,  1.42857143,  1.63265306,  1.83673469,
        2.04081633,  2.24489796,  2.44897959,  2.65306122,  2.85714286,
        3.06122449,  3.26530612,  3.46938776,  3.67346939,  3.87755102,
        4.08163265,  4.28571429,  4.48979592,  4.69387755,  4.89795918,
        5.10204082,  5.30612245,  5.51020408,  5.71428571,  5.91836735,
        6.12244898,  6.32653061,  6.53061224,  6.73469388,  6.93877551,
        7.14285714,  7.34693878,  7.55102041,  7.75510204,  7.95918367,
        8.16326531,  8.36734694,  8.57142857,  8.7755102 ,  8.97959184,
        9.18367347,  9.3877551 ,  9.59183673,  9.79591837, 10.        ])
y = np.array([ 0.85848224, -0.10657947,  1.42771901,  0.53554778,  1.20216826,
        1.81330509,  1.88362644,  2.23557653,  2.7384889 ,  3.41174583,
        4.08573636,  3.82529502,  4.39723111,  4.8852381 ,  4.70092778,
        4.66993962,  6.05133235,  5.44529881,  7.22571332,  6.79423911,
        7.05424438,  7.00413058,  7.98149596,  7.00044008,  7.95903855,
        9.96125238,  9.06040794,  9.56018295,  9.30035956,  9.26517614,
        9.56401824, 10.07659844, 11.56755942, 11.38956185, 11.83586027,
       12.45642786, 11.58403954, 11.60186428, 13.88486667, 13.35550112,
       13.93938726, 13.31678277, 13.69551472, 14.76548676, 14.81731598,
       14.9659187 , 15.19213921, 15.28195017, 15.97997265, 16.41258817])

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
regr=LinearRegression()
X=x.reshape(-1,1)
regr.fit(X,y)
Y=regr.predict(X)
plt.scatter(x,y)
plt.plot(x,Y)
plt.show()

w=regr.coef_
b=regr.intercept_

print("the linear regression is %f*x+%f"%(w,b))

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=20)
regr=LinearRegression()

X_train=x_train.reshape(-1,1)

regr.fit(X_train,y_train)
Y_train=regr.predict(X_train)
plt.scatter(x_train,y_train)
plt.scatter(x_train,Y_train)
plt.plot(x_train,Y_train)
plt.show()



X_test=x_test.reshape(-1,1)
Y_test=regr.predict(X_test)
plt.scatter(x_test,y_test)
plt.scatter(x_test,Y_test)
plt.plot(x_test,Y_test)
plt.show()

w=regr.coef_
b=regr.intercept_

print("the regression funcion is %f*x+%f"%(w,b))