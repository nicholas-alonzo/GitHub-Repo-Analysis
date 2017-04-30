# GitHub-Repo-Analysis

GitHub is the largest social coding platform for developers and repository for open source code on the web. There are over 21 million users and more than 56 million repositories to date. In our project, we plan to explore key indicators that characterize root repositories as completed, uncompleted, or abandoned.

__High level question of interest__
What are key indicators that characterize repository projects as completed, uncompleted, or abandoned?

__Why is it important and to whom?__
It would be helpful to understand user collaboration habits that characterize repositories. It would be another addition to the many GitHub related analyses.

__Background Literature: Whats been done before?__
- GitHub projects on listed on [Google Scholar](https://scholar.google.com/scholar?q=github)
- A compiled a list of analyses using [BigQuery](https://medium.com/google-cloud/github-on-bigquery-analyze-all-the-code-b3576fd2b150)

__The data and how we will obtain it__
There are 3 main sources for GitHub's data
- [GitHub API](https://developer.github.com/v3/)
- [GitHub Archive](https://www.githubarchive.org/)
- [GitHub BigQuery Tables](https://bigquery.cloud.google.com/dataset/bigquery-public-data:github_repos)

We will have our focus on the GitHub Archive data which records the different [event types](https://developer.github.com/v3/activity/events/types/) from the GitHub API.

__Hypotheses__
1. We expect completed repository projects to have no more activity after having gone through pushing commits, issues being raised and closed, accepting pull requests and perhaps a release event occurring. Issues may be raised after development, but no active response to it.
2. We expect uncompleted repository projects to have a cycle of commits, issues being raised and closed, accepting pull requests. The repo may be forked, but there is still a cycle continuing.
3. We expect abandoned repository projects to have gone through a cycle of commits, and multiple issues that have no active response and then perhaps a spike in forked repos.

These are what we expect to find, however once we see our variables we will define this clearer

__Methodology__
We select the repositories using the following criteria:
1. Select all root repositories created January 1st 2016 that are not github.io
2. From there check the repositories that ...
  - not from an organization
  - have at least 2 contributors to date
  - are not empty
  - have more than just a README.md file
3. Randomly sample 100 of those repositories

We choose January 1st 2016 so we can track at least a year’s worth of progress among the root repositories and so that they are on a similar timeline. We also decided to sample 100 of these repositories because a years worth of event tracking is enough data to gain insight from