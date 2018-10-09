# Task 
Sentiment Analysis using movie reviews.

## Project Structure

- data
	- train.tsv
	- test.tsv 
- notebooks
- scripts (Executable scripts)
- models (Pretrained Models) 

### Run

```python
pip install -r requirements.txt
python3 scripts/bowandtfidf_v1.py
```
You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included

### Pipeline Explained
#### Text Cleaning

First we cleaned the text by removing the html markups, stop words, converting text to lowercase, and finally stemming to convert the text in base form

### Feature Extraction

For Feature Extraction we used Bag of Words and TF-IDF to extract features from text that can be fed to machine learning model. We observe that just by little hyperparameter tuning of the Bag of Words and TF-IDF yields better results.

### Model Building
We fitted a basic linear regression to get a 0.89 f1-score.
