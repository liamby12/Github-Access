*Interrogate the GitHub API to retrieve and display data regarding the logged in developer.*
# Github Access
I demonstrated access of the GitHub API in early commits by using JSON via the python "requests" library, as well as using the PyGitHub library.

# Github Visualisation (Interactive)
The [GitHubAPI.py](https://github.com/liamby12/Github-Access/blob/main/GitHubAPI.py) file retrieves information from the [GitHub’s REST API v3](https://developer.github.com/v3/) and provides a graphical representation in a localhost adress.
This program returns a link to that localhost adress usually http://127.0.0.1:XXXXX/ or opens a browser at this adress automatically. The graphical representation is of the repositories in the logged in users account. The visualisation is interactive. You can use tools provided in the top right of the screen to interact with the bubble chart of repositories. When you select a repository you will be able to see further details about it. 
To log in you must replace the accessToken variable with a valid access token.
You can generate an access token at [https://github.com/settings/tokens](https://github.com/settings/tokens). Without an access token the program will not be able to obtain the information it needs for visualisation.

## Plotly
The visualisation library I used is called Plotly. To learn more go to https://plotly.com/python/
This code generates a bubble chart similar to the image below [Link to Image](https://github.com/liamby12/Github-Access/blob/main/liamby%20visualisation.PNG). The bubble chart will vary depending on how many repositories the  logged in user has and how many interactions these repositories have had. I was somewhat limited by the number of repositories that are on my account. The more repositories and interactions that are present the better the chart will appear.

##  PyGithub
I used [PyGitHub](http://pygithub.readthedocs.io/) to develop the Python script [GitHubAPI.py](https://github.com/liamby12/Github-Access/blob/main/GitHubAPI.py).  PyGithub is a Python library to use the [Github API v3](http://developer.github.com/v3).

##Popularity
Popularity is a metric I generated to indicate how much interest there is in a repository. Popularity is generated by using the number of clones, unique clones, views, unique views and stargazers.

## Instructions
To run [GitHubAPI.py](https://github.com/liamby12/Github-Access/blob/main/GitHubAPI.py) please replace the value of the **accessToken = 'Your Access Token'** with your own personal access token and run the file. I recommend that you use a Virtual Environment as this is what I used when working on the project.  
