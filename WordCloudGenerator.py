import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

# df = pd.read_csv(r"Youtube04-Eminem.csv", encoding="latin-1")
df = pd.read_csv("Sentiment.csv", error_bad_lines=False)

cloud_words = ''

for val in df.COMMENT:
    val = str(val).lower()
    tokens = val.split()
    cloud_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=300, height=650,
                      background_color='white',
                      min_font_size=10).generate(cloud_words)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()