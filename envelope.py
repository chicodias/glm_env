# envelope_glm
# recebe um modelo do sm e plota o respectivo envelope dos residuos
#
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.genmod.generalized_linear_model import GLM


def env_glm(model:GLMResults):

    # create an array with n 1s
    mt = np.ones(len(df))

    # create a matrix with the values of the variables
    X = df[fatores].values

    # join mt as first column of X
    X = np.column_stack((mt, X))
    # number of rows of X
    n = len(X)

    # number of columns of X
    p = len(X[0])

    # transpose of X
    X_t = X.T

    # matrix multiplication of X_t and X
    X_t_X = np.dot(X_t, X)

    # inverse of X_t_X
    X_t_X_inv = np.linalg.inv(X_t_X)

    # hat matrix of X
    # X%*%solve(t(X)%*%X)%*%t(X)
    H = np.dot(np.dot(X, X_t_X_inv), X_t)

    # diag of H matrix
    h = np.diag(H)

    infl = model.get_influence(observed=False)

    tsi = infl.resid_studentized

    # identity matrix of order n
    ident = np.identity(n)

    # matrix with n cols and 100 rows
    epsilon = np.zeros((n, 100))

    e = np.zeros((n, 100))

    # vector with n elements
    e1 = np.zeros(n)
    e2 = np.zeros(n)

    for i in range(100):
        epsilon[:, i] = np.random.normal(0,1,n)
        e[:, i] = np.dot((ident-H),epsilon[:, i])
        # create a diagonal matrix
        u = np.diagonal(ident - H)
        e[:,i] = e[:,i]/np.sqrt(u)
        # sort e[,i]
        e[:,i] = np.sort(e[:,i])

    for i in range(n):
        eo = np.sort(e[i,:])
        e1[i] = (eo[1]+eo[2])/2
        e2[i] = (eo[96]+eo[97])/2

    # mean of colums of e
    med = np.mean(e, axis=0)

    faixa = [np.min([tsi.values,e1,e2]),
            np.max([tsi.values,e1,e2])]

    # qqplot

    fig = sm.qqplot(tsi, line='45')
    fig = sm.qqplot(e1, ax = fig.axes[0],  color='#FFDD44')
    fig = sm.qqplot(e2, ax = fig.axes[0], linestyle='dashed')
    plt.ylim(faixa)
    fig.show()
