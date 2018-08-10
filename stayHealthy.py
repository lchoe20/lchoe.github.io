import health
import matplotlib.pyplot as plt
from textblob import TextBlob

from wordcloud import WordCloud

diseaseSearch = 'disease'

list_of_report = health.get_all_reports()

combinedDiseases = ''

for dis in list_of_report:
    combinedDiseases += ' ' + dis['disease']

healthBlob = TextBlob(combinedDiseases)

diseaseDictionary = dict()

for word in healthBlob.words:
    diseaseDictionary[word.lower()] = healthBlob.word_counts[word.lower()]




wordCloud = WordCloud(background_color = 'white').generate_from_frequencies(diseaseDictionary)
plt.title('Diseases in the US')
plt.axis('off')

for dis in list_of_report:
    healthBlob = TextBlob(dis['disease'])


plt.imshow(wordCloud, interpolation = 'bilinear')
plt.show()








plt.show()
