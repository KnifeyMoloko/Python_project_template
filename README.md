#Python_project_template

## Elevator pitch intro

This is a general purpose template for Python projects. It includes some bare-bones features that are usefull accross 
most Python projects.

## Requirements and dependencies
- Python 3.6 (tested)  

## Directory and file structure

This is the vanilla directory structure for the template:
```bash
.
├── app
│   └── __init__.py
├── config
│   ├── dev.ini
│   ├──__init__.py
│   ├── prod.ini
│   └── test.ini
├── logs
├── main.py
├── README.md
├── run_tests.py
├── tests
│   ├── __init__.py
│   └── tests_basic.py
```
Quick directory legend:
- **root**: main directory for the project as a whole
- **app**: main application directory. Put your code and app-specific directorires here. 
Please note the **\__init\__.py** file, which containts an app factory function, i.e. it should import and call your 
application code. This application factory function is called by **main.py**
- **config**: contains .ini files for different app configurations. By default production, development and testing 
config files are present.
- **logs**: default logfile directory
- **tests**: test definitions for _unittest_ are containted here. By default only a handful of very basic test cases 
are included

## App architecture

## Running the template scripts

To run the scripts provided in the template, cd into the template directory and:
- set the desired application environment type (prod, dev, test) on the command line:
       
        export APP_ENV=test
       

- For the main script running the app:
    
        python3 main.py
   
- For the predefined basic test set:
        
        python3 run_tests.py

## Installation

Since this template is so basic, you won't have much to do to get it running.

### 1. Download

Clone or download the zipped files to your directory of choice.

### 2. Checking the installation

The template should be ready to go as soon as you clone/download it, but I'd recommend running the template scripts
referenced in the *Running the template scripts* section above. The output for **run_tests.py** should be as follows:
    
    2019-05-23 00:28:35,034 : main : main : 38 : INFO : Running app: Anonymous App
    test_app_is_not_none (tests_basic.BasicTestCase) ... ok
    test_logger_is_present (tests_basic.BasicTestCase) ... ok
    test_main_is_running (tests_basic.BasicTestCase) ... ok
    
    ----------------------------------------------------------------------
    Ran 3 tests in 0.005s
    
    OK
    
Running **main.py** should give you:

    2019-05-23 00:30:22,155 : __main__ : main : 38 : INFO : Running app: Anonymous App
        

## Use cases

## Further development

## FAQ

## References

### Logging module readme

### Unittest testing package

### ConfigParser

## Pathlib?

    
