# IPL_Analysis
This repository stores the jupyter notebook used for my data science project where I performed Exploratory Data Analysis on [IPL Cricket Data](https://www.kaggle.com/datasets/anandkumarsahu09/ipl-player-stats-20162022).

The notebook can be viewed [here](https://www.kaggle.com/code/vraghubir/ipl-batting-and-bowling-analysis-2016-2022). I also wrote articles explaining my analysis and the insights gained from this [here](https://vraghubir.medium.com/data-science-series-1-cricket-data-analysis-f0923f39462d).

# Adding a season of IPL data

Go to https://www.iplt20.com/stats/{year} select Orange Cap for batting and Purple Cap for bowling and order by Season. When on the page scroll down and click View All and then copy all of the table data and paste it in a file called batting_{year}.csv located in a subfolder named {year} within Data folder. Then open the convert_format function and pass in the 2 files for batting and bowling for the season and this will output the formatted version in the same folder. Copy the final_batting/bowling_{year}.csv file into the current subfolder and open it alongside the formatted csv files. Copy all entries in the formatted csv files and paste them between the header row and the first row that is located in there. Save them and you now have the updated records for all seasons. Copy the IPL_EDA_{year}.ipynb notebook and change all years to be the current year.
