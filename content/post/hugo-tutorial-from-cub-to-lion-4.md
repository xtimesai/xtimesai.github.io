---
title: "From Cub to Lion 4. Templating"
date: 2024-11-22T10:44:42-05:00
description : "In this series, you'll learn how to set up a Hugo site, the basics of Hugo layouts, partials, and templating, set up a blog, and finally use data files."
tags: [""]
image : "img/from-cub-1.jpg"
draft: false
---

{{< youtube SVvihs0WfhQ >}}


With Hugo templating, you can control how your page is rendered. You can use variables, loop over arrays, check conditions, and run functions. Think of it as a simple programming language to help build the pages on your site. Those curly braces in your layout? That's Hugo templating.

## What is Front Matter?

Front matter is a snippet of metadata at the top of content files. Some metadata is specifically for Hugo, such as setting a layout or indicating that the current page is a draft. Other forms of metadata will be specific to your site, like indicating which type of hero to use on the page or listing your five favorite foods. Front matter comes in the form of a YAML snippet at the top of content files, and we've seen this in both the index and about pages. It may not seem like much, but we can reference the front matter using Hugo templating.

## Understanding Hugo Templating

Hugo uses Go templating as its templating language for layouts. It's easy once you get your head around it. As with many things in Hugo, sometimes it's easier to show rather than tell. You can write normal HTML in your layouts and use curly braces to execute code inside them. For example, outputting "Hello" will render "Hello" rather than showing the curly braces and double quotes.

You can reference variables from front matter in a layout. For instance, outputting the title from two pages in a layout is done with `.Params.VariableName`, like `.Params.Title`. You might want to set a variable globally in your `config.toml` file; for example, setting a title as part of the scaffolding allows access using `.Site.Title`.

## Using Conditions and Variables

You can set conditions to check if a title is set in params; if it is, output the params title; otherwise, output the site title. Variables can be set with the dollar sign. Here we're setting 'Gazelle' as our favorite food and then outputting it.

## Iterating Over Arrays

You can iterate over arrays by initializing an array of best friends and using `range` to iterate over them. The context of each iteration is set to `.` so outputting `.` in the first iteration will output "Pumba," then "Timon," etc.

## Nested Keys and Context Management

You can iterate over nested keys using `with`. For example, if you have an appearance with eyes, snoots, whiskers, and limbs (where limbs is an array), you can output that structure in your layout more easily using `with`. Without `with`, you'd need to reference it fully each time like `.Params.Appearance.Eyes`. Using `with` simplifies it to `.Eyes`.

## Practical Application

Let's put our new Hugo templating knowledge into action by adding a footer to the website that includes your name and current year. Additionally, we'll add an optional front meta field you can use to hide the footer on a particular page.

Start by editing your `config.toml` file to add your name under a params object. Then create a partial named `footer.html` in partials. In this partial, check if `params.hideFooter` exists; if it does, output no footer; otherwise, output a footer with "Website made by Site.Params.Name" and the current year.

Finally, add this partial just before the closing body tag in your base template. Pass up the current page's context for this params hide footer check.

To verify that the front matter hide footer field works, go to your about page and add `hideFooter: true`. The homepage will display the footer while the about page will not.

Next up, we'll explore creating a blog in Hugo and put our new Hugo templating knowledge to the test.
