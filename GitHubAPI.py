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
accessToken = 'Your Access Token'

#Create github object using AccessToken
g = Github(accessToken)

#Get and print user data using PyGithub
user = g.get_user()
print_user(user)

#Get and print user data using json
#print_json(user.login)

#Create graph object
fig = go.Figure()

#Create array of sizes of each repo
views = list()
for repo in user.get_repos():
    views_traffic = repo.get_views_traffic()
    views.append(views_traffic.get("count"))

#Scaler for size of each bubble
sizeref = 2.*max(views)/(40.**2)

#Add repository bubbles to graph
for repo in user.get_repos():

    #Get commit list / clones and views traffic breakdown for the last week
    commit_list = repo.get_commits()
    clones_traffic = repo.get_clones_traffic()
    clones = clones_traffic.get("count")
    unique_clones = clones_traffic.get("uniques")
    views = views_traffic.get("count")
    unique_views = views_traffic.get("uniques")
    views_traffic = repo.get_views_traffic()

    stargazers = repo.stargazers_count

    #Calculate popularity score
    popularity_score = 0
    if stargazers > 0:
        popularity_score += 1
    if stargazers > 10:
        popularity_score += 1
    if stargazers > 100:
        popularity_score += 1
    if stargazers > 1000:
        popularity_score += 1
    if views >= 10:
        popularity_score += 1
    if views >= 100:
        popularity_score += 1
    if views >= 1000:
        popularity_score += 1
    if unique_views < (views/2):
        popularity_score -= .5
    if clones >= 2:
        popularity_score += .5
    if clones >= 10:
        popularity_score += 1
    if clones >= 100:
        popularity_score += 1
    if popularity_score >= 10:
        popularity_score = 10
    if popularity_score <= 0:
        popularity_score = 0

    #Create strings to display info on repositories
    clones_text = 'Clones = ' + str(clones) + '<br>'
    unique_clones_text = 'Unique Clones = ' + str(unique_clones) + '<br>'
    views_text = 'Views = ' + str(views) + '<br>'
    unique_views_text = 'Unique Views = ' + str(unique_views) + '<br>'
    stargazers_text = 'Stargazers = ' + str(stargazers) + '<br>'
    divider_string = '-'*10 + '<br>'
    popularity_score_text = 'Popularity Score ' +  str(popularity_score) + '/10'
    text = clones_text + unique_clones_text + views_text + unique_views_text + stargazers_text + divider_string + popularity_score_text

    #print values
    print("repo name = ",repo.name)
    print(text)

    #Add create and add bubble trace for each repo
    fig.add_trace(go.Scatter(
        x= [views_traffic.get("count")],
        y= [clones_traffic.get("count")],
        name= repo.name,
        text= [text],
        mode= 'markers',
        marker=dict(
            size=[views_traffic.get("count") + 1],
            sizemode='area',
            sizeref=sizeref,
            sizemin=4)
        )
    )

#Update the layout of the graph
fig.update_layout(
    title='Clones Traffic vs Views Traffic for ' +  str(user.login),
    xaxis=dict(
        title='Views Traffic',
        gridcolor='white',
    ),
    yaxis=dict(
        title='Clones Traffic',
        gridcolor='white',
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)

#Publish Graph
fig.show()
