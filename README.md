# Life Expectancy Prediction 

<!---Project Logo -->
<p align="center">
  <a href=>
    <img src="/Static/Images/visualisations.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center"> Life expectancy prediction with Machine Learning </h3>
  
   
<br />
</p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Heroku](#heroku)
* [Future Work](#future-work)
* [Contributors](#contributors)



<!-- ABOUT THE PROJECT -->
## About The Project
Life expectancy refers to the number of years a person is expected to live based on the statistical average and depends on numerous socio-economic factors besides death. It is an important metric to assess population health. Life expectancy, education index and gross domestic product combine to provide Human Development Index. 
For the project we downloaded data from workld bank website [here](http://datatopics.worldbank.org/world-development-indicators/).

## Built With
* [Python](https://www.python.org/about/)
  * [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)
  * [Flask](https://flask-doc.readthedocs.io/en/latest/)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS#:~:text=Cascading%20Style%20Sheets%20%28CSS%29%20is%20a%20stylesheet%20language,on%20paper%2C%20in%20speech%2C%20or%20on%20other%20media.)
* [scikit-learn](https://scikit-learn.org/stable/)


<!-- GETTING STARTED -->
## Getting Started
* 00ETL.ipynb notebooks contains codesfor ETL of data. 
* 01EDA.ipynb contains exploratory data analysis. 
* 02_Multiple_regression.ipynb contains codes for multiple linear regression.
* model.py can be called from the root directory to train and save the model. It also houses the flask app that will allow the user to input values for birth rate, fertility  rate and Tuberculosis incidence per 100,000 people. 
* index.html houses a website accompanying the the flask app. 

## Heroku
The web app is hosted [here](https://life-expectancy-prediction.herokuapp.com/) using Heroku.

## Future Work

The project is at an extremely rudimentary and crude stage. Significant changes will be made with time. 

<!-- CONTRIBUTORS -->
## Contributors

* Alex Lawson
* Ashley Drayton
* Rishit Sheth
* Susov Dhakal
* Vineet Goyal

***




## Thank you for your time to read our project. We hope you enjoyed it.😊😊😊😊
