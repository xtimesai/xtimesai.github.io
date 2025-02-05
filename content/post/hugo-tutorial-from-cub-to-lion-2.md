---
title: "From Cub to Lion 2. Layouts"
date: 2024-11-24T12:41:03-05:00
description : "Description goes here..."
tags: [""]
image : "img/from-cub-2.jpg"
draft: false
---

{{< youtube xRwZmWItIBA >}}

## Hugo Beginner Tutorial — #2 Hugo Layouts

Introduction

(00:06)
Making good use of layouts is essential to creating an easy-to-maintain, flexible, and thriving Hugo website. So, let's see what makes them tick.

What is a Layout?
A layout is used for all the framing on the page around the content. Think of the elements that remain relatively the same across pages—for example, the header and footer. These are the parts that usually live in a layout.

In Hugo, each page on the site is a content file. At the top of a content file, there's a small snippet of metadata called front matter, followed by Markdown. The goal of a content file is to store content in its purest form. There’s rarely any HTML or other presentation logic in a content file. All the fancy HTML to display and format the content lives in the layout.

Reusing Layouts Across Pages

(00:38)
One layout might be used for multiple content files. For example, on a portfolio website, you might use the same layout for your About page and your Services page.

Other times, particularly if you're doing something intricate, you might have a layout specifically for an individual content page.

Hugo Page Bundles and Layout Types

(01:14)
There’s a Hugo concept called page bundles, which can be tricky to grasp. We’ll stick to the bare minimum here to get your site going.

By default, content pages use a layout called single. However, creating a content file named _index.md is an exception. These files act like a table of contents for pages around them and use a layout called list by default.

Example: Home Page Table of Contents
Just like a good non-fiction book, it's good practice to start off with a table of contents. You’ll do this for the home page of your site.

Create a file called _index.md in the content directory.
Inside, paste some content.
The triple dashed lines indicate the metadata (front matter) mentioned earlier, followed by Markdown content.
Hugo Layout Hierarchy

(02:40)
Hugo uses a hierarchy to figure out which layout to use for a content file. If it can’t find a specific layout, it falls back to the default directory.

Example: Creating a Default Layout
Let’s create a default list layout for your home page:

Go to layouts and create a directory called _default.
Inside _default, create a file called list.html.
Paste in some content.
This will be a basic HTML page. The unfamiliar part might be the curly braces ({{ }}), which are used to render content from the content file. In this case, the content comes from the _index.md file we created earlier. This uses Hugo templating, which we’ll explore in a later lesson.

Running Your Hugo Site Locally

(03:20)
Now that you’ve set up your first page, it’s time to test it. Hugo has a command called serve that builds your site and serves it locally at localhost:1313 by default.

Run hugo serve in the root of your site.
Open your browser and navigate to the address localhost:1313.
Look—your content is rendering through a layout on your Hugo site!

Adding an About Page

(03:58)
Let’s create a second page for your site: an About page.

Go to the content directory and create a new file called about.md.
Note: There's no underscore here; that’s only for the table of contents page.
Add content to about.md in a structure similar to the index page:
Front matter at the top, setting the title.
Markdown content below.
Since this isn’t a table of contents page, it will use the single layout by default.

Reusing Layouts with Base Layouts

(04:35)
Instead of maintaining two very similar layouts (list and single), we can reduce repetition by creating a base layout.

Example: Creating a Base Layout
Create a new layout in _default called baseof.html.
Paste in the base HTML structure.
This is almost identical to the current list layout, except for one key difference:

Replace the content area with a block:
{{ block "main" . }}{{ end }}
This block acts as a placeholder for other layouts to specify just that part of the page.
Updating list and single Layouts
Update the list layout:
Replace the HTML structure with the block defined earlier.
Output the content inside the block.
Create a new single.html layout and define the main block there as well.
If you navigate to localhost:1313/about, you’ll see your new About page.

Adding Styles with SCSS

(05:45)
Hugo doesn’t include CSS by default, but we can add styles to improve the appearance. We’ll use a SASS stylesheet for easy maintenance as the site grows.

Setting Up SCSS
Go to the static directory (this is where static assets like plain CSS files live).
Create a new directory in the root called assets.
Inside assets, create a folder called scss for .scss files.
Adding a Main SCSS File
Create a file called main.scss and add some content to it.
Reference the stylesheet in the base layout (baseof.html):
Add a <link> tag in the <head> section to include the SASS file.
Now the stylesheet will apply to both the list and single layouts.

Restarting the Hugo Server
If the styles don’t apply immediately, restart the Hugo server:

Press Ctrl + C to stop it.
Run hugo serve again.
Next Steps

(07:47)
Currently, the only way to access the About page is by navigating to it directly. In the next lesson, we’ll add site navigation using a Hugo partial.

