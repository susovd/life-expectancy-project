# Life Expectancy Prediction 

<!---Project Logo -->
<br />
<p align="center">
  <a href=>
    <img src="https://64.media.tumblr.com/e0b750d43e878b3958f5aeef474ea1f5/tumblr_mjgwdnOS1f1s2gg27o1_250.gif" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center"> Life expectancy prediction with Machine Learning </h3>
  
   
  <br />
</p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Feature list](#Feature-list)
* [Overview of steps](#Overview-of-steps)
* [Usage](#usage)
* [Getting Started](#getting-started)
* [Heroku](#heroku)
* [Contributors](#contributors)



<!-- ABOUT THE PROJECT -->
## About The Project
Life expectancy refers to the number of years a person is expected to live based on the statistical average. Life expectancy varies by geographical area and by era. In the Bronze age, for example, life expectancy was 26 years, while in 2010, it was 67 years.

### Why we think this project is important?
According to the ABS, the Australian population is set to double by 2066, which got us to thinking ...  What have been the macro trends for things like life expectancy, birth rates, population size and growth and how do they compare with the rest of the world?  So, like all good data nerds we went looking. 


## Built With
* Python
* certifi==2020.6.20
* click==7.1.2
* Flask==1.1.2
* gunicorn==20.0.4
* itsdangerous==1.1.0
* Jinja2==2.11.2
* joblib==0.17.0
* MarkupSafe==1.1.1
* numpy==1.19.3
* scikit-learn==0.23.2
* scipy==1.5.3
* sklearn==0.0
* threadpoolctl==2.1.0
* Werkzeug==1.0.1
* wincertstore==0.2


## Feature list (Need to update from final version)
* Country- Country
* Year- YearStatus- Developed or Developing status
* Life Expectancy- Age(years)
* Adult Mortality- Adult Mortality Rates of both sexes
* Percent Expenditure- Expenditure on health as a percentage of Gross Domestic Product per capita(%)

## Overview of steps: 

* Step1: Clean raw data. Identify independent variables for dependent variable life expectancy.  
* Step2: Import cleaned raw data to Hive and merge tables based on country names 
* Step3: Use Scikit-learn to do regression to find relationship between life expectancy and all different variables.  
* Step4: Visualize the results using Tableau


<!-- USAGE EXAMPLES -->
## Usage
We have provided an abbreviated dashboard of the Life Epectancy on heroku. The dashboard contains only demographic data from 2000-2020 **

Click on the link to explore and interact with our [Dashboard](*********)


<!-- GETTING STARTED -->
## Getting Started
If you wish to run a local version with the full dataset, skip to [Local](#local). If you wish to run a scaled down version on your own Heroku app, follow the following [Heroku](#heroku) steps.

### Heroku
**To get your own database and app up and running on heroku, follow these steps.**
1. Fork our directory on github.
2. Sign up for an [Heroku](https://www.heroku.com/) account.
3. Connect your github page to a new Heroku app, and click **'Deploy'**.
4. Add your database to your Heroku app. 
5. And now you are all set. Have fun with your new app!


## Future Work

* Look at class within a particular country and see if these same factors are same in determining life expectancy for an individual. 
* Use the Twitter API to incorporate NLP analysis for a country to see how it relates to Life Expectancy. 
* Increase the dataset size with continuing UN and Global Data to incorporate new added features like population, GDP,  environmental, and etc in order to test and clarify country groupings.  
* Mental Health versus Life Expectancy


<!-- CONTRIBUTORS -->
## Contributors

* Alex Lawson
* Ashley Drayton
* Rishit Sheth
* Susov Dhakal
* Vineet Goyal

***




## Thank you for your time to read our project. We hope you enjoyed it.😊😊😊😊
