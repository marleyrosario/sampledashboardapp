import streamlit as st
import pandas as pd

def get_trends_data(keyword):
    url = 'https://storage.googleapis.com/cooking-ai/dataset_google-trends-scraper_2023-07-09_18-52-59-734.csv'
    df = pd.read_csv(url)
    df.set_index('Term / Date', inplace=True)
    return df.loc[keyword]


def main():
    descriptions = {
        'AI': "The search interest for 'AI' has seen some fluctuation over the past year, with peaks in April and October 2023. Interest was relatively low in August and September 2022.",
        'Artificial Intelligence': "Interest in the term 'Artificial Intelligence' peaked in April 2023 and remained relatively stable throughout the year, with some increases in October and December 2022.",
        'Machine Learning': "'Machine Learning' has consistently high search interest throughout the year, with peaks in April 2023. The interest remained stable throughout the rest of the year.",
        'ML': "The term 'ML' has the lowest search interest among the four terms. The interest remained relatively stable throughout the year, with a slight increase in April 2023."
    }
    keyword = st.selectbox("Select a keyword", list(descriptions.keys()))
    df = get_trends_data(keyword)

    st.write(descriptions[keyword])

    st.line_chart(df)

if __name__ == "__main__":
    main()
