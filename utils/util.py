import dash_html_components as html
import random

def generateFrequency(text):
    value = {}
    words = []
    freq = []
    text = text.split(" ")
    for x in text:
        if x not in value:
            value[x] = 1
        else:
            value[x] += 1
    for x in value:
        words.append(x)
        freq.append(value[x])
    return [words, freq]

def colorWord(text,value,color):
    return html.Span(text,style={'color':color}, title=value)

def makeTokens(text, metric, colorMaper):
    tokenArray = []
    for x in text.split(" "):
        if x in colorMaper:
            tokenArray.append(colorWord(x,str(metric[x]),colorMaper[x]))
            tokenArray.append(html.Span(" ",style={'color':"white"}))
        else:
            tokenArray.append(html.Span(x,style={'color':"black"}))
            tokenArray.append(html.Span(" ",style={'color':"white"}))
    return tokenArray

def colorMaper(metric):
    r = lambda: random.randint(0,0xFFFFFF)
    colorMaper = {}
    for word in metric:
        colorMaper[word] = f"#%06x"%r()
    return colorMaper
