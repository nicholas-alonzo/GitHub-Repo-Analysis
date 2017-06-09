# An Analysis of Contribution Through Issues, Forks and Pull Requests 

GitHub is the largest social coding platform for developers and repository for open source code on the web. There are over 21 million users and more than 56 million repositories to date. In our project, we plan to explore and summarize how contribution takes place through issues, forks, and pull requests. 

__High level question of interest__  
How are issues, forks, and pull requests related and what is the process among these events that lead to contribution to projects on GitHub?

__Why is it important and to whom?__  
Generalizing collaboration habits that make up GitHub will help new or current users understand the processes that make a project active and more well developed.

__Background Literature: What's been done before?__  
GitHub projects listed on [Google Scholar](https://scholar.google.com/scholar?q=github) and a compiled a list of analyses using [BigQuery](https://medium.com/google-cloud/github-on-bigquery-analyze-all-the-code-b3576fd2b150), a data warehouse for analytics.

__GitHub data and where to obtain it__
- [API](https://developer.github.com/v3/)
- [Event Archive](https://www.githubarchive.org/) or [Event Archive through BigQuery](https://bigquery.cloud.google.com/dataset/githubarchive:year)
- [BigQuery](https://bigquery.cloud.google.com/dataset/bigquery-public-data:github_repos)  

__Methodology__  
For full details refer to [Sampling Process](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/SamplingProcess.ipynb) on how repositories were selected and [BigQuery Processing](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/BigQueryProcessing_na.ipynb) on how events were processed into a database.

__Event Exploration and Analysis__  
The analyses can be found [here](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/Event-Exploration_na.ipynb) by Nicholas Alonzo and [here](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/Event-Exploration_ql.ipynb) by Quan Li.

__Data Files__  
All data files referenced in Sampling Process and BigQuery Processing can be downloaded from [here](https://mega.nz/#F!LZ0jQQDZ!K4p6b9afXmBYZ2rDhyv5zQ). The most important downloads are github.db used in the analyses and GitHub-Diagram.png to view the database schema.

## Issues: Characteristics and Closing Efficiency 
1. What are the most common words shared among issue titles when they are first opened? (Q - HP)  
    - Show using a word cloud or barplot (Finished)
2. How quickly do issues close (not including reopened issues)? (Q - HP)  
    - Show with a histogram or density plot (Finished)
3. What kind of labels are attached to issues most frequently? (Q - HP)  
    - Show with a barplot (Finished)
    - Are issues with labels closed more quickly than those unlabeled (not including reopened issues)? (Split the data by labeled and unlabeled and then find out how quickly they are closed for both data sets)
4. What are the most common ways to write the beginning of an issue across all issues when they are first opened if any? (Q - LP)      
    - Use the first 5 words as the "beginning of an issue" (refer [here](https://medium.com/google-cloud/analyzing-github-issues-and-comments-with-bigquery-c41410d3308))
    - Which ones get closed more if any?
5. What percentage of issues are reopened per repo? (Q - LP)  
    - Show with a barplot / pie chart (Finished)

## Forks: How are they being used?
1. What percentage of forks are pull requests? are not pull requests? (N - HP)  
    - How long does it take for a fork to become an open pull request? (Finished)
2. What percent of fork owners have starred the repo? haven't starred the repo? (N - HP)  
    - Do they typically star the repo before they fork it or after?

## Pull Requests: Characteristics and Successful Merges
1. What are the most common words shared among the titles of merged pull requests? (Q - HP)  
    - Show with a barplot or word cloud (Finished)
2. Are merged pull requests typically open by core contributors or external contributors? (N - HP) (Finished)

## Issues and Pull Requests
1. What does the relationship of issues opened and opened pull requests look like? (N - HP)
    - Show with a scatter plot (Finished)
2. What percentage of pull requests attempt to close referenced issues?? (N - HP)
    - Was the issue opened by the person who opened the pull request?
    - Are the issues resolved more by core contributors or external contributors?