# GitHub-Repo-Analysis

GitHub is the largest social coding platform for developers and repository for open source code on the web. There are over 21 million users and more than 56 million repositories to date. In our project, we plan to explore the relation between raised issues from root repositories and their forked counterparts.

__High level question of interest__
How related are issues and forks and do these lead to contribution to projects on GitHub?

__Why is it important and to whom?__
It would be helpful to understand and generalize collaboration habits that make up GitHub. It would be another addition to the many GitHub related analyses.

__Background Literature: What's been done before?__
- GitHub projects on listed on [Google Scholar](https://scholar.google.com/scholar?q=github)
- A compiled a list of analyses using [BigQuery](https://medium.com/google-cloud/github-on-bigquery-analyze-all-the-code-b3576fd2b150), a data warehouse for analytics.

__The data and how to obtain it__
There are 3 main sources to GitHub's data
- [GitHub API](https://developer.github.com/v3/)
- [GitHub Event Archive & via BigQuery](https://www.githubarchive.org/)
- [GitHub BigQuery Tables](https://bigquery.cloud.google.com/dataset/bigquery-public-data:github_repos)

We will use the GitHub API to select repos and then use BigQuery to select events from the Event Archive and the different types of events listed [here](https://developer.github.com/v3/activity/events/types/) from the GitHub API.

__Methodology__
- Refer to [SamplingProcess](https://github.com/nicholas-alonzo/GitHub-Repo-Analysis/blob/master/SamplingProcess.ipynb) on how we selected repositories.

- Refer to BigQueryProcessing_na & BigQueryProcessing_ql on how we extracted the event data for exploration

__Data Files__
All large data files can be downloaded from here  

https://mega.nz/#F!LZ0jQQDZ!K4p6b9afXmBYZ2rDhyv5zQ