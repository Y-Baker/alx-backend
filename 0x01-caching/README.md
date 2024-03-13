<div align="center">
  <img src="https://cdn.pixabay.com/photo/2013/07/12/17/22/database-152091_640.png" alt="Storage" width="120"/>
</div>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=900&size=32&pause=1000&width=435&lines=Caching\(:)](https://git.io/typing-svg)


## Create an Environment
```bash
cd myproject
python3 -m venv .venv  # you can use any name instead of .venv
```
<br />

## Activate the Environment
```bash
source .venv/bin/activate  # the path of the acitvate file in bin of the environment
```
<br />

## Installation Python:
```bash
sudo apt update -y
sudo apt install python3
python3 --version
```
<br />

## Install mypy by pip
```bash
pip install mypy
```
<br />


## Starting Class:

```py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```
<br />


## Authors :black_nib:

* __Yousef Bakier__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
 &nbsp;&nbsp;[<img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">](https://github.com/Y-Baker)
