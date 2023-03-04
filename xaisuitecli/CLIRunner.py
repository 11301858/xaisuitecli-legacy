#!/usr/bin/env python

from xaisuite import*
import sys
import os.path

keywords = ["train", "check", "model", "data", "compare", "verbose", "GUI", "explainers", "target"]

assert len(sys.argv) >= 4 or sys.argv[1] == "GUI", "Not enough arguments"


if ((sys.argv[1]) == "check"):
    assert len(sys.argv) == 4, "At most 2 arguments after check command - 1 option, 1 name "
    assert (sys.argv[2] == "model" or sys.argv[2] == "data" or sys.argv[2] == "explainers"), "Unrecognized option after command check: " + str(sys.argv[2])
    
    if (sys.argv[2] == "model"):
        acceptedModels = {"SVC": "sklearn.svm", "NuSVC": "sklearn.svm", "LinearSVC": "sklearn.svm", "SVR": "sklearn.svm", "NuSVR": "sklearn.svm", "LinearSVR": "sklearn.svm", 
                 "AdaBoostClassifier": "sklearn.ensemble", "AdaBoostRegressor": "sklearn.ensemble", "BaggingClassifier": "sklearn.ensemble", "BaggingRegressor": "sklearn.ensemble",
                 "ExtraTreesClassifier": "sklearn.ensemble", "ExtraTreesRegressor": "sklearn.ensemble", 
                 "GradientBoostingClassifier": "sklearn.ensemble", "GradientBoostingRegressor": "sklearn.ensemble",
                 "RandomForestClassifier": "sklearn.ensemble", "RandomForestRegressor": "sklearn.ensemble",
                 "StackingClassifier": "sklearn.ensemble", "StackingRegressor": "sklearn.ensemble",
                 "VotingClassifier": "sklearn.ensemble", "VotingRegressor": "sklearn.ensemble",
                 "HistGradientBoostingClassifier": "sklearn.ensemble", "HistGradientBoostingRegressor": "sklearn.ensemble",
                 "GaussianProcessClassifier": "sklearn.gaussian_process", "GaussianProcessRegressor": "sklearn.gaussian_process", 
                 "IsotonicRegression": "sklearn.isotonic", "KernelRidge": "sklearn.kernel_ridge", 
                 "LogisticRegression": "sklearn.linear_model", "LogisticRegressionCV": "sklearn.linear_model",
                 "PassiveAgressiveClassifier": "sklearn.linear_model", "Perceptron": "sklearn.linear_model", 
                  "RidgeClassifier": "sklearn.linear_model", "RidgeClassifierCV": "sklearn.linear_model",
                  "SGDClassifier": "sklearn.linear_model", "SGDOneClassSVM": "sklearn.linear_model", 
                  "LinearRegression": "sklearn.linear_model", "Ridge": "sklearn.linear_model", 
                  "RidgeCV": "sklearn.linear_model", "SGDRegressor": "sklearn.linear_model",
                  "ElasticNet": "sklearn.linear_model", "ElasticNetCV": "sklearn.linear_model",
                  "Lars": "sklearn.linear_model", "LarsCV": "sklearn.linear_model", 
                  "Lasso": "sklearn.linear_model", "LassoCV": "sklearn.linear_model",
                  "LassoLars": "sklearn.linear_model", "LassoLarsCV": "sklearn.linear_model",
                  "LassoLarsIC": "sklearn.linear_model", "OrthogonalMatchingPursuit": "sklearn.linear_model",
                  "OrthogonalMatchingPursuitCV": "sklearn.linear_model", "ARDRegression": "sklearn.linear_model",
                  "BayesianRidge": "sklearn.linear_model", "MultiTaskElasticNet": "sklearn.linear_model", 
                  "MultiTaskElasticNetCV": "sklearn.linear_model", "MultiTaskLasso": "sklearn.linear_model",
                  "MultiTaskLassoCV": "sklearn.linear_model", "HuberRegressor": "sklearn.linear_model",
                  "QuantileRegressor": "sklearn.linear_model", "RANSACRegressor": "sklearn.linear_model",
                  "TheilSenRegressor": "sklearn.linear_model", "PoissonRegressor": "sklearn.linear_model",
                  "TweedieRegressor": "sklearn.linear_model", "GammaRegressor": "sklearn.linear_model", 
                  "PassiveAggressiveRegressor": "sklearn.linear_model", "BayesianGaussianMixture": "sklearn.mixture",
                  "GaussianMixture": "sklearn.mixture", 
                  "OneVsOneClassifier": "sklearn.multiclass", "OneVsRestClassifier": "sklearn.multiclass", 
                  "OutputCodeClassifier": "sklearn.multiclass", "ClassifierChain": "sklearn.multioutput", 
                   "RegressorChain": "sklearn.multioutput",  "MultiOutputRegressor": "sklearn.multioutput",
                   "MultiOutputClassifier": "sklearn.multioutput", "BernoulliNB": "sklearn.naive_bayes", 
                  "CategoricalNB": "sklearn.naive_bayes", "ComplementNB": "sklearn.naive_bayes", 
                  "GaussianNB": "sklearn.naive_bayes", "MultinomialNB": "sklearn.naive_bayes", 
                  "KNeighborsClassifier": "sklearn.neighbors", "KNeighborsRegressor": "sklearn.neighbors", 
                  "BernoulliRBM": "sklearn.neural_network", "MLPClassifier": "sklearn.neural_network", "MLPRegressor": "sklearn.neural_network",  
                  "DecisionTreeClassifier": "sklearn.tree", "DecisionTreeRegressor": "sklearn.tree",
                  "ExtraTreeClassifier": "sklearn.tree", "ExtraTreeRegressor": "sklearn.tree"
                 }
        if (sys.argv[3] in acceptedModels.keys()):
            print("Model is valid.")
            sys.exit(0)
        else:
            print("Model is not valid.")
            print("List of accepted models: " + str(list(acceptedModels.keys())))
            sys.exit(1)

    elif ((sys.argv[2]) == "data"):
        if ((os.path.isfile(sys.argv[3])) and (str(sys.argv[3])[-4:] == ".csv")) :
            print("File is valid.")
            sys.exit(0)
        else:
            print("File is not valid. If you are trying to use a sklearn dataset, please download it first before using.")
            sys.exit(1)
    else:
        if (sys.argv[3] in ["lime", "shap", "mace", "ale", "pdp", "sensitivity"]):
            print("Explainer is supported")
            sys.exit(0)
        else:
            print("Explainer is not supported")
            sys.exit(1)
           
                    
elif (sys.argv[1] == "train"):
    assert "model" in sys.argv, "Must specify model if using train command"
    assert "data" in sys.argv, "Must specify data if using train command"
    assert "target" in sys.argv, "Must specify target variable if using train command"
    
    model = sys.argv[sys.argv.index("model") + 1]
    data = sys.argv[sys.argv.index("data") + 1]
    target = sys.argv[sys.argv.index("target") + 1]
    explainers = []

    if "explainers" in sys.argv:
        for i in range (sys.argv.index("explainers") + 1, len(sys.argv)):
            if (sys.argv[i] in keywords):
                break
            explainers.append(sys.argv[i])
    debug = "verbose" in sys.argv
    train_and_explainModel(str(model), load_data_CSV(str(data), str(target)), explainers, verbose = debug)
    if ("compare" in sys.argv):
        fileList = []
        for i in range (len(explainers)):
            fileList.append(str(explainers[i]) + "ImportanceScores - " + str(model) + " " + str(target) + ".csv")
        compare_explanations(fileList)

elif (sys.argv[1] == "compare"):
    assert len(sys.argv) > 1, "Paths to data files must be provided after compare command."
    fileList = []
    for i in range (2, len(sys.argv)):
        fileList.append(str(sys.argv[i]))
    compare_explanations(fileList)
elif (sys.argv[1] == "GUI"):
    import xaisuitegui.runner
else:
    print("Not a valid command " + str(sys.argv[1]))
    sys.exit(1)
