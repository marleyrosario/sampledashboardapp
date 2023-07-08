import streamlit as st
import pandas as pd
import altair as alt
import openai
from pytrends.request import TrendReq

openai.api_key = "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"

def description(json):
    chat_log = []
    json = str(json)[:2000]
    system = {"role": "system", "content": f"{json}"}
    chat_log.append(system)
    prompt = {"role": "user", "content": "This data is going to displayed on a streamlit app. Please return a 100 word description of this Google Trends data"}
    chat_log.append(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        temperature = .75,
        )
    message = response['choices'][0]['message']['content']
    return message

@st.cache_data
def get_trends_data(keyword):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], timeframe='today 5-y')
    df = pytrends.interest_over_time()
    return df

def plot_line_chart(df, keyword):
    chart = alt.Chart(df).mark_line().encode(
        x='date:T',
        y=keyword,
        tooltip=['date:T', keyword]
    ).properties(
        title=f'Google Trends data for {keyword}',
        width=600
    )
    chart.encoding.x.title = 'Date'
    chart.encoding.y.title = 'Trend Index'
    return chart

def main():
    keyword = st.text_input("Enter a keyword", value="Bitcoin", max_chars=None, key=None, type='default')
    df = get_trends_data(keyword)

    gpt3_response = description(df[keyword].to_dict()).choices[0].text.strip()
    st.text(gpt3_response)

    st.altair_chart(plot_line_chart(df, keyword), use_container_width=True)

if __name__ == "__main__":
    main()
