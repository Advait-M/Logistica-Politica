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
        curMood = newUser.mood
        curMood = curMood.title()
        newUser.updateParty(newUser.askInfo("party", "string"))
        newUser.addToDB()
        eStuff = newUser.compareWithParty()
        amountError = eStuff[0]
        amountError = round(amountError*100,2)
        emotionsParty = eStuff[1]
        interpretError = newUser.interpretError(amountError)
        partyConfidence = newUser.percentParty()
        print(partyConfidence)
        #Important interface
		# return str((newUser.twitterHandle, newUser.realName, newUser.opinionString, newUser.mood, newUser.politicalParty))
		# listOf(dictOf(Dict) Float listOf(float) Str  Str Str Str
        return render_template("results.html", data = data, amountError = amountError, emotionsParty = emotionsParty, interpretError = interpretError, handle = newUser.twitterHandle, name = newUser.realName, tweet = newUser.opinionString, mood = curMood, party = newUser.politicalParty, partyConfidence = partyConfidence)
@app.route("/howitworks.html")
def showPage():
    return render_template("howitworks.html")
@app.route("/index.html")
def showHome():
    return(render_template("index.html"))
if __name__ == "__main__":
    pydb.LogiticaPolitica().start()
    app.run()
