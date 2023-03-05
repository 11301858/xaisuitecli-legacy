:warning: Obsolete. Please refer to the new xaisuitecli repository.

This is the script for XAISuiteCLI, XAISuite's command-line interface. Simply download XAISuiteCLI.sh and CLIRunner.py to your working directory and type

```
$alias xs="bash XAISuiteCLI.sh"
```

Command-line options and flags include:

| **Command**  | **Argument**                              | **Function**                                                                |
|--------------|-------------------------------------------|-----------------------------------------------------------------------------|
| train      | minimum 4                                 | trains a model                                                              |
| model      | minimum 1                                 | fetches a model                                                             |
| data       | 1, filename or address of data            | sets the data used in training the model                                    |
| explainers | minimum 1                                 | sets the list of explainers to be used                                      |
| target     | 1, name of target variable                | sets the target variable in the dataset                                     |
| compare    | 0 (flag)                                  | will enable explainer comparison, provided explanations have been generated |
| verbose    | 0 (flag)                                  | will enable debugging dialogue                                              |
| GUI        | 0 (flag)                                  | will open XAISuite GUI                                                      |
| check      | minimum 2                                 | check if argument is a valid, model, dataset, or explainer                  |

An example of correct usage would be

````

$xs train model SVR data energy_efficiency_data.csv target Heating_Load explainers shap lime verbose

````

or

````

$xs check model SDGRegressor

````
