Title: Announcement
Date: 2017-04-26 19:41
Category: Announcement
Author: Brandon Brown
Summary: Some announcements about this blog's migration to a different static site generator as well as some new GitHub repos I've created.
---

I've decided to migrate this blog to Pelican from Jekyll. I did this largely because
Pelican has a plugin for allowing Jupyter notebooks to be served automatically
as blog posts. With Jekyll, I had to use nbconvert to convert my ipynb document to html
every time I wanted to publish a new post, and I also had to often manually edit that html document to get it formatted correctly when embedded into the site. That was fine once, but if you want to make
edits or updates, it becomes a real hassle. Now I can directly edit the notebook
and the post will automatically update. There are a number of typos and code bugs
in some of my old posts that I just never got around to fixing because it was
so annoying to re-publish the post. But now I will work on them. Unfortunately some formatting/display
issues have arisen from the migration but I will fix them all soon.

Additionally, I've created some GitHub repos for some of the code used in various projects.
Namely, I've turned the Gridworld game from RL part 3 into a separate project on GitHub
so you can use it in other projects more easily. Find it here: <a href="https://github.com/outlace/Gridworld">https://github.com/outlace/Gridworld</a>

I also made a simple Data Augmentation library for creating synthetic image data
from originals so you can amplify your data for use in deep learning models.
You can find it here: <a href="https://github.com/outlace/Data-Augmentation">https://github.com/outlace/Data-Augmentation</a>

As far as a roadmap for the next few months, I plan to complete the second
sub-series in my series on Topological Data Analysis (TDA). That is, I will roll out
a series of posts on the Mapper algorithm. Simultaneously I will be slowly working on
an open source TDA library in Python called <a href="https://github.com/outlace/OpenTDA">OpenTDA</a>.

After that, I want to get back into reinforcement learning as that's my biggest passion
in machine learning. I'm not exactly sure what I plan to work on yet, but will likely
use OpenAI's gym library as a testing ground. Feel free to drop a comment if you have any suggestions.

-Brandon
