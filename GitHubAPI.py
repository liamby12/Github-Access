import base64
from github import Github
from pprint import pprint
import requests


#prints json nicely
def print_json(user_data):
    print('USER DATA')
    pprint(user_data)
    print()


#prints a PyGithub user object nicely
def print_details(user):
    print()
    print("-"*100)
    print("id: ", user.id)
    print("node_id: ", user.node_id)
    print("avatar_url: ", user.avatar_url)
    print("gravatar_id: ", user.gravatar_id)
    print("url: ", user.url)
    print("html_url: ", user.html_url)
    print("followers_url: ", user.followers_url)
    print("following_url: ", user.following_url)
    print("gists_url: ", user.gists_url)
    print("gravatar_id: ", user.gravatar_id)
    print("hireable: ", user.hireable)
    print("html_url: ", user.html_url)
    print("id: ", user.id)
    print("html_url: ", user.html_url)
    print("location: ", user.location)
    print("login: ", user.login)
    print("name: ", user.name)
    print("node_id: ", user.node_id)
    print("organizations_url: ", user.organizations_url)
    print("public_gists: ", user.public_gists)
    print("public_repos: ", user.public_repos)
    print("received_events_url: ", user.received_events_url)
    print("repos_url: ", user.repos_url)
    print("site_admin: ", user.site_admin)
    print("starred_url: ", user.starred_url)
    print("subscriptions_url: ", user.subscriptions_url)
    print("type: ", user.type)
    print("updated_at: ", user.updated_at)
    print("url: ", user.url)
    for repo in user.get_repos():
        print(repo)
    print("-"*100)
    print()


#prints a PyGithub repo object nicely
def print_repo(repo):
    print()
    print("-"*100)

    print("Full name:", repo.full_name)
    print("Description:", repo.description)
    print("Date created:", repo.created_at)
    print("Date of last push:", repo.pushed_at)
    print("Home Page:", repo.homepage)
    print("Language:", repo.language)
    print("Number of forks:", repo.forks)
    print("Number of stars:", repo.stargazers_count)
    print()

    commit_list = repo.get_commits()
    print("commit list")
    pprint(commit_list)
    clones_traffic = repo.get_clones_traffic(per="week")
    print("clones traffic")
    pprint(clones_traffic)
    views_traffic = repo.get_views_traffic(per="week")
    print("views traffic")
    pprint(views_traffic)
    print()

    print("Contents:")
    for content in repo.get_contents(""):
        print(content)

    print("-"*100)
    print()


#prints a PyGithub user and repo object nicely
def print_user(user):
    #print user profile data
    print_details(user)
    #print users repo data
    for repo in user.get_repos():
        print_repo(repo)


#Specify github account
accessToken = 'accessToken'
#username = "username"
#password = "password"

#Create github object using username and password or
#Create github object using AccessToken
#g = Github(username, password)
g = Github(accessToken)

#Get and print user data using json
#url = f"https://api.github.com/users/{username}"
#user_data = requests.get(url).json()
#print_json(user_data)

#Get and print user data using PyGithub
user = g.get_user()
print_user(user)

#Get commit list / clones and views traffic breakdown for the last week
#for repo in user.get_repos():
#    commit_list = repo.get_commits()
#    pprint(commit_list)
#    clones_traffic = repo.get_clones_traffic(per="week")
#    pprint(clones_traffic)
#    views_traffic = repo.get_views_traffic(per="week")
#    pprint(views_traffic)
