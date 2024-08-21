import  wikipedia
# wiki=wikipedia.page('Artificial intelligence')
# text=wiki.content
text="""According to Nietzsche, it is the Apollonian-Dionysian struggle for power that makes life worth living, and in Damien Chazelle’s film, Whiplash, the collapse of this Apollonian-Dionysian balance destroys the power of music, wreaking havoc on the main character’s life. In this film, the popular growing-up narrative, with its dominance of Apollonian reason, is ingeniously transformed into a fascinating enlightenment film, centering on a student’s search for his path in music and life. This paper first explores the significance of enlightenment in regard to music and life and the crisis caused by a predominant Apollonian drive, through the relationship between enlightenment and music in Whiplash. It then examines the possibility of self-enlightenment and the rebirth of music through a restoration of balance between the two fundamental life-drives."""
print(text)

from wordcloud import WordCloud
wd=WordCloud(width =2000, height = 1500).generate(text)


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(wd)
plt.show()