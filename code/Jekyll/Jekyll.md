# Jekyll

<!-- TOC -->

- [Jekyll](#jekyll)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Starting a website](#starting-a-website)
  - [Running the Website](#running-the-website)
  - [Configuration file](#configuration-file)
  - [Front Matter](#front-matter)
  - [Creating blog posts](#creating-blog-posts)
  - [Working with Drafts.](#working-with-drafts)
  - [Creating Pages](#creating-pages)
  - [Permalinks](#permalinks)
  - [Front matter defaults](#front-matter-defaults)
  - [Installing Themes](#installing-themes)

<!-- /TOC -->

## Introduction

Jekyll is a static site generator software made using Ruby. It is useful for creating a static website. It will take care of all the HTML. Write the content in a text file and it will automatically convert into HTML file. Also, there is a provision for including CSS files to make your own website design.

## Installation

You need to install:

* Ruby Compiler
* Ruby Gems [Package Manager]

In Ubuntu, install Ruby and Jekyll using the commands:

```bash
sudo apt install ruby
sudo gem install jekyll bundler
```

To check if the components are installed, type the following commands and see if a similar output pops-up.

```bash
arun@hpdv6:~$ ruby -v
ruby 2.5.1p57 (2018-03-29 revision 63029) [x86_64-linux-gnu]
arun@hpdv6:~$ gem -v
2.7.6
arun@hpdv6:~$ jekyll -v
jekyll 3.8.5
arun@hpdv6:~$ bundler -v
Bundler version 2.0.1
```

## Starting a website

To create a website, type the command ``jekyll new <foldername>`` as follows:

```bash
jekyll new fluidiccolours
```

Once it is done, a directory called ``fluidiccolours`` is created with a lot of files in it.

```bash
arun@hpdv6:~/Website_Experimental/jekyll_minimal_experiment$ tree
.
└── fluidiccolours
    ├── 404.html
    ├── about.md
    ├── _config.yml
    ├── Gemfile
    ├── index.md
    └── _posts
        └── 2019-06-11-welcome-to-jekyll.markdown

2 directories, 6 files
```

* ``index.md`` is the home page of the website.
* ``about.md`` is the about page of the website.
* ``Gemfile`` is the bundle configuration file for the project. Do not edit it unless you want to go and tweak a lot of fundamental settings. It contains all the packages and the dependencies that are necessary for the ruby project to work.
* ``_posts`` folder has all the blog posts in markdown that will be converted into HTML files.
* ``_site`` folder will have all the HTML files of your website - essentially the final version of your website. It gets updated as and when the web pages are modified.
* ``_config.yaml`` file contains the configuration values for the files as a list of key-value pairs.

## Running the Website

To run the website, go into the website folder and type this command in the terminal.

```bash
arun@hpdv6:~/Website_Experimental/jekyll_minimal_experiment/fluidiccolours$ bundle exec jekyll serve
Configuration file: /home/arun/Website_Experimental/jekyll_minimal_experiment/fluidiccolours/_config.yml
            Source: /home/arun/Website_Experimental/jekyll_minimal_experiment/fluidiccolours
       Destination: /home/arun/Website_Experimental/jekyll_minimal_experiment/fluidiccolours/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
       Jekyll Feed: Generating feed for posts
                    done in 0.8 seconds.
 Auto-regeneration: enabled for '/home/arun/Website_Experimental/jekyll_minimal_experiment/fluidiccolours'
    Server address: http://127.0.0.1:4000/
  Server running... press ctrl-c to stop.
[2019-06-11 01:35:49] ERROR `/favicon.ico' not found.
```

The website should be accessible from the local server ``http://127.0.0.1:4000/``

## Configuration file

``_config.yml`` is the configuration file for the project. It contains all the important attributes for the website as a key-value pair list.

The default configuration file will be like this:

```yaml
# Welcome to Jekyll!
#
# This config file is meant for settings that affect your whole blog, values
# which you are expected to set up once and rarely edit after that. If you find
# yourself editing this file very often, consider using Jekyll's data files
# feature for the data you need to update frequently.
#
# For technical reasons, this file is *NOT* reloaded automatically when you use
# 'bundle exec jekyll serve'. If you change this file, please restart the server process.

# Site settings
# These are used to personalize your new site. If you look in the HTML files,
# you will see them accessed via {{ site.title }}, {{ site.email }}, and so on.
# You can create any custom variable you would like, and they will be accessible
# in the templates via {{ site.myvariable }}.
title: Your awesome title
email: your-email@example.com
description: >- # this means to ignore newlines until "baseurl:"
  Write an awesome description for your new site here. You can edit this
  line in _config.yml. It will appear in your document head meta (for
  Google search results) and in your feed.xml site description.
baseurl: "" # the subpath of your site, e.g. /blog
url: "" # the base hostname & protocol for your site, e.g. http://example.com
twitter_username: jekyllrb
github_username:  jekyll

# Build settings
markdown: kramdown
theme: minima
plugins:
  - jekyll-feed

# Exclude from processing.
# The following items will not be processed, by default. Create a custom list
# to override the default setting.
# exclude:
#   - Gemfile
#   - Gemfile.lock
#   - node_modules
#   - vendor/bundle/
#   - vendor/cache/
#   - vendor/gems/
#   - vendor/ruby/
```

You can go and tweak the values as per your convenience.

## Front Matter

If you open the default sample blog jekyll created for you, the header of the file will look like this:

```yaml
---
layout: post
title:  "Welcome to Jekyll!"
date:   2019-06-11 01:26:32 +0530
categories: jekyll update
author: "Arun Prasaad Gunasekaran"
permalink: /sample/
---
```

This is the front matter for the blog post. A similar front matter exists for other web pages. It is the information of the webpage. Front matter is written using ``YAML`` or ``JSON``. The content is written in ``YAML`` by default.

* ``layout`` is used to set the type of the webpage.
* ``title`` is the title of the webpage.
* ``date`` is the date and time of the webpage.
* ``categories`` has a set of keywords associated with the webpage. It is also used for maintaining the folder structure.
* ``author`` is the name of the author of the webpage.
* ``permalink`` is the permanent link for the webpage.

All the values given here are the ``variables`` for the webpage.

## Creating blog posts

Inside the ``_posts`` directory, create a markdown file with a similar front matter and type all your contents. For blogs, you need the ``post`` layout idea.

You can create as many posts as you like in whichever order you fancy within the ``_posts`` directory. And that includes creating sub-folders within ``_posts`` folder and placing the blogs inside them. As long as the linking method is fixed, the address of the webpages is taken care of.

## Working with Drafts.

If you have draft pages, write them in the ``_drafts`` folder in the same level as that of ``_posts`` folder. Inside it, write all the draft versions of the blog posts. Jekyll does not post the draft pages. Only when it is moved to ``_posts`` folder will it work.

To see the draft webpost served, use the command

```bash
jekyll serve --draft
```

Jekyll will automatically create a link based on the date the draft was last modified to display the draft file.

## Creating Pages

There are two kinds of pages:

* General pages like “About” page
* Blog pages

Other important webpages like “About” or “Contact” are called “Pages”.

To create them, write a normal markdown file with a front-matter like this:

```yaml
---
layout: page
title: FAQ
permalink: /faq/
---

This is a sample FAQ page!
```

## Permalinks

Permalinks are permanent links for the webpages. By modifying the variable in the permalink section, you can give permanent links to each page.

```yaml
permalink: /:categories/:year/:month/:day/:title
```

This will create a weblink with categories followed by the year, month, day, and title.

## Front matter defaults

These are settings that are default to a certain kinds of webpages.

To set custom front-matter, you can use the default values in the ``_config.yaml`` file.

```yaml
defaults:
  scope:
    path: ""
  values:
  	layout: "post"
```

This setting will automatically make any page without any layout value a blog post by default.

Whenever a ``yaml`` file is modified, shut the server and restart it to have the details reflected.

```yaml
defaults:
  scope:
    path: ""
      type: "posts"
    values:
      layout: "post"
      title: "My Title"
```

This setting will take any page inside the post folder without any details and assign a “post” layout and a default “title”.

## Installing Themes

