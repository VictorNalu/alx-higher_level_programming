#!/usr/bin/python3
"""
# Backend Interview:
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""

import requests
import sys

if __name__ == "__main__":

    # Get repository name and owner name from command line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # URL for GitHub API to get commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send GET request to GitHub API
    response = requests.get(url)

    # Check if response status code is successful
    if response.status_code == 200:
        commits = response.json()
        # print the 10 most current commits in the response
        for commit in commits[:10]:
            # Extract commit hash and author name
            commit_hash = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            # Print commit hash and author name
            print(f"{commit_hash}: {author_name}")
    else:
        # Print error message if response status code is not successful
        print("Error: Unable to fetch commits. Status code " +
              str(response.status_code))
