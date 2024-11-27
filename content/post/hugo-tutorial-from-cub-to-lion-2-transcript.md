---
title: "Hugo Beginner Tutorial: Understanding and Using Layouts"
date: 2024-11-26
description : "Description goes here..."
tags: [""]
image : "img/from-cub-2.jpg"
draft: false
---

## Introduction

Making good use of layouts is essential to creating an easy-to-maintain, flexible, and thriving Hugo website. Let’s see what makes them tick.

### What is a Layout?

A layout is used for all the framing on the page around the content. Think of the elements that remain relatively the same across pages—for example, the header and footer. These typically live in a layout.

In Hugo, each page on the site is a content file. At the top of a content file, there’s a snippet of metadata called **front matter**, followed by Markdown. The goal of a content file is to store content in its purest form. There’s rarely any HTML or other presentation logic in a content file. All the fancy HTML to display and format the content lives in the layout.

### Reusing Layouts Across Pages

One layout might be used for multiple content files. For example, on a portfolio website, you might use the same layout for your **About** page and your **Services** page.

Sometimes, particularly if you’re doing something intricate, you might have a layout specifically for an individual content page.

### Hugo Page Bundles and Layout Types

There’s a Hugo concept called **page bundles**, which can be tricky to grasp. Here’s the bare minimum to get your site going:

- By default, content pages use a layout called **single**.
- Creating a content file named `_index.md` is an exception. These files act like a table of contents for pages around them and use a layout called **list** by default.

#### Example: Home Page Table of Contents

Just like a good non-fiction book, it’s good practice to start off with a table of contents. You’ll do this for the home page of your site:

1. Create a file called `_index.md` in the `content` directory.
2. Inside, paste some content. The triple dashed lines indicate the metadata (**front matter**) mentioned earlier, followed by Markdown content.

### Hugo Layout Hierarchy

Hugo uses a hierarchy to determine which layout to use for a content file. If it can’t find a specific layout, it falls back to the **default** directory.

#### Example: Creating a Default Layout

1. Go to `layouts` and create a directory called `_default`.
2. Inside `_default`, create a file called `list.html`.
3. Paste in some content. This will be a basic HTML page.

The unfamiliar part might be the curly braces (`{{ }}`), which are used to render content from the content file. For instance, content comes from the `_index.md` file we created earlier. This uses Hugo templating, which we’ll explore in a later lesson.

### Running Your Hugo Site Locally

After setting up your first page, it’s time to test it. Hugo has a command called `serve` that builds your site and serves it locally at `localhost:1313` by default.

1. Run `hugo serve` in the root of your site.
2. Open your browser and navigate to `localhost:1313`. Your content will render through a layout on your Hugo site!

### Adding an About Page

To create a second page for your site, such as an **About** page:

1. Go to the `content` directory and create a new file called `about.md`. (Note: There’s no underscore here; that’s only for the table of contents page.)
2. Add content to `about.md` in a structure similar to the index page: **Front matter** at the top and Markdown content below.

Since this isn’t a table of contents page, it will use the **single** layout by default.

### Reusing Layouts with Base Layouts

Instead of maintaining two very similar layouts (e.g., **list** and **single**), you can reduce repetition by creating a **base layout**.

#### Example: Creating a Base Layout

1. Create a new layout in `_default` called `baseof.html`.
2. Paste in the base HTML structure. This is almost identical to the current list layout, except for one key difference:
   - Replace the content area with a block: `{{ block "main" . }}{{ end }}`. This block acts as a placeholder for other layouts to specify just that part of the page.

#### Updating List and Single Layouts

1. Update the list layout: Replace the HTML structure with the block defined earlier.
2. Output the content inside the block.
3. Create a new `single.html` layout and define the main block there as well.

Navigate to `localhost:1313/about` to see your new About page.

### Adding Styles with SCSS

Hugo doesn’t include CSS by default, but you can add styles to improve the site’s appearance. Using a **SASS stylesheet** makes maintenance easier as the site grows.

#### Setting Up SCSS

1. Go to the `static` directory (where static assets like plain CSS files live).
2. Create a new directory in the root called `assets`. Inside, create a folder called `scss` for `.scss` files.

#### Adding a Main SCSS File

1. Create a file called `main.scss` and add some content to it.
2. Reference the stylesheet in the base layout (`baseof.html`) by adding a `<link>` tag in the `<head>` section to include the SASS file. The stylesheet will now apply to both the list and single layouts.

If the styles don’t apply immediately, restart the Hugo server:

- Press `Ctrl + C` to stop it.
- Run `hugo serve` again.

### Next Steps

Currently, the only way to access the About page is by navigating to it directly. In the next lesson, we’ll add site navigation using a Hugo partial.
