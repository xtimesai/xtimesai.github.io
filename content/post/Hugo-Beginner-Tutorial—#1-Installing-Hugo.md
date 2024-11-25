---
title: "Hugo Beginner Tutorial—#1 Installing Hugo"
date: 2024-11-25T10:44:42-05:00
description : "Description goes here..."
tags: [""]
image : "assets/img/youtube_thumbnail.jpg.webp"
draft: false
---

{{< youtube SVvihs0WfhQ >}}

Introduction to Hugo Tutorial
Hey team, welcome to this introduction to Hugo tutorial. The goal of this series is to take you from a lion cub with basic web design knowledge to creating your first Hugo site. In this series, you'll learn how to set up a Hugo site, the basics of Hugo layouts, partials, and templating, set up a blog, and finally use data files. By the end of this series, you'll have the foundational knowledge to build your own Hugo site.
What is Hugo?
Hugo is a static site generator. It takes a directory of source files and runs a build process over them to generate a purely static website. What makes a Hugo site unique is its unparalleled build speeds and strict conventions around layouts, taxonomies, and content. It's a static site generator that powers high-profile websites such as Let's Encrypt, 1Password, the Lino documentation, and digital.gov.
Hugo is one of the simplest static site generators to install as it's distributed as a single binary—one of the many perks of a Go program. If you're using macOS or Linux, then Homebrew is the easiest way to install Hugo. Once you have Homebrew installed, you can run:
bash
brew install hugo

If you're on Windows, then Chocolatey package manager is the way to go. Once Chocolatey is installed, you can run:
bash
choco install hugo-extended --confirm

Let's triple check that all went to plan. In your terminal, check the Hugo version:
bash
hugo version

If that printed out a version number, you're good to go! If not, consult the Hugo documentation or reach out on the Hugo community forums.
Now we're going to set up our Hugo site. In your terminal, navigate to the directory where you want your Hugo project to live and run this command:
bash
hugo new site my-first-hugo-site

Hugo will set up the scaffolding for your site. Open your site up in your favorite code editor and poke through the contents. You'll see a number of directories that probably don't mean anything to you at this stage. I'll give a brief explanation of each one, but don't fret if you don't understand them right now; they'll become more familiar over the course of this series.
archetypes: Defines the default metadata (also known as front matter) for new content. You don't need to worry about archetypes for this series.
content: Your typically markdown content for pages lives here.
data: CSV, JSON, XML files that can be accessed like a read-only database.
layouts: The page templates for your content.
static: All your assets that don't need processing (often images, fonts, PDFs, etc.).
themes: Jumpstart your Hugo site with an existing theme (we won't be using themes in this series).
config.toml: The configuration for your soon-to-be flourishing Hugo site.
Stay tuned for the next lesson; we will learn the basics of Hugo layouts!