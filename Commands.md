Create an environment - this is for installing all the packages related to that project in that environment only
- conda create -p venv python==version

Activate environment
- conda activate venv/

Deactivate a virtual env
- deactivate

Creating and activating env using python commands
- python -m create myenv (it gets a default python version that is there in the system)
- myenv/Scripts/activate
- deactivate

Creating virtual env using virtual 
- First we will have to install virtualenv
    - pip install virtiualenv
    - virtualenv -p python3 virtual_env
    - virtual_env/Scripts/activate (this will activate it)
    - deactivate
