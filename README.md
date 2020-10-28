# Life Expectancy Prediction 

<!---Project Logo -->
<br />
<p align="center">
  <a href=>
    <img src="Static/Images/logo.JPG" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center"> Life expectancy prediction with Machine Learning Project</h3>
  
   
  <br />
</p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Usage](#usage)
* [Getting Started](#getting-started)
* [Heroku](#heroku)
* [Local](#local)
* [Contributors](#contributors)



<!-- ABOUT THE PROJECT -->
## About The Project
Life expectancy refers to the number of years a person is expected to live based on the statistical average. Life expectancy varies by geographical area and by era. In the Bronze age, for example, life expectancy was 26 years, while in 2010, it was 67 years.

## Why we think this project is important?
According to the ABS, the Australian population is set to double by 2066, which got us to thinking ...  What have been the macro trends for things like life expectancy, birth rates, population size and growth and how do they compare with the rest of the world?  So, like all good data nerds we went looking. 


### Built With
* [Python](https://www.python.org/about/)
  * [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)
  * [Flask](https://flask-doc.readthedocs.io/en/latest/)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS#:~:text=Cascading%20Style%20Sheets%20%28CSS%29%20is%20a%20stylesheet%20language,on%20paper%2C%20in%20speech%2C%20or%20on%20other%20media.)
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/javascript)
  * [d3.js](https://d3js.org/)
  * [Leaflet](https://leafletjs.com/)
  * [SweetAlert](https://sweetalert.js.org/guides/)
  * [Image-map](https://www.npmjs.com/package/image-map)
  * [Plotly](https://plotly.com/javascript/)


<!-- USAGE EXAMPLES -->
## Usage
We have provided an abbreviated dashboard of the Life Epectancy on heroku. The dashboard contains only demographic data from 2000-2020 **

Click on the link to explore and interact with our [Dashboard](*********)

![Dashboard](/static/images/dashboard.gif ***** )

<!-- GETTING STARTED -->
## Getting Started
If you wish to run a local version with the full dataset, skip to [Local](#local). If you wish to run a scaled down version on your own Heroku app, follow the following [Heroku](#heroku) steps.

### Heroku
**To get your own database and app up and running on heroku, follow these steps.**
1. Fork our directory on github.
2. Sign up for an [Heroku](https://www.heroku.com/) account.
3. Sign up for [mapbox](https://www.mapbox.com/), and replace your api key with ours on the _/static/js/config.js_ file. Remember to restrict your mapbox api key to your app url, so you don't get hit with nasty charges!!!
4. Connect your github page to a new Heroku app, and click **'Deploy'**.
5. Add your database to your Heroku app. 
6. And now you are all set. Have fun with your new app!

### Local
**To get a local copy up and running follow these steps.**
1. Clone our directory down to your local machine.
```sh
git clone https://github.com/susovd/life-expectancy-project
```
2. Ensure you have the following [Python](https://www.python.org/downloads/) version 3.6 or later installed.
3. Ensure you have the libraries listed in [requirements.txt](requirements.txt) installed. An easy way to do so is to type
  ```sh
  $ pip install -r requirements.txt
```
4. Get a free API Key at _mapbox_ [https://www.mapbox.com/](https://www.mapbox.com/), and replace your api key with ours on the _/static/js/config.js_ file.
5. To set up your database, comment out _line 17_ (that is for the heroku version) and comment in _lines 24-28_ (local version) in **initdb.py**. Then, run    
```sh
$ python initdb.py.

6. Run app.py and you are all set. Open up the flask page
```sh
$ python app.py
```

<!-- CONTRIBUTORS -->
## Contributors

* Alex Lawson
* Ashley Drayton
* Rishi Sheth
* Susov Dhakal
* Vineet Goyal

***




## Thank you for your time to read our project.