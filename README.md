# Python CLI
This is a python CLI Skelton, go through the below checklist to 
update this repo to your specific needs.

## Ready for Coding Checklist
* Update the setup.py as follows:
    - Update the name to your application
    - Update the description to your application
    - Update the entry point from pycli to your cli app name
    (The command in a terminal)
    - Update the author and author_email to your own or
    teams contact information.
* Update Readme as follows:
    - Rename app title
    - Update main description
    - Update Install step 5 to name of application (set in setup.py)
    - Update run instructions for name of application (set in setup.py)
* Remove the *Ready for Coding Checklist* from the readme

## Install
Within the root directory of this application using either git bash or CMD:
1. Create a virtual environment with the command
> py -m venv env
2. Activate the virtual environment with the command for windows
> .\env\Scripts\Activate.bat

or Bash
> source .\env\Scripts\activate
3. Install tox with the command
> pip install tox
4. Build using the command
> tox
5. Install local with the command
> pip install .\.tox\dist\PyCli-*.zip

## Run
After doing an install, using either git bash or CMD, run the command below to get
interface details:
> pycli -h