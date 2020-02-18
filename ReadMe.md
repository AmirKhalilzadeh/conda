This repository is provided to answer the 3 tasks given by EES on 07.02.2020.

### Task 1: creating a demo unit to explain the Naive Bayes Classifier
The main content and the example in this unit are original. The two tasks are slightly modified versions of [here](https://www.datasciencecentral.com/m/blogpost?id=6448529%3ABlogPost%3A285052) and [here](https://youtu.be/ZAfarappAO0). Catching up with the content does not assume any prior background in statistics or data science. The exercises are aimed to be solved manually and thus there is no need to run the cells. The use of data is minimal and is limited to the tables provided in the text. This task can be reached by clicking on the following icon.

[![Generic badge](https://img.shields.io/badge/jupyter_nbviewer-Task_1-green)](https://mybinder.org/v2/gh/AmirKhalilzadeh/conda/master?filepath=task_2.ipynb)

### Task 2: creating a Scikit-learn demo unit to explain the F1 Score
The main content, the example and tasks in this unit are original. For task 2 though I benefited from this [Kaggle dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database). To get the best out if this unit one requires basic knowledge of Python and Scikit-learn library as well as running certain cells. This task can be reached by clicking on the following icon.

[![Binder](https://img.shields.io/badge/jupyter_mybinder-Task_2-green)](https://mybinder.org/v2/gh/AmirKhalilzadeh/conda/master?filepath=task_2.ipynb)


### Task 3: short answer to the sample learner question

[![Binder](https://img.shields.io/badge/jupyter_nbviewer-Task_3-green)](https://mybinder.org/v2/gh/AmirKhalilzadeh/conda/master?filepath=task_2.ipynb)

<b>Time spent doing the tasks</b>:
It took me several (3-4) after work evenings to finish the work. Here is the distribution:
  - reviewing the related content (10%)
  - framing stories and examples (20%)
  - framing the exercies (20%)
  - composing the layout and content and finding out how to best communicate them (50%). I hadn't used nbviewer and binder before.

## Note
The `environment.yml` file should list all Python libraries on which your notebooks
depend, specified as though they were created using the following `conda` commands:

```
source activate example-environment
conda env export --no-builds -f environment.yml
```

Note that the only libraries available to you will be the ones specified in
the `environment.yml`, so be sure to include everything that you need! 

Also note that conda will possibly try to include OS-specific packages in `environment.yml`, so you
may have to manually prune `environment.yml` to get rid of these packages. Confirmed Mac-OSX-specific
packages that should be removed are:

* libcxxabi=4.0.1
* appnope=0.1.0
* libgfortran=3.0.1
* libcxx=4.0.1
