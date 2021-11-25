import praw
from matplotlib import pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud
wordList = []
def getUserPass():

    fileObj = open("C:\\Users\\Andre\\Documents\\txt.txt", "r", encoding='utf-8')
    words = fileObj.read().splitlines()
    for i in words:
        wordList.append(i)
getUserPass()
secretKey = wordList[0]# api secret key
personaluse = wordList[1] # READ FROM FILE
reddit = praw.Reddit(client_id = personaluse,
                     client_secret =secretKey,
                     user_agent="<console:HAPPY:1.0>",
                     username = wordList[2],
                     password = wordList[3] # needed pass
)

pinned_post_comments = []
wanted_subreddit1 = reddit.subreddit("wallstreetbets")
count_comments = 0  # this is off by rougly 3000

def getPinnedPost(subreddit_):
    for post in subreddit_.hot(limit=10):  # first n posts
        if post.stickied:  # if post pinned
            return post
    return None

def writeToFile(list, filename):
    textfile = open(f"{filename}.txt", "w", encoding='utf-8')
    #textfile.write('hello')
    for i in list:
        textfile.write(str(i) + ",\n")

    textfile.close()

def createListOfComments(subreddit_):
    local_list = []
    count = 0
    for submission in subreddit_.hot(limit=10):  # first n posts
        for comment in submission.comments:
            if hasattr(comment, "body"):
                count+=1
                #print(comment.body)
                local_list.append(comment.body)

    print(count)
    writeToFile(local_list, 'file')

def readFile(fileName):
    fileObj = open(fileName, "r", encoding='utf-8')  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words

def wordCloud(frequencyCounter):
    wcloud = WordCloud().generate_from_frequencies(frequencyCounter)
    plt.imshow(wcloud, interpolation='bilinear')
    plt.show()

def populateArray(frequnecy_dist_):
    twoDVec_ = []
    for i in frequnecy_dist_:
        for j in i:
            twoDVec_.append(j)
    return twoDVec_

def printSentimentList(full_list_):
    for i in range(len(full_list_)):
        blob = TextBlob(full_list_[i])
        if blob.sentiment.polarity > .2 or blob.sentiment.subjectivity > .2:
            print(f"Text {blob} [SENTIMENT: {blob.sentiment}")

def returnSentimentList(full_list_):
    list_ = []
    for i in range(len(full_list_)):
        blob = TextBlob(full_list_[i])
        if blob.sentiment.polarity > .2 or blob.sentiment.subjectivity > .2:
            list_.append(blob)
    return list_
