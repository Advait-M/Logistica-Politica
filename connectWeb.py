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
		eStuff = newUser.compareWithParty()
		amountError = eStuff[0]
		emotionsParty = eStuff[1]
		interpretError = newUser.interpretError(amountError)

		# return str((newUser.twitterHandle, newUser.realName, newUser.opinionString, newUser.mood, newUser.politicalParty))
		return render_template("results.html", data = data, amountError = amountError, emotionsParty = emotionsParty, interpretError = interpretError, handle = newUser.twitterHandle, name = newUser.realName, tweet = newUser.opinionString, mood = newUser.mood, party = newUser.politicalParty)

if __name__ == "__main__":
	pydb.LogiticaPolitica().start()
	app.run()
