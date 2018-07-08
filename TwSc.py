from lib import scrap
from lib import tweet

scrap.sC()
if scrap.titlePost in open('post.txt').read():
    print("This is a repetitive post")
else:   
	f=open("post.txt", "a+")
	f.write("\n" + scrap.titlePost)
	tweet.tweeti(scrap.titlePost, scrap.correctUrl)
	print("done")
	

