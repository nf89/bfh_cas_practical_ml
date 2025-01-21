"""
    Useful functions for example notebooks and workshop solutions
    of course Practical Machine Learning - Supervised Learning
    Bern University of Applied Sciences (BFH)
"""


# ========== Packages ==========

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ========== Functions ==========

def prep_data(dataset, target, train_ratio = 2 / 3, seed = None, sep = ','):
    """ read and prepare real data from the current directory
    performs 
        read data
        features - target - split
        train - test - split

    Parameters
    ----------
    dataset: name of dataset in csv format
    target: name of target column
    train_ratio (2 / 3): (optional)
    seed (None): random seet for split (optional)
    sep (,): separator of csv file (optional)

    Returns
    -------
    X_train: feature matrix of train set
    X_test: target vector of train set
    y_train: feature matrix of test set
    y_test: target vector of train set
    """

    ## load data
    data = pd.read_csv(dataset, sep = sep)

    ## features - target - split
    X = data.drop(target, axis=1)
    y = data[target]

    ## train - test - split
    from sklearn.model_selection import train_test_split
    return train_test_split(
        X,
        y,
        train_size=train_ratio,
        random_state=seed)
    


def prep_demo_data(dataset, target):
    """ read demo data from the current directory
    performs 
        read data
        features - target - split

    Parameters
    ----------
    dataset: name of dataset in csv format, ',' separated
    target: name of target column

    Returns
    -------
    X: feature matrix
    y: target vector
    """

    ## load data
    data = pd.read_csv(dataset)
    
    ## features - target - split
    X = data.drop(target, axis=1)
    y = data[target]
    
    return X, y   



def inspect_decision_tree_model(model_def, features, target, figsize=(6, 6)):
    """ train a DecisionTreeClassifier and visualize the tree
    
    prints some motel attributes from within the function
    
    Parameters
    ----------
    model_def: DecisionTreeClassifier object with set parameters
    features: feature matrix
    target: target vector
    figsize: size of image, optional, default = (6, 6)
    
    Returns
    -------
    visualization of the trained tree
    prints model attributes
    """
    
    from sklearn.tree import plot_tree
    
    model = model_def
    model.fit(features, target)

    print('TREE DIAGNOSTICS:')
    print('depth  :', model.get_depth())
    print('leaves :', model.get_n_leaves())
    print('score  :', model.score(features, target))

    plt.figure(figsize=figsize)
    plot_tree(model,
              feature_names=features.columns,
              class_names=model.classes_,
              filled=True);



def test_regression_model(model, X_train, y_train, X_test, y_test, show_plot=True):
    
    """ shows behavoiur of univariate ML regression on synthetic dataset
    
    performs
    -   training on train data
    -   prediction on test data
    -   calculate performance measures
 
    Parameters
    ----------
    model: a parametrized regression model
    X_train, y_train: train data
    X_test, y_test: test data
    show_plot: show scatterplot ov pred vs true, optional, default=True
    

    Returns
    -------
    shows a scatterplot von X_test vs X_pred with a diagonal line, indicating identity
    prints r2_score and mean_squared_error
    
    """

    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error

    model = model
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print('R2 = %0.4f' %(r2_score(y_test, y_pred)))
    
    if show_plot == True:
        plt.figure(figsize=(6,6))
        ax = sns.scatterplot(x=y_test, y=y_pred)
        ax.set(xlabel='y_test', ylabel='y_pred')
        ls = np.linspace(min(y_test), max(y_test), 100)
        plt.plot(ls, ls, color='black', linestyle='dashed')
        ax.set_title(model.__class__.__name__)
        plt.show()
    
    return (model)
    


def show_pred_on_synth(model, X, y, X_synth, param_str):
    """ shows behavoiur of univariate ML regression on synthetic dataset
 
    Parameters
    ----------
    model: a parametrized regression model
    X, y: data for univariate regression
    X_synth: synthetic Feature
    param_str: parameter description for title
    seed (None): random seet for split

    Returns
    -------
    a scatterplot von X, y, with the prediction values for X_synth
    
    """
    
    model.fit(X.to_numpy(), y)
    y_pred = model.predict(X_synth)

    ax = sns.scatterplot(x=X['X'], y=y)
    ax = sns.lineplot(x=X_synth[:,0], y=y_pred, color='orange')
    ax.set_title(model.__class__.__name__ + ' : ' + param_str)
    ax.set(xlabel='X', ylabel='y')
    plt.show()


