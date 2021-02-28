import os

env_pr_branch = "System.PullRequest.SourceBranch"
default_branch = "Build.SourceBranchName"

branch_name = ""
if env_pr_branch in os.environ:
    branch_name = os.environ[env_pr_branch].replace("/", "-")

branch_name = os.environ[default_branch].replace("refs/heads/", "")

print("##vso[task.setvariable variable=branchName]%s" %  branch_name)
