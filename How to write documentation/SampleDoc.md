# Project Name
Short Project Description

### Install

This project requires **Python3** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included

## Project Structure
- data
	- raw
		- train (Training audio files)
		- test (Test audio files used for evaluation
- libs
	- classification (All scripts used for training and evaluation)
-  notebooks
- scripts (Executable scripts)
- models (Pretrained Models) 

### Run

In a terminal or command window, navigate to the top-level project directory `` (that contains this README) and run one of the following commands:

```bash
jupyter notebook __.ipynb
```
or
```bash
ipython notebook __.ipynb
```

This will open the Jupyter Notebook software and project file in your web browser.

## Architecture
### Models used
1. A variant of Convolutional LSTM (https://arxiv.org/pdf/1610.00277.pdf)

### Training

The model was trained using a GCP instance with the following specifications:
- 
-  
- 

### Data

The dataset used in this project is included as `titanic_data.csv`. This dataset is provided by Udacity and contains the following attributes:

**Features**
- `` :  
- `` : 
- `` : 
- `` : 
- `` : 
- `` : 
- `` : 
- `` : 
- `` : 
- `` : 

**Target Variable**
- `` : (0 = No; 1 = Yes)

# Note
If there is any issue running the code, please post it in the issue tracker.
