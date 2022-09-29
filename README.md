# RoutingProject2022
AAU 2022 1st Semester Project

## Developer Initial Python Setup

1. Download the latest version of [Python (At least 3.10 or greater)](https://www.python.org/downloads/).
2. Open up a terminal in your `RoutingProject2022` folder, and enter the following
```
    python -m venv .venv
```
This creates a virtual Python environment in the project folder, which is specific to you and your machine. 

In VSCode, if you open a Python file (.py), you should see your python version followed by ('.venv':venv), showing that that VSCode is using the Python instance in your newly created virtual environment, and not the one on your base machine. 

![What you should see](\.readmepics\pythonvenv.png)

If VSCode doesn't automatically switch to the virtual environment, you may have to change it manually by clicking the circled area in the above image, and selecting the correct environment

![Selecting the correct environment](.readmepics\goodvenv.png)


3. Now when you open a terminal in VSCode, you should notice a "(.venv)" on the line you're working on. If using a terminal outside of VSCode, you'll have to activate it manually. Do this by using a terminal to navigate to:
```
\RoutingProject2022\.venv\Scripts
```
And then on Windows typing 

`activate`

or on Linux by typing 

`source activate`

4. Final step, update the libraries of your venv. It's a good idea to do this any time you pull new changes from the main branch. To do this, insure that your terminal is in _(.venv) mode_, and then type 
```
pip install -r requirements.txt
```

