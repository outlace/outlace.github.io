# Outlace

Pelican project for (outlace.com)[outlace.com] blog

## Develop

To start server on local computer, first cd into the root directory and then run the following command
```
python -m pelican.server
```

## Generate
```
cd /pelican
pelican content -o .. -s pelicanconf.py
```

## Publish

Just push to master
```
git push origin master
```