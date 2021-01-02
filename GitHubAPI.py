'''
This file retrieves information from the github V3 API and provides a graphical
representation in a localhost adress.
This program returns a link to that localhost adress usually http://127.0.0.1:56968/
The graphical representation is of the repositories in the logged in users account.
To log in you must replace the accessToken variable with a valid access token.
'''

####################################### Imports ######################################

import base64
import requests
import plotly.graph_objects as go #https://plotly.com/python/
from github import Github   #https://pygithub.readthedocs.io/en/latest/introduction.html
from pprint import pprint

####################################### Functions ######################################

#Prints json nicely
def print_json(username):
    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url).json()
    print('USER DATA')
    pprint(user_data)
    print()


#Prints a PyGithub user object nicely
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


#Prints a PyGithub repo object nicely
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


#Prints a PyGithub user and repo object nicely
def print_user(user):
    #print user profile data
    print_details(user)
    #print users repo data
    for repo in user.get_repos():
        print_repo(repo)


####################################### Main ######################################

#Specify github account
accessToken = 'ff5d7adba0589f0bcecbcaaa5ab78cd59f3d971c'

#Create github object using AccessToken
g = Github(accessToken)

#Get and print user data using PyGithub
user = g.get_user()
#print_user(user)

#Get and print user data using json
#print_json(user.login)

#Create graph object
fig = go.Figure()

#Create array of sizes of repo
views = list()
clones = list()
for repo in user.get_repos():
    views_traffic = repo.get_views_traffic()
    views.append(views_traffic.get("count"))
    clones_traffic = repo.get_clones_traffic()
    clones.append(clones_traffic.get("count"))

    print(views_traffic.get("count"))
    print(clones_traffic.get("count"))
    print(2.* 21/(40.**2))
    print()



#Add repository bubbles to
for repo in user.get_repos():

    #Get commit list / clones and views traffic breakdown for the last week
    commit_list = repo.get_commits()
    clones_traffic = repo.get_clones_traffic()
    views_traffic = repo.get_views_traffic()
    size = 10
    if views_traffic.get("count") > 10:
        size = views_traffic.get("count")

    #print values
    print(repo.name)
    print(views_traffic.get("count"))
    print(clones_traffic.get("count"))
    print(size)
    print()

    #Add create and add bubble trace for each repo
    fig.add_trace(go.Scatter(
        x= [views_traffic.get("count")],
        y= [clones_traffic.get("count")],
        name= repo.name,
        text= ['A<br>placeholder'],
        mode= 'markers',
        marker=dict(
            size=size,
            opacity=[0.5])
        )
    )

#Update the layout of the graph
fig.update_layout(
    title='Clones Traffic v. Count of Views Traffic',
    xaxis=dict(
        title='Count of Views Traffic',
        gridcolor='white',
    ),
    yaxis=dict(
        title='Count of Clones Traffic',
        gridcolor='white',
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)

#Publish Graph
fig.show()
