# TuiTube
If you are minimalist then this youtube client with textual interface is for you!

**TuiTube is not ready yet, it is currently under active development, if you want to contribute, read the section below**

## Contributing goals (Short term)
- [ ] Write TUI interface with `curses` python libary, TUI will be inspired by [ranger](https://github.com/ranger/ranger)
- [ ] Add subscriptions, list of subscriptions will store in `settings.py`, example:
```python
# In settings.py
...

subscriptions = ['@channelone', '@channeltwo']
```
- [ ] Add `SearchSubscriptions` class: which will search videos by subscriptions

## Installing
1. You need [Pyhon3.X](https://www.python.org/downloads/) installed
2. Clone repository: `git clone https://github.com/MikeMitusov/TuiTube.git ~/TuiTube`
3. Go to repository directory: `cd ~/TuiTube`
4. Install requirements: `pip install -r requirements`
5. Add support for Android Termux
