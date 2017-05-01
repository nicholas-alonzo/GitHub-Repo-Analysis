import os
import requests
import requests_cache
import lxml.html as lx
import wget
import pandas as pd
import json

# Downloads the events at all the hours at a given date
def download_events(files_to, ymd, to_endDay=None):
    """
    :param files_to: (str) file path to put requested files in
    :param ymd: (str) date to download from, formatted 2012-01-01
    :param to_endDay: (int) how many days after day in ymd to download
    :return: downloaded files into directory 
    """

    url_list = []

    if to_endDay is None:

        for hours in range(0, 24):
            url_list.append('http://data.githubarchive.org/%s-%s.json.gz' % (ymd, hours))

        for url in url_list:
            try:
                response = requests.get(url)
                response.raise_for_status()
                wget.download(url, files_to)
                print "Downloaded %s" % url
            except:
                print "Could not download %s" % url

    else:
        from_startDay = int(ymd.split('-')[2])
        day_range = []
        for days in range(from_startDay, to_endDay + 1):
            day_range.append("%02d" % days)

        for day in day_range:
            ymd_split = ymd.split('-')
            ymd_split[2] = day
            ymd = '-'.join(ymd_split)

            for hours in range(0, 24):
                url_list.append('http://data.githubarchive.org/%s-%s.json.gz' % (ymd, hours))

            for url in url_list:
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    wget.download(url, files_to)
                    print "Downloaded %s" % url
                except:
                    print "Could not download %s" % url


# unzips the downloaded files from download_events()
def unzip_files(files_path, command=None):
    """
    :param files_path: path to where the files were downloaded to
    :param command: the command right after gunzip to unzip a file
    :return: unzipped files in directory
    """

    cwd = os.getcwd()
    os.chdir(files_path)

    if command is None:
        os.system('gunzip *.json.gz')
    else:
        command = 'gunzip %s' % command
        os.system(command)

    os.chdir(cwd)


# make pandas df from json file
def make_df(file):
    """
    :param file: 
    :return: a pandas DF of the file extracted
    """
    data = []
    with open(file) as f:
        for line in f:
            data.append(json.loads(line))

    return pd.DataFrame(data)


# find root repositories created
def find_rootrepos(df, cache='cache'):
    """
    :param df: pandas DF
    :param cache: name of cache
    :return: a subset of df with the following conditions applied
            - not from an organization
            - are repos
            - are not github.io projects
            - exists to date
            - have at least 3 contributors to date
    """
    # not from an organization
    cond1 = df['type'] == 'CreateEvent'
    cond2 = pd.isnull(df['org'])

    df_sub = df[cond1 & cond2]
    df_sub = df_sub.reset_index(drop=True)

    # are repos
    df_sub_payload = df_sub['payload'].tolist()
    df_sub_payload = pd.DataFrame(df_sub_payload)

    ghpl = df_sub_payload[pd.isnull(df_sub_payload['ref'])]
    keep_rows = ghpl.index.values

    df_sub = df_sub.iloc[keep_rows]
    df_sub = df_sub.reset_index(drop=True)

    # are not github.io OR
    df_sub_repos = df_sub['repo'].tolist()
    df_sub_repos = pd.DataFrame(df_sub_repos)

    ghio = df_sub_repos[~df_sub_repos['name'].str.contains('.github.io|github.com')]
    keep_rows = ghio.index.values

    df_sub = df_sub.iloc[keep_rows]
    df_sub = df_sub.reset_index(drop=True)

    # exists
    # have at least 3 contributors to date
    df_sub_repos = df_sub['repo'].tolist()
    df_sub_repos = pd.DataFrame(df_sub_repos)

    repo_names = df_sub_repos['name'].tolist()

    L = []
    indicies = 0

    for name in repo_names[:50]:

        requests_cache.install_cache(cache)
        url = 'https://github.com/%s/contributors_size' % name
        try:
            response = requests.get(url)
            response.raise_for_status()
            html = lx.fromstring(response.text)
            contr_count = html.xpath("number(//span/text())")
            if contr_count > 3:
                L.append(indicies)
            else:
                pass
        except:
            pass

        indicies += 1

        return df_sub.iloc[L]

# RESOURCES
# https://stackoverflow.com/questions/7656754/place-a-0-in-front-of-numbers-in-a-list-if-they-are-less-than-ten-in-python
