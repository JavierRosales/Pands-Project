# David Markham
# Data Analytics Project - April 2019
# G.M.I.T. 
# Lecturer: Ian McLoughlin 

# Topic: Iris Data Set


## This project required me to research the well known Fisher's Iris data set, and provide my own analysis of it, and provide scripts of Python code to illustrate tables, graphs, histograms etc. 

# Contents 

1. **Project Plan** 
2. **What's involved when investigating a data set and how Python can be used as a tool.**
3. **What is the Iris Data Set**
4. **Who was Fisher?** 
5. **How was his research beneficial?**
6. **My Research and Investigation**
7. **Findings**
8. **References** 



**1. Project Plan**

I will be first explaining what is involved when setting out to investigate a data set, and how you can back up arguments using scripts of code through Python and graphs which will illustrate and back up your findings.

In my research I will be providing, background information on the data set, a detailed analysis of the data set and my findings, which will be included in this ReadMe. In this I will explain how I investigated and summarized the data set, my findings and other peoples analysis which I considered interesting. 
 
I will be using Python scripts of code to explain my arguments and findings, and attached will be graphs and snippets in the ReadMe.

Finally I will provide a summary and draw my conclusion of the data set.



**2. What's involved when investigating a data set and how Python can be used as a tool.**

To get started you will need to install Anaconda and Python and a command line on your machine. Python is regarded by many as the easiest machine language to learn, but it is also a high level and powerful language. The Iris CSV file data set will also have to be downloaded and from this you will be generating all you findings through tables, graphs etc. When writing your code to present visual findings, you will need to import libraries such as Numpy, Pandas, Matplotlib etc. 

When investigating data four steps to follow can be as follows;

**1. Question**: What are you trying to resolve or achieve?

**2. Analyze**: What tools are you going to use to present your findings?

**3. Investigate**: Research and investigate the problem/sector you are trying to extract data from.

**4. Repeat**: Keep repeating the process until you resolve the problem and present your findings.

Data can be an excellent resource when trying to predict, forecast, improve decision-making or gain a competitive advantage. When investigating a data set you ask yourself what you want to get from it? What is the sole purpose of it, and will pulling data answer the problem you want to solve correctly? You will need to set aside an amount of time to research the topic/sector you are investigating and understand the problem. An excellent way of aiding in your investigations is by displaying results via graphs, scatter plots etc, which can be done by writing code using Python. This will display data and explore weekly, monthly, quarterly or yearly trends based on what you are looking for.

Try and picture what your data set will look like, how you are going to write the code necessary to back up your findings. It's a lot easier to spot relationships between variables if you analyze data from different subsets. What type of statistical tools you will need to get your point across, for example bar charts, line charts, histograms etc. What tools you can use to measure the relationship between two variables or multi-variables? Some examples to achieve this would be correlation testing or scatter plots. And for multi-variables you might use heat maps, regression, ratios etc. 




**3. What is the Fisher Iris data set?**

This Iris data set was introduced by British mathematician and statistician Ronald Fisher which he published in his paper in 1936 *The use of multiple measurements in taxonomic problems*. The data set is often used in data mining, classification and clustering examples and to test algorithms. It is famous because it is used as the "hello world" in data sets and statistics by most people.

The data set contains five columns, the first four are the measurements of the flowers in centimeters and the fifth is the species of the flower. The set comprises of 150 records of flowers representing three species of Iris (Iris setosa, versicolor and virginica) under five attributes - petal length, petal width, sepal length, sepal width and species. It is a data set which is based on the combination of four measurements, petal length and width, sepal length and width. Fisher developed a linear discriminant model to distinguish the species from each other. "Logistic regression is a classification algorithm traditionally limited to only two-class classification problems. If you have more than two classes then Linear Discriminant Analysis is the preferred linear classification technique."




**4. Who was fisher?**



Sir Ronald Fisher was a British Statistician who pioneered the application of statistical procedures to the design of scientific experiments. By many, he was thought to be the greatest statistician of the last century who made profound contributions to both theoretical and applied statistics, and population genetics. He was born in London and studied mathematics at Cambridge University and graduated with a B.A. in astronomy. He continued to work at Cambridge after he graduated where he focused on astronomy and physics,the theory of errors. He taught maths and physics in Cambridge while he focused his research on statistics and genetics until 1919.

In 1919 he did statistical work associated with plant breeding experiments and his methods were published and remained in print for more than 50 years. The experiments that he conducted led to theories about gene dominance and fitness. He analyzed crop data and experiments since the late 1800's and developed the analysis of variance. (https://www.statisticssolutions.com/manova-analysis-anova/) In 1921 He published *Studies in Crop Variation*, which was his first application of analysis of variance.(ANOVA)

In 1933 he became head of Eugenics( beliefs and practices that aim to improve the genetic quality of human population by excluding certain groups judged to be inferior and promoting certain groups judged to be superior) at University College London. While here he published *The Design of Experiments* in 1935, which he outlined *The Lady Tasting Tea* which is now a famous design of a statistical randomized experiment. 

In 1936 he introduced the *Iris Flower Data Set* as an example of discriminant analysis. This was a method used in statistics, pattern recognition and machine learning to find a linear combination that characterizes or separates two or more classes of objects or events. 

He worked in Cambridge from 1940 until 1956 where he published many more books and papers on data sets. In 1957 he retired to Adelaide, and he died in 1962 from an operation he had to remove colon cancer.



**5. How was his research beneficial?**

Fisher introduced many new concepts and approaches to improve research, backed up by mathematical statistics and other theories. Two of his most influential books are *Statistical Methods for Research Workers*, which was to revolutionize statistics and biology (1925), and *The Design of Experiments* (1935). This established the cause and effect relationship, the information retrieved from this managed process inputs to optimise outputs. 

He laid the foundations of statistics as a science, which he proved in much of his research. The Iris data set which he also produced became a typical test case for many statistical classification techniques in machine learning. There is a strong relationship between the measurements and the species and thus various machine learning models can accurately predict the species given the measurements. He established the Fisher-Race notation, still used today, for Rhesus phenotypes and genotypes. Much of Fisher's work remains relevant,and may even serve as a foundation for future research in the statistical analysis of DNA data.


**6. My summary of research and investigation.** 

I started my research on the Irish data set by going through various websites reading and watching material based on the data set. First I downloaded the Iris data csv file which will help me find the relationship or patterns between the three different species which are as follows, the setosa, versicolor and virginica. I will be using various scripts of Python code to calculate the maximum, minimum, mean of the columns and other methods  to demonstrate my findings. I will be also using tables and graphs as necessary. 

To get started you will need to import some libraries which will read and help analyze and plot your data. These will consist of Pandas, Numpy, Matplotlib.pylpot. All three are explained on [Cloudxlab](https://cloudxlab.com/blog/numpy-pandas-introduction)

When **Importing the data from the CSV file** you will need to enter this to ensure that the data is read correctly and not the flower details on the first row on each column. 

import numpy as np,
import pandas as pd,
import matplotlib.pyplot as plt


data = ("iris.csv")

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']

dataset = pd.read_csv(data, header=0)




**Statistical Data** 
When you have this done you can test your data statistically using many different commands such as for example: 



1. print(dataset.shape) - This will output rows and column totals. 

2. print(dataset.head()) - Enter a number within the brackets to display the number of data rows. 

3. print(dataset.describe()) - This outputs the mean, max, min as well as some other data in percentage

4.  print(dataset.groupby('class').size()) - This will display each classification of data along with the number of each.




**Data Visualization** 

Next we can look at the data relating to each variable and also the relationships between each of the variables in the data-set. This can be done through scripts which will output data, in this case a Boxplot and Histogram will illustrate the data.

**1. Boxplot**: A box and whisker plot—also called a box plot—displays the five-number summary of a set of data. The five-number summary is the minimum, first quartile, median, third quartile, and maximum. In a box plot, we draw a box from the first quartile to the third quartile. A vertical line goes through the box at the median. The whiskers go from each quartile to the minimum or maximum.(Wellbeing at School) 

I found information online and code which enabled me to display the data for each variable in the set. I done this in the "irisplot.py" folder. 

- dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()


**2. Histogram**: A histogram shows the frequency on the vertical axis and the horizontal axis is another dimension. Usually it has bins, where every bin has a minimum and maximum value. This can be illustrated using the matplotlib.pyplot function from the Python library.  

- dataset.hist()
plt.show()

For this data to be displayed using a histogram I entered the following 



**7. Findings.**

**8. Bibliography** 

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

<<<<<<< HEAD
CloudXlab, Numpy, Pandas and Matplotlib, viewed on 2019-04-12, https://cloudxlab.com/blog/numpy-pandas-introduction 

Wellbeing at School, Understanding and interpreting box plots, viewed on 2019-04-12, https://www.wellbeingatschool.org.nz/information-sheet/understanding-and-interpreting-box-plots 
=======
Wellbeing at School, Understanding and interpreting box plots, viewed on 2019-04-12, https://www.wellbeingatschool.org.nz/information-sheet/understanding-and-interpreting-box-plots 
>>>>>>> 8353a405de3c9cc34a8013511eaba514ea99a761
