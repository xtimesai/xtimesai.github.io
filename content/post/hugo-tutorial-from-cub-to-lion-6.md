---
title: "From Cub to Lion 6. Data Files"
date: 2024-11-20T12:41:03-05:00
description : "Hugo Beginner Tutorial — #3 Hugo Partials"
tags: [""]
image : "img/from-cub-3.jpg"
draft: false
---

{{< youtube EGwLmE7hfSE >}}

## Hugo Beginner Tutorial — #3 Hugo Partials

### Introduction to Partials

(00:06)
The idea behind a partial is simple:

It’s a file that can be included into a layout to reduce repetition or hide complexity.
Instead of duplicating code or creating overly large layout files, you can split logic into smaller, reusable components.
In this tutorial, you’ll learn how to add a navigation bar to your site using a partial. While it’s possible to add this logic directly to baseof.html, using partials keeps your layouts more modular and manageable.

### Step 1: Creating a Partial for the Navigation Bar

(00:43)

Create a Partials Directory:
Navigate to the layouts directory in your Hugo project.
Create a new folder called partials.
Create a Partial File:
Inside the partials directory, create a file named nav.html.
Add Navigation Structure:
In nav.html, define a very basic navigation structure:
<nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
    <!-- Add more links as needed -->
  </ul>
</nav>
Now your navigation is set up and ready to be included in your layouts.

### Step 2: Including the Navigation Partial in Your Layout

(01:11)

Open the Base Layout:
Open baseof.html (the parent layout for your site).
Include the Partial:
Add the following code below the <body> tag to include the navigation partial:
{{ partial "nav.html" }}
Important Note:
In Go templates (which Hugo uses), double quotes (") are required for strings. Single quotes (') will not work.
Render the Page:
After rendering the page, you should see your simple navigation bar included.

### Step 3: Simplifying baseof.html Further with Another Partial

(01:40)
Now, let’s simplify baseof.html even further by moving the <head> section into a partial.

Create a Partial for Meta Data:
Create a new partial file in the partials directory called meta.html.
Move the <head> Content:
Cut all the contents of the <head> section from baseof.html and paste them into meta.html.
For example:
<head>
  <title>{{ .Page.Title }}</title>
  <meta name="description" content="{{ .Page.Description }}">
  <!-- Add more meta tags as needed -->
</head>
Handling Variables in the Partial:
Some variables in meta.html, such as .Page.Title, require the context of the current page.
To pass the current page context, you can use a single character—a dot (.).
Include the Partial in baseof.html:
Replace the <head> section in baseof.html with the following code:
{{ partial "meta.html" . }}

### Why the Dot (.) is Important

(02:10)
The dot (.) represents the context of the current page. When you pass it to a partial, it ensures the partial has access to the same variables and data as the layout that includes it.

You’ll see this syntax frequently in Hugo templates, as it’s essential for passing data to partials and other templates.

### Next Steps

In the next lesson, you’ll dive deeper into the basics of Hugo templating. You’ll learn how to:

- Manipulate data.
- Iterate over data to create dynamic pages.
