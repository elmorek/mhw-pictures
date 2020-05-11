# Monster Hunter World image scrapper

This is a scrapper to download all the images for a set of monsters from the WIKI page.

## Requirements:
- beautifulsoup4
- requests
- python-dotenv

## Functions:


```python
get_monster_list() -> list:
```
Gets the list of monsters from http://mhw-db.com

```python
get_monster_image_link(name: str) -> str:
```

Return a URL link to the image of the monster with 700px width.

```python
get_monster_image(url: str, path: str) -> None:
```

Download the URL as an image to the defined path.