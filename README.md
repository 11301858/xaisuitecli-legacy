This is the script for XAISuiteCLI, XAISuite's command-line interface. Simply type

```
$brew install xai
```

Command-line options and flags include:

| **Command**  | **Argument**                              | **Function**                                                                |
|--------------|-------------------------------------------|-----------------------------------------------------------------------------|
| --train      | minimum 4                                 | trains a model                                                              |
| --model      | minimum 1                                 | fetches a model                                                             |
| --import     | 1, filename where trained model is stored | imports model from file                                                     |
| --data       | 1, filename or address of data            | sets the data used in training the model                                    |
| --explainers | minimum 1                                 | sets the list of explainers to be used                                      |
| --target     | 1, name of target variable                | sets the target variable in the dataset                                     |
| --compare    | 0 (flag)                                  | will enable explainer comparison, provided explanations have been generated |
| --verbose    | 0 (flag)                                  | will enable debugging dialogue                                              |
| --GUI        | 0 (flag)                                  | will open XAISuite GUI                                                      |
| --graphics   | 0 (flag)                                  | will generate graphics                                                      |

The correct positioning of the options are as follows:

````

$xai --train --model <Model name> --import <filename if --model has no arguments> --data <Data> 
--target <Target name> --compare --verbose -- GUI --graphics

````
