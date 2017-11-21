## Logistica-Politica

**Background and Problem**

Our group had been paying attention to the United States presidential election. We had noticed that the election had become less about actual policy and more about how people feel about the two parties. After noticing this, the next question to ask was "How do the members of each party actually feel?" Are they angry, fearful, or even happy? After some discussion, we found a way to figure out how they're feeling: by listening to what they're saying.

**How It Works**

A user can input the twitter handle of an individual. Our program will collect a series of that user's tweet and create a large string. Using twitter data, it is possible for a user to find the most likely political affiliation of a string using the machine learning website Indico. If we give this large string that we have created to Indico, then we can find the political leaning and overall emotional sentiment of the user. This helps for one user, but with the use of a database like Firebase, like we have in our program, it is possible to collect the party affiliations and the emotional sentiments of many users. By grouping people into their parties, we can find the average emotional sentiment of a large sample of a party, that we use to make statistics about the emotional sentiment of a political group.

**Uses**

This can be helpful to predict how a political group feels about the election. Having the overall emotions of a group could help in making preliminary findings about a survey. For instance, if we happen to know that Green voters have an overall emotional sentiment of fearful, then we can have some idea about what results we would get if we surveyed the group. We could also begin to reason as to why a certain group feels a certain way at a certain time, in order to find how a particular event is affecting the election.

**Technologies used**
* Flask
* Python 3
* HTML
* JavaScript
* Jinja 2
* JQuery
* CSS
* Indico (API calls)
* Twitter (API calls)
* Heroku (server)

**Challenges Faced**
* Integrating the backend and frontend
* Implementing the Heroku server
* Using Flask in Python
* Creating a webapp using JQuery
* Using version control effectively

**Future Steps**

In the future, we would love to place a geographic component to the analysis.We know that tweets can be geocoded, and so using that or another method, we believe that it would be possible to determine where the user lives and factor that into the party affiliation. Certain states have higher proportions of a certain voter, so including the geographic component could prove to be valuable.
