# pythonDiffTool

Behave-Python automation framework tool to compare two JSON files

# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Need the following installed:
```
git clone https://github.com/iso13/pythonDiffTool
pip install behave

```
### Behave Structure

Test file resides in the features directory; ie. diffTool.feature
The step definition resides in the features/steps directory; ie. steps.py

### Running the tests

Within the project directory run the following command:
```
behave
```

### Reporting

If all goes well, the tests will generate 10 html report files that will show the diff between the gold and test json files.