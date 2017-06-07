# An Analysis of Contribution Through Issues, Forks and Pull Requests 

GitHub is the largest social coding platform for developers and repository for open source code on the web. There are over 21 million users and more than 56 million repositories to date. In our project, we plan to explore and summarize how contribution takes place through issues, forks, and pull requests. 

__High level question of interest__  
How are issues, forks, and pull requests related and what is the process among these events that lead to contribution to projects on GitHub?

__Why is it important and to whom?__  
Generalizing collaboration habits that make up GitHub will help new or current users understand the processess that make a project active and more well developed.

__Background Literature: What's been done before?__  
GitHub projects listed on [Google Scholar](https://scholar.google.com/scholar?q=github) and a compiled a list of analyses using [BigQuery](https://medium.com/google-cloud/github-on-bigquery-analyze-all-the-code-b3576fd2b150), a data warehouse for analytics.

__GitHub data and where to obtain it__
- [API](https://developer.github.com/v3/)
- [Event Archive](https://www.githubarchive.org/) or [Event Archive through BigQuery]()
- [BigQuery](https://bigquery.cloud.google.com/dataset/bigquery-public-data:github_repos)  

__Methodology__  
For full details refer to [Sampling Process](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/SamplingProcess.ipynb) on how repositories were selected and [BigQuery Processing](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/BigQueryProcessing_na.ipynb) on how events were processed from the Event Archive through BigQuery.

__Event Exploration and Analysis__  
The analyses can be found [here](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/Event-Exploration_na.ipynb) by Nicholas Alonzo and [here](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/Event-Exploration_ql.ipynb) by Quan Li.

__Data Files__  
All data files referenced in Sampling Process and BigQuery Processing can be downloaded from [here](https://mega.nz/#F!LZ0jQQDZ!K4p6b9afXmBYZ2rDhyv5zQ). The most important downloads are github.db used in the analyses and GitHub-Diagram.png to view the relational database schema.

## Issues: Characteristics and Closing Efficiency 
1. What are the most common words shared among issue titles?  
2. How quickly do issues close (not including reopened issues)? 
  - Is there someone who typically opens them per repo? 
  - Does the owner typically close them per repo?
  - What percent of the issues contain the top 3 most common words shared among the titles?  
3. What kind of labels are attached to issues most frequently?
  - Are issues with labels closed more quickly than those unlabeled?  
4. What are the most common ways to write the beginning of an issue across all issues?
  - Which ones get closed more?  
5. What percentage of issues are reopened?
6. What kinds of issues have comment activity even after the issue is last closed?

## Forks: How are they being used?
1. What percentage of forks are pull requests? are not pull requests?
  - How long does it take for a fork to become an open pull request on average?
2. What percent of fork owners have starred the repo? haven't starred the repo?
  - Do they typically star the repo before they fork it or after?

## Pull Requests: Characteristics and Successful Merges
1. What are some characteristics of merged pull requests?
  - What are the most common words shared among pull request titles?
  - Do they have a shorter description?
  - Are there fewer comments before it becomes merged?
2.	Are merged pull requests typically open by core contributors or external contributors? 

## Issues and Pull Requests
1. What does the relationship of issues opened and opened pull requests look like?
2. What percentage of referenced issues are closed by a pull request? not closed?
  - Was the issue opened by the person who opened the pull request?
  - Does an issue typically have 1 pull request?
