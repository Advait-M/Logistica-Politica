from twitter import *
import time
config = {}
with open("config.py") as f:
    code = compile(f.read(), "config.py", 'exec')
    exec(code, config)
f.close()
twitter = Twitter(
auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
def getTweets(handle):

    print(handle)
    results = twitter.statuses.user_timeline(screen_name = handle)
    if results != []:
        # print(results)
        # print()
        statii = []
        print(results)
        #print(results[0])
        uName = results[0]["user"]["name"]
        print(uName)
        for status in results:
            statii.append(status["text"])
        # print(statii)
        textS = " ".join(statii)
        while "\n" in textS:
            i = textS.index("\n")
            textS = textS[0:i] + textS[i+1:]

        print(textS)
        print([uName, textS])
        return [uName, textS]
    else:
        return[]
if __name__ == "__main__":
    getTweets("POTUS")