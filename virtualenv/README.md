## DataTube Virtual Environment

_Note that it is not currently necessary to use a virtual environment. Only
setup one if you need it for local development._

It's good practice to use a virtual environment to avoid dependency issues. You
may use whatever virtual environment you want (venv, poetry, etc.). The
requirements.txt file lists out the expected packages. In the interest of
keeping the codebase small, we exclude the actual virtual environment packages
however.

### Setting up Python's venv

More recent versions of Python (3.3 >=) comes with `venv`, a virtual
environment module. This section describes the setup process.

To begin, cd into the virtualenv directory and run `python3 -m venv datatube`.
This will create the datatube environment. Activate the virtual environment if
it is not already enabled with `source datatube/bin/activate`. The packages can
then be installed with `pip -r requirements.txt`.
