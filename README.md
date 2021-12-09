# Temporal and Spatial Distribution and Impact of Influenza

> **Group members:** 
> - Yizhou Zhao, 
> - Yibo Yan, 
> - Yuxin Jiang, 
> - Ziyue Wan.

## Introduction


## Organization Overview

We placed our codes and results in three separate folders.

- `code` folder
  
  All scripts and codes go here.

- `data` folder

  All data go here, including stored database and cache.

- `notebooks` folder

  All notebooks for analyzing research questions.

  - `case_num_regional_distribution.ipynb`  
    
    We conducted an analysis of regional and temporal distribution of influenza.

  - `hospitality.ipynb`

    We conducted an analysis of how hospitality is related to the confirmed case number of influenze.

  - `social_impact.ipynb`

    We conducted an analysis of relation between influenza and Google search volume on related topics.

- `report` folder

  The final report notebook which combined all different research questions and also includes the pdf version of report.

## Grading Rubric Walkthrough

We have covered **6** out of 7 topics mentioned in the grading rubric. The crucial topics that we covered are:   

- **Project organization, writeup readability, and overall conclusions**  
  We organized our files and notebooks. The detailed structure, you can refer to **[Organization Overview](#organization-overview)** section. Conclusions are included in the notebooks and final report.

- **Code quality, readability, and efficiency**  
  For all scripts organized under the folder `code`, they are fully documentated. The `code` folder files are a middleware library, where we can use provided interface to fetch the data from different endpoints and the middleware will save the cache and also save the fetched data into the local database automatically.

  You can refer to the documentation of this customized middleware [here](./code/README.md).

- **Data munging**  
  In the analysis of regional and temporal distribution of influenza case number and influenza impact of related search volume on Google, we used `groupby` to conduct regional and temporal analysis. In the cross-comparison of influenze case number and search volume on Google, we also utilized `merge` to merge two data sources and perform analysis based on that. We also transformed `epiweek` into `datetime` by using customized time string format, and use this `timestamp` as the index to plot the time series plot.

  For more details, you can refer to the final pdf report or individual notebook files under folder `notebook`.

- **Data visualization**  
  For each research question, we all performed data visualization. The details plot information can be found in the final report or individual notebook files under folder `notebook`.

- **Data extraction**  
  In this project, we built a middleware to help us to fetch the data from the Web API. The middleware used `request` library to perform the web request. The middleware will also parse the returned json string into pandas dataframe.

- **Data storage**  
  In this project, the middleware we built also handled the data storage. We used `sqlite` to store the data. Meanwhile, we also enabled the cache of the `request` library, which will also automatically save the cached data of API requests into a sql lite database. 

  Since we are using several different endpoints and data source to conduct the analysis, the middleware will store the data from different data sources/endpoints into different tables.

