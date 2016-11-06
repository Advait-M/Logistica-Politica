from flask import Flask, render_template, request
import pyredb as pydb
import Backend as twitData
import userDataClass as udc
import config

app = Flask(__name__)
@app.route("/")
def index():
	handle = request.args.get("handle")
	if handle == None:
		
		return render_template("index.html")
	else:
		data = pydb.LogiticaPolitica().getAll()
		newUser = udc.UserData()
		newUser.updateHandle(handle)
		tweets = twitData.getTweets(handle)
		newUser.updateRealName(tweets[0])
		newUser.updateOpinion(tweets[1])
		newUser.updateMood(newUser.askInfo("mood", "string"))
		newUser.updateParty(newUser.askInfo("party", "string"))
		newUser.addToDB()
		return str((newUser.twitterHandle, newUser.name, newUser.opinion, newUser.mood, newUser.party))
		# return render_template("results.html", handle = newUser.twitterHandle, name = newUser.name, tweet = newUser.opinion, mood = newUser.mood, party = newUser.party)

if __name__ == "__main__":
	pydb.LogiticaPolitica().start()
	app.run()
