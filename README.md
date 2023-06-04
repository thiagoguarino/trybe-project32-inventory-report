## Trybe Project 32 - Inventory Report


## PROJECT OVERVIEW

  This is project #2 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/).

  This project genereates reports data from command line. It handles XML, JSON and CSV files as data inputs. The outputs can be divided in two options. Simple Report and Complete Report. This project also has Unit Tests and Bonus Tasks.

  Stack: Python3, Pytest.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>

## PROJECT TASKS

<details>
  <summary>
    <b>Tasks and Status</b>
  </summary>

* tasks 10 and 11 are bonus tasks

*Description* | *Status*
--- | :---:
1 - should create a new product with all attributes correctly filled | :heavy_check_mark:
2.1 - generate method of SimpleReport Class should return all info from Simple Report | :heavy_check_mark:
2.2 - generate method from class SimpleReport should return the correct format from Simple Report | :heavy_check_mark:
3 - generate method from class CompleteReport should return all info from Complete Report | :heavy_check_mark:
4 - when importing a csv file, should return the Simple reports or the Complete as requested | :heavy_check_mark:
5 - when importing a JSON file, should return the Simple reports or the Complete as requested | :heavy_check_mark:
6 - when importing a XML file, should return the Simple reports or the Complete as requested | :heavy_check_mark:
7 - the classes CsvImporter, JsonImporter and CsvImporter should return product's data in a list | :heavy_check_mark:
8 - the default return of a Product object should be a report about it | :heavy_check_mark:
9 - the report should be styled with colors | :heavy_check_mark:
10.1 - checks if instance of InventoryRefactor is Iterable | :heavy_check_mark:
10.2 - checks if it is possible to iterate the first item in the list using csv | :heavy_check_mark:
10.3 - checks if it is possible to iterate o primeiro item da lista usando json | :heavy_check_mark:
10.4 - checks if it is possible to iterate o primeiro item da lista usando xml | :heavy_check_mark:
10.5 - checks if it is possible to receive two data sources without overwritting | :heavy_check_mark:
10.6 - checks if is not possible to send an invalid file | :heavy_check_mark:
11.1 - checks if the menu imports a csv file and generates a Simple Report | :heavy_check_mark:
11.2 - checks if the menu imports a csv file and generates a Complete Report | :heavy_check_mark:
11.3 - checks if the menu imports a json file and generates a Simple Report | :heavy_check_mark:
11.4 - checks if the menu imports a json file and generates a Complete Report | :heavy_check_mark:
11.5 - checks if the menu imports a xml file and generates a Simple Report | :heavy_check_mark:
11.6 - checks if the menu imports a xml file and generates a Complete Report | :heavy_check_mark:
11.7 - checks if when sending missing arguments outputs an error | :heavy_check_mark:

</details>

<details>
  <summary><strong>How to Execute the Tests</strong></summary>

  To execute the tests, first check if you have the virtual environment up and running.

  <strong>To Execute All tests:</strong> ```$ python3 -m pytest```

  the file `pyproject.toml` already correctly configures pytest. However, in case you have issues with that and want a complete explicit output, the command is:

  ```bash
  python3 -m pytest -s -vv
  ```

  In case you need to execute just one test file, use the command:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  In case you need to execute just one test function, use the command:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  If you wish that the tests stop from being executed when the first error happens, use the param `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```

  To execute a specific test of a file, type the command:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```
</details>

## HOW TO RUN THE APP


  1. clone the repository

   - `git clone git@github.com:thiagoguarino/trybe-project32-inventory-report.git`
  
  2. enter the project's folder 

   - `cd trybe-project32-inventory-report`

  3. create and open the project's virtual environment

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  4. install dependencies

  - `python3 -m pip install -r dev-requirements.txt`

  <details>
  <summary><strong>How To Execute the App</strong></summary>

  After implementing the bonus task, the app must be executable from command line.

  The command to be executed is inventory_report. To work correctly you must install the module on your own environment as a pip package: `pip install`

  Now you can call the command inventory_report passing the arguments: `inventory_report argument1 argument2`

  argument1 should receive the file path of the file to be imported. the file can be a csv, json or xml.

  argument2 can receive two strings: simple or complete, each one generating their own report.

  another option is to use the command: `python3 -m inventory_report.main argumento1 argumento2`
  </details>
