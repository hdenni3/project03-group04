# project03-group04 - https://hdenni3.pythonanywhere.com/
Project 3

Purpose: Develop an Interactive Data Application:

The objective is to build a data-centric application that communicates insights through interactive visualizations, providing a user-friendly experience for exploring data independently

Project Overview
Database: Global YouTube Statistics 2023

Key measures including subscribers, video views, categories, and revenue are the subject of this all-encompassing study of YouTube success on a worldwide scale. The project's overarching goal is to highlight successful YouTube channels and to track global trends in the popularity of various types of videos. By using a data-driven approach, we investigate how demographics relate to the number of popular YouTube channels by nation, shedding light on what makes YouTube so popular throughout the globe. The project's interactive visualizations and dashboards are powered by a full-stack data application that utilizes Flask, SQLite, and a variety of front-end technologies.

Comprehensive Application Development:

Backend Implementation (Flask + SQLite): Utilize Flask as the backend framework to manage user interactions and database operations. Employ SQLite as the database system, executing queries based on user inputs and filters.

Frontend Development (HTML/JavaScript): Utilize HTML and JavaScript for the frontend to create dynamic visualizations and enhance user engagement.

Interactive Dashboard Feature:

The application will present a dashboard where users can apply filters and observe real-time updates in the visualizations. The dashboard will host multiple visualizations such as charts, maps, etc., responding to user interactions.

Geospatial Visualization Component:

Incorporate an interactive map visualization to present geographical data effectively. Enable users to explore data geographically through interactive map features.

Key Deliverables:

Application Components:

app.py: Primary Flask application file managing routing, user interactions, and serving the frontend.

SQLHelper.py: Auxiliary module containing SQL query functions for database interactions. database.sqlite: SQLite database file containing relevant data tables.

HTML Components:

Main/Home Landing Page: Introduction to the project, its objectives, and an overview of functionalities. 

Dashboard Page: Includes customizable filters for users to tailor displayed data. Incorporates visualizations using Plotly.  A tabular dropdown data display with filters dynamically. Provides user guidance for interacting with the dashboard effectively. 

Map Page:Features an interactive map visualization. Integration of a Leaflet map with advanced features like marker clusters and heatmap to enhanced geographical data exploration.

About Us Page: brief sumary of the project, team, contributors. Also included works cited and technology used logos.
JavaScript Components:

Libraries: 

Leaflet for map visualizations. Plotly for interactive charts and graphs. Bootstrap Grid and Bootswatch for layout and styling. Potential use of additional JavaScript libraries like Highcharts.js, charts.js, or D3 for visualization enhancements.

Python Components:

Database Notebook: Jupyter notebook for creating the SQLite database was required. Exploratory Data Analysis to understand the dataset and determine visualization strategies. Also tested SQL queries before integrating them into the Flask application.

Technology Used Prerequisites

Python 3.8+, Flask, SQLite3, Pandas, Plotly, Leaflet, D3, Visual Studio Code.

Interaction

Homepage: Presents an introduction to the project with an overview of the data-driven approach. Growth and Trends Dashboard: Interactive charts that display trends in subscriber growth, most popular content categories, and channels with the highest video views. Country Comparisons: Compare YouTube channels from different countries in terms of average subscribers and views. Population Correlation Analysis: Examine the correlation between a country's population and the number of top-ranked YouTube channels it has.

Ethical Considerations

This project involves analyzing and presenting publicly available YouTube data. We made careful efforts to ensure the data used is aggregated and anonymized, avoiding any personal or sensitive information. 

Data Sources

YouTube Data: Kaggle Dataset - YouTube Statistics
https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023

References

Flask and SQLite Documentation
Flask Documentation
Flask. (n.d.). Flask Documentation. Retrieved from https://flask.palletsprojects.com/

SQLite Documentation
SQLite. (n.d.). SQLite Documentation. Retrieved from https://sqlite.org/docs.html

Frontend Libraries and Tools
Leaflet
Leaflet. (n.d.). Leaflet JavaScript Library. Retrieved from https://leafletjs.com/

Plotly
Plotly. (n.d.). Plotly JavaScript Library. Retrieved from https://plotly.com/javascript/

Bootstrap Grid
Bootstrap. (n.d.). Bootstrap Grid System. Retrieved from https://getbootstrap.com/docs/5.0/layout/grid/

Bootswatch
Bootswatch. (n.d.). Bootswatch Themes. Retrieved from https://bootswatch.com/

Highcharts.js
Highcharts. (n.d.). Highcharts JavaScript Charting Library. Retrieved from https://www.highcharts.com/

Charts.js. (n.d.). 
Charts.js Documentation. Retrieved from https://www.chartjs.org/

D3.js. (n.d.). 
D3.js - Data-Driven Documents. Retrieved from https://d3js.org/

Python Tools and Notebooks
Jupyter Notebooks
Project Jupyter. (n.d.). Jupyter Documentation. Retrieved from https://jupyter.org/

Pandas. (n.d.). Pandas Documentation. Retrieved from https://pandas.pydata.org/

Data Visualization Best Practices
Tableau. (n.d.). Data Visualization Best Practices. Retrieved from https://www.tableau.com/learn/articles/data-visualization-best-practices

Bootcamp Exercises Samples and AI: 
DATA-PT-EAST-APRIL-041524-MTTH-CONS Xpert Learning Assistant EdX platform
DATA-PT-EAST-APRIL-041524-MTTH-CONS Lesson Practice Activity Module 15 Alexander Booth.
