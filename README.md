# zeppelin-automation

use this project to create a 1) pipeline of your zeppelin notebook 2) extract pyspark,spark (any) code from your notebook to their corresponding .py or .scala file

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

python2.7 and above (this project is carried out on 3.6 version)

### Installing

```
pip install requests (if not installed)
pip install configparser (if not installed)
```

## Steps to run the project

1) clone the project to your local machine.

2) Modify the ```zeppelin-server.properties``` which have below given fields

```
[SERVER]
hostname=localhost    (Your zeppelin server)

port=8081             (zeppplin port)

[DEFAULT]
code.language=scala   (if you have written spark code in scala in your zeppelin notebook named abc, this is required to give the extension of extracted code file like abc.scala)

notebook.path=/Users/quantumblack/notebook_list      (this is the path where you will put the text file containing notebook name which you want to run)
```

#### Imp Info about the project
The whole project is divided into two mode

Extraction : In this mode the zeppelin notebook code gets extracted in their repective code files.

Notebook productionizing : In this mode user can productionize your zeppelin notebook.


3) Call the run.py as below
``` 
python run.py "extract"          [EXTRACTION MODE]
python run.py "notebook"         [NOTEBOOK PRODUCTIONIZE]
```

## Notebook Productionize mode

In this mode the user have to provide a text file containing all of his notebook he want to run, and update the path of this file in ```zeppelin-server.properties``` at ```notebook.path```

Once done with basic configuration when he call the run.py file as ```python run.py "notebook"```. It will start running the notebook sequentially as given in user given text file.

## Extraction mode

As mentioned above the user has to provide the similar text file containing notebook name to run. 
When done with basic setup, call the run.py file as ```python run.py "extract"```
This mode will extract the code present in each paragraph of zeppelin notebook and create a code folder inside your project directory. 
The code folder will contain all of your zeppelin notebook code.

### Note 
1) The user has to provide the ```code.language``` as scala or py(python) in terms of getting the .scala or .py file in code folder.
2) To run the .py file or .scala file the user has to take care of language consistencey in their zeppelin notebook. 
3) For spark projects written in scala, it will simply give you a .scala file of each notebook. User have to take care of further class and object declaring syntax.



#### TODO LIST
```
Exception handling
Logging
Running Notebook like DAG (this is almost implemented)
```
