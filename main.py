import requests
import shutil
from dotenv import load_dotenv
load_dotenv()
import os
from bs4 import BeautifulSoup


def get_monster_image_link(name: str) -> str:
    """
    Function that given the name of a monster, returns the image URL from MHW Wiki Page.
    :param name: Name of the monster
    :return: URL to the image.
    """
    r = requests.get(f'{os.getenv("MHW_WIKI_URL")}{name}')
    if r.status_code == 200:
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        images = soup.find_all('img')
        image = [image["src"] for image in images if image.has_attr('srcset')]
        if len(image) > 0:
            return f'{image[0].split("?")[0][:-3]}700'


def get_monster_list() -> list:
    """
    Function that gets the list of monsters available on MHW DB API.
    :return: List of monsters.
    """

    r = requests.get(f'{os.getenv("MHW_API_URL")}monsters')
    if r.status_code == 200:
        monsters = r.json()
        monster_names = [monster["name"] for monster in monsters]
        return monster_names
    else:
        return None


def get_monster_image(url: str, path: str) -> None:
    """
    Function that download and stores the monster image and stores it in the destination path.
    :param url: URL of the image
    :param path: Path to store the image
    :return:
    """
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def main():
    monsters = get_monster_list()
    for monster in monsters:
        image_link = get_monster_image_link(monster)
        print(image_link)
        get_monster_image(image_link, f'{os.getenv("STORAGE_PATH")}\\{monster}.png')


if __name__ == '__main__':
    main()

