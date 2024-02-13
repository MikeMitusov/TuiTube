import requests
from bs4 import BeautifulSoup

from settings import current_server


class Video:
    def __init__(self, thumbnail, title, link, author, date, time, views):
        self.thumbnail = thumbnail
        self.link = link
        self.title = title
        self.author = author
        self.published = date
        self.time_play = time
        self.views = views

    def __repr__(self):
        return f"[Video: thumbnail={self.thumbnail}, title={self.title}, link={self.link}, author={self.author}, published={self.published}, time_play={self.time_play}, views={self.views}]"


class Searcher:
    def __init__(self, video_text):
        self.page = 2
        self.response = requests.get(
            f"{current_server}/search?q={video_text}&page={self.page}"
        )
        self.response.encoding = "urf-8"
        self.soup = BeautifulSoup(self.response.text, "lxml")

    def get_video_info(self):
        videos = self.soup.find_all("div", class_="h-box")

        for video in videos[2:-1]:
            if "channel" in video.find("a").get("href"):
                continue

            thumbnail = current_server + video.find("img").get("src")
            title = video.find_all("p")[1].text
            author = video.find("p", class_="channel-name").text
            published = video.find("p", class_="video-data").text
            views = video.find_all("p", class_="video-data")[1].text
            time = video.find("p", class_="length").text
            link = current_server + video.find("a").get("href")

            yield Video(
                thumbnail=thumbnail,
                title=title.strip(),
                link=link,
                author=author.strip(),
                date=published,
                time=time,
                views=views,
            )


a = Searcher("Рецепт пельменей")
for i in a.get_video_info():
    print(i)
