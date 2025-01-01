from feedgen.feed import FeedGenerator
from datetime import date

startDate = date(2025, 1, 1)

postLim = 1993

fg = FeedGenerator()
fg.id('https://dojeedev.github.io/' )
fg.title('Comics')
fg.link( href='https://dojeedev.github.io/' )
fg.subtitle('This is a cool feed!')
fg.language('en')

today = date.today()
delta = (today - startDate) 
num = delta.days + 1

NumOfPosts = 3

for p in range(NumOfPosts):
    n = (num + p) % postLim
    if n == 0:
        n = 1
    fe = fg.add_entry()
    fe.id('https://dojeedev.github.io/PHD/' + str(n) + '.html')
    fe.title(str(n))
    fe.link(href="https://dojeedev.github.io/PHD/" + str(n) + '.html')

rssfeed  = fg.rss_str(pretty=True) # Get the RSS feed as string
fg.rss_file('rss.xml') # Write the RSS feed to a file

