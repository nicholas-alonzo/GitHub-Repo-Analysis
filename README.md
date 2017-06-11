# An Analysis of Contribution Through Issues, Forks and Pull Requests 

GitHub is the largest social coding platform for developers and repository for open source code on the web. There are over 21 million users and more than 56 million repositories to date. In our project, we plan to explore and summarize how contribution takes place through issues, forks, and pull requests. 

__High level question of interest__  
How are issues, forks, and pull requests related and what is the process among these events that lead to contribution to projects on GitHub?

__Why is it important and to whom?__  
Generalizing collaboration habits that make up GitHub can help new or current users understand the processes that make a project active and more well developed.

__Background Literature: What's been done before?__  
[Google Scholar](https://scholar.google.com/scholar?q=github) has various references of studies on GitHub and this site has a compiled a list of analyses using [BigQuery](https://medium.com/google-cloud/github-on-bigquery-analyze-all-the-code-b3576fd2b150), a data warehouse for analytics.

__GitHub data and where to obtain it__
- [API](https://developer.github.com/v3/)
- [Event Archive](https://www.githubarchive.org/) or [Event Archive through BigQuery](https://bigquery.cloud.google.com/dataset/githubarchive:year)
- [BigQuery](https://bigquery.cloud.google.com/dataset/bigquery-public-data:github_repos)  

__Methodology__  
For full details refer to [Sampling Process](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/SamplingProcess.ipynb) on how repositories were selected and [BigQuery Processing](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/BigQueryProcessing_na.ipynb) on how events were processed into a sqlite database.

__Event Exploration and Analysis__  
The analyses can be found [here](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/Event-Exploration_na.ipynb) by Nicholas Alonzo and [here](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/Event-Exploration_ql.ipynb) by Quan Li.

__Data Files__  
All data files referenced in Sampling Process and BigQuery Processing can be downloaded [here](https://mega.nz/#F!LZ0jQQDZ!K4p6b9afXmBYZ2rDhyv5zQ). The most important downloads are github.db used in the analyses and GitHub-Diagram.png to view the database schema.

## Issues: Characteristics & Closing Efficiency 
1. What are the most common words shared among issue titles when they are first opened? (Q)
2. What are the most common ways to write the beginning of an issue when they are first opened and which ones get more closure if any? (Q)
3. How quickly do issues close (not including reopened issues)? (Q)
4. What kind of labels are attached to issues most frequently? (Q)
5. Are issues with labels closed more quickly than those unlabeled (not including reopened issues)? (Q)
6. What percentage of issues are reopened per repo? (Q)

## Forks and Pull Requests: Characteristics and Successful Merges
1. Are pull requests typically open by core contributors or external contributors? (N)
2. What percentage of forks per repo become pull requests? (N)
3. How long does it take for a fork to become a pull request? (N)
4. What percent of pull requests from forks are merged? (N)
5. How quickly are pull requests from forks merged? (N)
6. What are the most common words shared among the titles of merged pull requests from forks? (Q)

## Issues and Pull Requests
1. What percentage of pull requests attempt to close referenced issues? (N)
2. What percentage of issues referenced in the pull request were opened by the same user? (N)
3. Are the issues resolved more by core contributors or external contributors? (N)
4. What is the relative time between when a pull request is opened and references an issue? (N)

## Final Report Link ([here](https://goo.gl/HQHdrx))
