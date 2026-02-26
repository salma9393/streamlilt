import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
import time

st.set_page_config(
    page_title="Image Scraper",
    page_icon="🌍",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align:center;'>Image Scraper</h1>",
    unsafe_allow_html=True
)

with st.form("search"):
    keyword = st.text_input("Enter your keyword")
    search = st.form_submit_button("Search")

placeholder = st.empty()

if search and keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, "lxml")

    rows = soup.find_all("div", class_="ripi6")
    col1, col2 = placeholder.columns(2)

    for index, row in enumerate(rows):
        figures = row.find_all("figure")

        if len(figures) < 2:
            continue

        for i in range(2):
            img = figures[i].find("img")
            anchor = figures[i].find("a")

            if not img or not anchor:
                continue

            img_url = img.get("src")

            if i == 0:
                col1.image(img_url)
                if col1.button("Download", key=f"{index}-{i}"):
                    webbrowser.open_new_tab(
                        "https://unsplash.com" + anchor["href"]
                    )
            else:
                col2.image(img_url)
                if col2.button("Download", key=f"{index}-{i}"):
                    webbrowser.open_new_tab(
                        "https://unsplash.com" + anchor["href"]
                    )

        time.sleep(0.5)
