# Outlace

Pelican project for (outlace.com)[outlace.com] blog

## To add a blog page

- Add jupyter notebook to `/pelican/content` directory
- Add meta jupyter notebook file (same name with suffix `-meta`) in `/pelican/content`
- Generate template files

```
# must be in /pelican directory
pelican content -o .. -s pelicanconf.py
```

- Just push to master

```
git push origin master
```

## Run blog locally

To start server on local computer, first cd into the root directory and then run the following command
```
python -m pelican.server
```
Server starts on `http://localhost:8000/`

