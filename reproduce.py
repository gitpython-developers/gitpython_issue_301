#!/usr/bin/env python
import git
"""
# this works
url = 'https://github.com/jantman/gitpython_issue_301.git'
"""
# this doesn't
url = 'git@github.com:jantman/gitpython_issue_301.git'
git.Repo().remotes.origin.fetch()
print("done")
