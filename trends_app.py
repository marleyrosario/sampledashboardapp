import streamlit as st
import pandas as pd
import openai
from pytrends.request import TrendReq

openai.api_key = "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"

def description(json, keyword):
    chat_log = []
    json = str(json)[:2000]
    system = {"role": "system", "content": f"{json}"}
    chat_log.append(system)
    prompt = {"role": "user", "content": "This data is going to displayed on a streamlit app.  Please return a 100 word description of the results of this Google Trends data from this keyword: " + keyword + "."}
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

def main():
    keyword = st.text_input("Enter a keyword", value="AI", max_chars=None, key=None, type='default')
    df = get_trends_data(keyword)

    gpt3_response = description(df[keyword].to_dict(), keyword).strip()

    st.write(gpt3_response)

    st.line_chart(df[keyword])

if __name__ == "__main__":
    main()
