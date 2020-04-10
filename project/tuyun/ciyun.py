import jieba
from imageio import imread
from wordcloud import WordCloud

photo = imread(r'D:\python-3.6.5-amd64\project\tuyun\test.jpg')
fonts = r'C:\Windows\Fonts\STFANGSO.TTF'
citxt = r'D:\python-3.6.5-amd64\project\tuyun\test.txt'

def ciyun():
    with open(citxt) as f:
        txt=f.read()
    words=jieba.lcut(txt)
    nextword=' '.join(words)
    wordshow=WordCloud(background_color='white',width=800,height=600,max_words=500,max_font_size=80,min_font_size=10,font_path=fonts,mask=photo).generate(nextword)
    wordshow.to_file(r'D:\python-3.6.5-amd64\project\tuyun\cy.jpg')

if __name__=='__main__':
    ciyun()