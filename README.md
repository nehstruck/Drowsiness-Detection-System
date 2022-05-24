# Drowsiness-Detection-System

Installing and Configuring dlib:
We need to create an enivronment in order to install dlib, as it cannot be directly installed using pip. So, follow this commands in order to install dlib into your system if you haven't installed it previously. Make sure you have Anaconda installed, as we will be doing everyting in Anaconda Prompt.

Step 1: Update conda

conda update conda

Step 2: Update anaconda

conda update anaconda 

Step 3: Create a virtual environment

conda create -n env_dlib 

Step 4: Activate the virtual environment

conda activate env_dlib

Step 5: Install dlib

conda install -c conda-forge dlib 

If all these steps are completed successfully, then dlib will be installed in the virtual environment env_dlib. Make sure to use this environment to run the entire project.

Step to deactivate the virtual environment

conda deactivate 

Running the system:

Step 1:

Clone the repository into your system by:

git clone

Step 2:

Install all the system requirments by:

pip install -r requirements.txt

Step 3:

After the system has been setup. Run the command:

python app1.py

Step 4:

Open your browser and in the search bar type: localhost:8000 as this port is mostly used by flask. In case, this port is not available in your system, flask will try to use another port. The port number will be displayed in the command prompt. So, type in the same port number in that case as: localhost:<port_number>.
