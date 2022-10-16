import plotly.graph_objects as go
# plotly=1.16.0
color_lst = ['red', 'green']
def bar_color_func(score, color_lst):
    if score < 0:
        return color_lst[0]
    else:
        return color_lst[1]
def plotly_graph (stock, score, bar_color):
    bar_color = bar_color_func(score, color_lst)
    fig = go.Figure(go.Indicator(
       domain = {'x': [0, 1], 'y': [0, 1]},
       value = score,
       mode = "gauge+number",
       title = {'text': f"Sentiment Score of {stock}"},
       # delta = {'reference': 0},
       gauge = {'axis': {'range': [-1, 1]},
                'bar': {'color': bar_color},
                'steps' : [
                    {'range': [-1, 0], 'color': "lightskyblue"},
                    {'range': [0, 1], 'color': "cyan"}],
                'threshold' : {'line': {'color': "darkblue", 'width': 4}, 'thickness': 0.75, 'value': 0.99}
        }
    ))
    return fig
stock = 'AAPL'
score = -100
while score < -1 or score > 1:
    score = input("Enter the sentiment score: ")
    score = float(score)
print(f"The sentiment score is {score}")
bar_color = bar_color_func(score, color_lst)
fig = plotly_graph(stock, score, bar_color)
fig.show()

