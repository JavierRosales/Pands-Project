# David Markham
# Data Analytics Project - April 2019
# G.M.I.T. 
# Lecturer: Ian McLoughlin 

# Topic: Iris Data Set

![iris_petal_sepal](https://user-images.githubusercontent.com/47174160/56137829-89e4a000-5f8d-11e9-9b9c-82aa58013d95.png)

## This project required me to research the well known Fisher's Iris data set, and provide my own analysis of it, and provide scripts of Python code to illustrate tables, graphs, histograms etc. 

# Contents 

1. **Project Plan and purpose.** 
2. **What's involved when investigating a data set and how Python can be used as a tool.**
3. **What is the Iris Data Set**
4. **Who was Fisher?** 
5. **How was his research beneficial?**
6. **My Research and Investigation**
7. **Findings**
8. **References** 



# 1. Project Plan

I will be first explaining what is involved when setting out to investigate a data set, and how you can back up arguments using scripts of code through Python and graphs which will illustrate and back up your findings. The purpose of this project was to gain skills in machine learning classification, data visualization and to improve my skills in learning machine languages.

In my research I will be providing, background information on the data set, a detailed analysis of the data set and my findings, which will be included in this ReadMe. In this I will explain how I investigated and summarized the data set, statistical data of each species of flower, and what relationships are there between the three species.
 
I will be using  scripts of Python code to explain my arguments and findings, and attached will be graphs and other visual data I used to provide my findings, along with screenshots of my work in the ReadMe. Finally I will provide a summary and draw my conclusion of the data set.



# 2. What's involved when investigating a data set and how Python can be used as a tool.

To get started you will need to install Anaconda and Python and a command line on your machine. Python is regarded by many as the easiest machine language to learn, but it is also a high level and powerful language. The Iris CSV file data set will also have to be downloaded and from this you will be generating all your findings through tables, graphs etc. When writing your code to present visual findings, you will need to import libraries such as Numpy, Pandas, Matplotlib etc. 

When investigating data four steps to follow can be as follows;

**1. Question**: What are you trying to resolve or achieve?

**2. Analyze**: What tools are you going to use to present your findings?

**3. Investigate**: Research and investigate the problem/sector you are trying to extract data from.

**4. Repeat**: Keep repeating the process until you resolve the problem and present your findings.

Data can be an excellent resource when trying to predict, forecast, improve decision-making or gain a competitive advantage. When investigating a data set you ask yourself what you want to get from it? What is the sole purpose of it, and will pulling data answer the problem you want to solve correctly? You will need to set aside an amount of time to research the topic/sector you are investigating and understand the problem. An excellent way of aiding in your investigations is by displaying results via graphs, scatter plots etc, which can be done by writing code using Python. Machine learning is about making predictions. This will display data and explore weekly, monthly, quarterly or yearly trends based on what you are looking for.

Try and picture what your data set will look like, how you are going to write the code necessary to back up your findings. It's a lot easier to spot relationships between variables if you analyze data from different subsets. What type of statistical tools you will need to get your point across, for example bar charts, line charts, histograms etc. What tools you can use to measure the relationship between two variables or multi-variables? Some examples to achieve this would be correlation testing or scatter plots. And for multi-variables you might use heat maps, regression, ratios etc. 




# 3. What is the Iris data set?

![Setosa](https://user-images.githubusercontent.com/47174160/56285152-76ad0e00-610e-11e9-84d3-9e001a5bb63d.jpg)

This Iris data set was introduced by British mathematician and statistician Ronald Fisher which he published in his paper in 1936 *The use of multiple measurements in taxonomic problems*. The data set is often used in data mining, classification and clustering examples and to test algorithms. It is famous because it is used as the "hello world" in data sets and statistics by most people. It is traditionally used for classification and prediction to see which features(petal or sepal) of the flower belong to a certain type of Iris flower. This is done through petal and sepal length and width.


The data set contains five columns, the first four are the measurements of the flowers in centimeters and the fifth is the species of the flower. The set comprises of 150 records of flowers representing three species of Iris (Iris setosa, versicolor and virginica) under five attributes - petal length, petal width, sepal length, sepal width and species. It is a data set which is based on the combination of four measurements, petal length and width, sepal length and width. Fisher developed a linear discriminant model to distinguish the species from each other. "Logistic regression is a classification algorithm traditionally limited to only two-class classification problems. If you have more than two classes then Linear Discriminant Analysis is the preferred linear classification technique."




# 4. Who was fisher?

![H4060169-Sir_Ronald_Fisher](https://user-images.githubusercontent.com/47174160/56134869-628ad480-5f87-11e9-895d-242792215f2c.jpg)

Sir Ronald Fisher was a British Statistician who pioneered the application of statistical procedures to the design of scientific experiments. By many, he was thought to be the greatest statistician of the last century who made profound contributions to both theoretical and applied statistics, and population genetics. He was born in London and studied mathematics at Cambridge University and graduated with a B.A. in astronomy. He continued to work at Cambridge after he graduated where he focused on astronomy and physics,the theory of errors. He taught maths and physics in Cambridge while he focused his research on statistics and genetics until 1919.

In 1919 he did statistical work associated with plant breeding experiments and his methods were published and remained in print for more than 50 years. The experiments that he conducted led to theories about gene dominance and fitness. He analyzed crop data and experiments since the late 1800's and developed the analysis of variance. In 1921 He published *Studies in Crop Variation*, which was his first application of analysis of variance.(Encyclopedia Britannica, 2019)

In 1933 he became head of Eugenics( beliefs and practices that aim to improve the genetic quality of human population by excluding certain groups judged to be inferior and promoting certain groups judged to be superior) at University College London. While here he published *The Design of Experiments* in 1935, which he outlined *The Lady Tasting Tea* which is now a famous design of a statistical randomized experiment. 

In 1936 he introduced the *Iris Flower Data Set* as an example of discriminant analysis. This was a method used in statistics, pattern recognition and machine learning to find a linear combination that characterizes or separates two or more classes of objects or events. 

He worked in Cambridge from 1940 until 1956 where he published many more books and papers on data sets. In 1957 he retired to Adelaide, and he died in 1962 from an operation he had to remove colon cancer.



# 5. How was his research beneficial?

Fisher introduced many new concepts and approaches to improve research, backed up by mathematical statistics and other theories. Two of his most influential books are *Statistical Methods for Research Workers*, which was to revolutionize statistics and biology (1925), and *The Design of Experiments* (1935). This established the cause and effect relationship, the information retrieved from this managed process inputs to optimise outputs. 

He laid the foundations of statistics as a science, which he proved in much of his research. The Iris data set which he also produced became a typical test case for many statistical classification techniques in machine learning. There is a strong relationship between the measurements and the species and thus various machine learning models can accurately predict the species given the measurements. He established the Fisher-Race notation, still used today, for Rhesus phenotypes and genotypes. Much of Fisher's work remains relevant,and may even serve as a foundation for future research in the statistical analysis of DNA data. (Encyclopedia of Mathematics, 2016)


# 6. Summary of my research and investigation of the Iris Data-Set.

I started my research on the Irish data set by going through various websites reading and watching material based on the data set. First I downloaded the Iris data csv file which will help me find the relationship or patterns between the three different species which are as follows, the setosa, versicolor and virginica. I will be using various scripts of Python code to calculate the maximum, minimum, mean of the columns and other methods  to demonstrate my findings. I will be also using tables and graphs as necessary. 

To get started you will need to import some libraries which will read and help analyze and plot your data. These will consist of Pandas, Numpy, Matplotlib.pylpot and Seaborn. 

- 1. Numpy: Designed for mathematical and scientific computation.

- 2. Pandas: Manipulates and analyzes data, for eg CSV files or SQL databases.

- 3. Matplotlib: A Python plotting library which plots and displays data on graphs, histograms, bar-charts, scatterplots etc.

- 4. Seaborn: A Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. (Seaborn) 


When **Importing the data from the CSV file** you will need to enter this to ensure that the data is read correctly and not the flower details on the first row on each column. Before you enter this you will first need to import the libraries required to output the data.

- Import numpy as np

- Import pandas as pd

- Import matplotlib.pyplot as plt.

- Import Seaborn as sns

- From pandas.plotting import scatter_matrix


`data = ("iris.csv")`

`names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']`

`dataset = pd.read_csv(data, header=0)`




**Statistical Data** 
When you have this done you can test your data statistically using many different commands such as for example: `print(dataset.describe())`

![Stats](https://user-images.githubusercontent.com/47174160/56137892-a1238d80-5f8d-11e9-9602-a40215592a7b.PNG)

Other lines of code to output statistical data are as follows:

1. `print(dataset.shape)` - This will output rows and column totals. 

2. `print(dataset.head())` - Enter a number within the brackets to display the number of data rows you wish to output. 

3. `print(dataset.describe())` - This outputs the mean, max, min as well as some other data in percentage

4.  `print(dataset.groupby('class').size())` - This will display each classification of data along with the number of each species in this case.




**Data Visualization** 

Next we can look at the data relating to each variable and also the relationships between each of the variables in the data-set. This can be done through histograms, plots etc. By exploring the data visually you can see the relationships between each species by the grouping or clustering on scatterplots and other graphs you may use.

**1. Boxplot**: A box and whisker plot—also called a box plot—displays the five-number summary of a set of data. The five-number summary is the minimum, first quartile, median, third quartile, and maximum. In a box plot, we draw a box from the first quartile to the third quartile. A vertical line goes through the box at the median. The whiskers go from each quartile to the minimum or maximum.(Wellbeing at School) 

I found information online and code which enabled me to display the data for each variable in the set. I done this in the "irisplot.py" folder. 

- `dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)`

`plt.show()`

![Plot](https://user-images.githubusercontent.com/47174160/56138624-2b202600-5f8f-11e9-8787-67614c3cacf6.PNG)


**2. Histogram**: A histogram shows the frequency on the vertical axis and the horizontal axis is another dimension. Usually it has bins, where every bin has a minimum and maximum value. This can be illustrated using the matplotlib.pyplot function from the Python library.  

For this data to be displayed using a histogram I entered the following code on Python.

- `data = ("iris.csv")`
   `names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']`
   `dataset = pd.read_csv(data, header = 0)`

`dataset.hist()`
  
`plt.show()`

![Histogram](https://user-images.githubusercontent.com/47174160/56138674-3ecb8c80-5f8f-11e9-981f-89c3dcb65f8d.PNG)


## Relationship between variables. 

This can be achieved by multivariate plots which can reveal the relationship among several variables simultaneously which generally include the form, strength and dependence of each relationship. There are numerous plots available to display your findings such as, 2D, 3D, colour, scatter plots etc. The closer the dots come together on scatter plots, the stronger the relationship. 

Given a set of variables, the scatter plot matrix contains all the pair-wise scatter plots of the variables on a single page in a matrix format. There is a positive correlation within the data below which I extracted from using Python. 


![Scattermatrix](https://user-images.githubusercontent.com/47174160/56145049-75a79f80-5f9b-11e9-8314-2a1efcfe44e0.PNG)


From the above scatterplot we can see that the petal and sepal measurements are quite different from the other two species.

# Coloured Scatterplot

This will help us determine what data variables (species) have more in common with each other as we found out above.(Benalexkeen.com)

## Here we can see Petal length versus Sepal length. 

 ![ColScatterplot](https://user-images.githubusercontent.com/47174160/56202574-48123300-603b-11e9-9da6-911896be3a74.PNG)

## And the relationship between Petal Width and Sepal Width.

![Scatterplot width col](https://user-images.githubusercontent.com/47174160/56204108-8f4df300-603e-11e9-8cdd-784f0e66fab1.PNG) 

We can clearly see the strong relationship between the Iris Virginica and Versicolor through the size of their petal width. With the Setosa, this species is a lot easier to identify because of the size difference it has in the sepal width over the other two species. From the above visual data I have provided, it is clear that the Setosa is a different species of Iris plant. 


# Algorithms and Predicted Scores.

## Using Various Algorithm Models we wil predict accuracy scores using our validation data which we split in two groups.

We now know that the data above is a *classification problem* as opposed to a *regression problem*. Classification is the task of predicting a discrete class label. Regression is the task of predicting a continuous quantity. These two types categories are known as *Supervised Machine Learning*. The main difference between them is that the output variable in regression is numerical (or continuous) while that for classification is categorical (or discrete). (Math Works, 2019)

## Here we see different groupings of machine learning.

![Machinelearning classification](https://user-images.githubusercontent.com/47174160/56304368-e387ce80-6135-11e9-8dd0-109e29891ac1.png) (Math Works, 2019)




When applying an algorithm you split the dataset into training and testing. The testing dataset is generally a lot smaller as it will help in training the model more effectively. 

- Now we will split the dataset in two, 80% of which we will use to train our models and 20% which we will hold back as a validation dataset. 

- Next we will use different algorithms will will help us to choose the best model done through an 'accuracy' metric which determines the most accurate percentage.

### Split-out validation dataset

Here we split the data-set into two groups, one group we hold back on to test the algorithms out from just a certain percentage of the data, known as the validation data-set.

`array = dataset.values`

`X = array[:,0:4]`

`Y = array[:,4]`

`validation_size = 0.20`

`seed = 7`


`X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)` (Machine Learning Mastery, 2016)

### Next we can do the following: 

We test the data we just split into two groups using various different algorithm models for accuracy. We can do this by importing *Sklearn*, a very good library for machine learning in Python. It is on NumPy, SciPy and matplotlib, this library contains a lot of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction. (Analytics Vidha, 2015) 

### We can do this through six different supervised machine learning algorithms which can solve both classification and regression problems. 

1. Logistic Regression (LR)

2. Linear Discriminant Analysis (LDA)

3. K-Nearest Neighbors (KNN).

4. Classification and Regression Trees (CART).

5. Gaussian Naive Bayes (NB).

6. Support Vector Machines (SVM).

- This will check the scoring accuracy of each algorithm.

`seed = 7`

`scoring = 'accuracy'` 


### Spot Check Algorithms

Here we enter code for the different algorithms we will test.

`models = []`

`models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))`

`models.append(('LDA', LinearDiscriminantAnalysis()))`

`models.append(('KNN', KNeighborsClassifier()))`

`models.append(('CART', DecisionTreeClassifier()))`

`models.append(('SVM', SVC(gamma='auto')))`

### Evaluate each model in turn

- The code blow will evaluate all the models we have entered above and output the scores for each model.

`results = []`

`names = []`

`for name, model in models:`

`kfold = model_selection.KFold(n_splits=10, random_state=seed)`

`cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)`

`results.append(cv_results)`

`names.append(name)`

`msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())`
`print(msg)` (Machine learning mastery, 2016) 



### Which gives us a score of: 


![Algorithmscore](https://user-images.githubusercontent.com/47174160/56298108-7e2de080-6129-11e9-9e7a-6171137867e7.PNG)


- SVM: Results show Support Vector Machines has the highest scoring accuracy of 0.991667 (0.025000)

- So we now go ahead and test Support Vector Machines to see how accurate it is as it has the highest scoring algorithm. We can do that by entering the following code:

`svm =SVC(gamma='auto') `

`svm.fit(X_train, Y_train)`

`predictions = svm.predict(X_validation)`

`print(accuracy_score(Y_validation, predictions))`

`print(confusion_matrix(Y_validation, predictions))`

`print(classification_report(Y_validation, predictions))`

- This will output the following results: 

![Algorithm predictor](https://user-images.githubusercontent.com/47174160/56357160-c523e080-61d2-11e9-9ae2-a3a5fdd02b0f.PNG) 

- From the above data we can see that we have an accuracy score of 93 percent. ` print(accuracy_score(Y_validation, predictions))` 

- Under this are the three errors made which the `print(confusion_matrix(Y_validation, predictions))` displayed. 

- And finally we got the classification report on the validation data by inputting `print(classification_report(Y_validation, predictions))`. This breaks down each class as follows: 

- Precision: The ratio of correctly predicted positive observations to the total predicted positive observations

- Recall: Recall is the ratio of correctly predicted positive observations to the all observations in actual class

- F1-Score: This gives you the harmonic average of precision and recall. Reaches its best value at One and worst at Zero.

- Support: The number of occurrences in each class. (Scikit-learn, 2018)




# 7. Findings.

- From all the above data that we extracted from the csv Iris data-set and illustrated it is quite obvious that the Setosa is a different breed of Iris. One flower species, the Setosa is linearly separable from the other two, but the other two are not linearly separable from each other. The Virginica and Versicolor are quite larger in Pepal length and width. The Setosa sepal width was larger in a quite a few cases but overall the Virginica and Versicolor was much the larger species out of the three classes which were analyzed. This was displayed in the statistical data and in the different plots we used to display the data. 

- In summary we can predict from the data we have examined that if the Iris flower has a long sepal of 6-8cm, long petals of 5-7cm and wide petals of 1.5-2.5cm then the Iris is most likely an IrisVirginica. If the Iris flower has a short sepal of 4.5-5.5cm, short petals of 1-2cm and very narrow petals of .1-.5cm then the Iris is most likely an Iris-Setosa. Any Iris flower that which measures in between these two classifications is most likely an Iris-Versicolor. 

![Scatterplot width col](https://user-images.githubusercontent.com/47174160/56368890-3de56580-61f0-11e9-9c0e-4723b0d24628.PNG)

![ColScatterplot](https://user-images.githubusercontent.com/47174160/56368952-56ee1680-61f0-11e9-9087-803933b96b4f.PNG)


- We then learned how to test the data, train and predict different algorithm models based on score accuracy. We done this by using the classification data through supervised machine learning. We held back some data so we could train using one set and and test using another. We found that (SVM) Support vector Machines had the highest accuracy test. We then went on to test this model with the validation set, from which it got a high score of 93%.

- Tested all the algorithm models 

![Algorithmscore](https://user-images.githubusercontent.com/47174160/56298108-7e2de080-6129-11e9-9e7a-6171137867e7.PNG)

- Tested the model with the highest score. 

![Algorithm predictor](https://user-images.githubusercontent.com/47174160/56357160-c523e080-61d2-11e9-9ae2-a3a5fdd02b0f.PNG)  

# 8. Bibliography 

Encyclopedia Britannica, Sir Ronald Aylmer Fisher, 2019, viewed on 2019-04-03,  https://www.britannica.com/biography/Ronald-Aylmer-Fisher 

Statistics Solutions, Analysis of Variance, 2013, viewed on 2019-04-04, https://www.statisticssolutions.com/manova-analysis-anova/ 

The Python Tutorial, viewed on 2019-0404, https://docs.python.org/3/tutorial/index.html

Warwick University, Plotting the Iris Data, 2008, viewed on 2019-04-04, https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/r/iris_plots/ 

Quora,Investigating a Data Set, 2018, viewed on 2019-04-07, https://www.quora.com/As-a-data-scientist-how-do-you-start-investigating-a-data-set-assuming-that-you-just-pulled-the-data-from-source-and-prepared-it-in-a-nice-possibly-tabular-form 

Encyclopedia of Mathematics, Ronald Aylmer FISHER, 2016, viewed on 2019-04-08, https://www.encyclopediaofmath.org/index.php/Fisher,_Ronald_Aylmer

Kaggle, Machine learning first steps with the Iris dataset, 2015, viewed on 2019-04-08, http://blog.kaggle.com/2015/04/22/scikit-learn-video-3-machine-learning-first-steps-with-the-iris-dataset/

Machine Learning Mastery, Linear Discriminant Analysis for Machine Learning, 2016, viewed 2019-04-09,https://machinelearningmastery.com/linear-discriminant-analysis-for-machine-learning/

Real Python, Reading and Writing CSV Files, 2018, viewed on 2019-04-12, https://realpython.com/python-csv/ 

Data Camp, Python Exploratory Data Analysis Tutorial, 2017, viewed on 2019-04-12, https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python 

CloudXlab, Numpy, Pandas and Matplotlib, viewed on 2019-04-12, https://cloudxlab.com/blog/numpy-pandas-introduction 

Wellbeing at School, Understanding and interpreting box plots, viewed on 2019-04-12, https://www.wellbeingatschool.org.nz/information-sheet/understanding-and-interpreting-box-plots 

Seaborn, viewed on 2019-04-16, http://seaborn.pydata.org

Benalexkeen.com, Scatterplots in Matploblib, viewed on 2019-04-16, http://benalexkeen.com/scatter-charts-in-matplotlib/

Youtube, Pandas, Seaborn and Scikit-Learn, viewed on 2019-04-17, https://www.youtube.com/watch?v=3ZWuPVWq7p4

A Medium Corporation, Regression Versus Classification Machine Learning, viewed on 2019-04-17, https://medium.com/quick-code/regression-versus-classification-machine-learning-whats-the-difference-345c56dd15f7

Machine Learning Mastery, 2016, viewed on 2019-04-17, https://machinelearningmastery.com/machine-learning-in-python-step-by-step

Math Works, What is machine learning, 2019, viewed on 2019-04-17, https://uk.mathworks.com/help/stats/machine-learning-in-matlab.html

Alnalytics Vidhya, Scikit-Learn, 2015, viewed on 2019-04-17, https://www.analyticsvidhya.com/blog/2015/01/scikit-learn-python-machine-learning-tool/

Machine Learning Mastery, How to Make Predictions with Scikit-Learn, 2018, viewed on 2019-04-18, https://machinelearningmastery.com/make-predictions-scikit-learn/ 

Sci-kit Learn, 2018, viewed on 2019-04-18, https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html