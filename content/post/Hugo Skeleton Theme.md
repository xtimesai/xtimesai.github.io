---
title: "Hugo Skeleton Theme"
date: 2024-11-19T10:07:12-05:00
draft: false
tags: ["markdown", "tutorial", "hugo", "blog"]
image: "img/rainbow.jpeg"
Description: "Welcome back to the channel.
We're going to be looking at a new cool feature, which is the Hugo skeleton theme.
It helps you get started with Hugo a little bit faster, and it's also great for testing."
featured: true
---

welcome back to the channel 
we're going to be looking at a new cool feature which is the Hugo skeleton theme 
it helps you get started with Hugo a little bit faster 
and it's also great for testing 
for this video you need to have the latest version of Hugo installed and visual studio code set up 
I've got a video on how to install Hugo along with everything else you'll need that links above 
on completing this video you'll be able to create a skeleton project which doesn't have a theme in it 
add a skeleton theme to that project 
and also create the same setup but without a theme directory 
so open up Powershell in a directory where i' would like to create the project 
I use the command Hugo new site 
and then I put the name in 
so we'll call it skeleton and it's been created 
however we haven't got a theme in it 
but we'll have a look at it first so
so if we right click and choose open with code 
have a look 
all the folders are created for us 
we've got a hug hugo. tomal file 
but we don't have any themes layouts uh content and that's where the theme comes in handy 
we can now open up a new terminal 
we'll run Hugo new theme we'll just call it my theme
and we have a look in there you'll notice we've got some content and some layouts uh it's all been set up for us we going to go into our hugo. tml file and explain um that's the thing we want to use so we'll type in the key of theme and we'll use my theme so we'll save that and we can run Hugo server
and control click and then we've got uh the site setup the skeleton theme there isn't a whole lot to it it is super basic if we have a look at the b. HTML you'll see we've got the Bare Bones in there and we've got a our head set up with CSS JS the basic
are ready to go it's been noted by the Hugo developers that they've deliberately left out intermediate and advanced features and this is just for really simple testing if You' like to set this up with more advanced features that's something you have to do yourself so now I have look at doing the exact same thing but without using a theme directory so this time we'll run Hugo new theme
and we'll call it skeleton no theme di for example and specify the theme directory as the base of the project run that it's then merged the two together and I'll put those in the description for you then open it up in Visual Studio code
have a look in the layouts folder and you'll see it's all been merged into the one project we're not worrying about that themes directory anymore we can go to the terminal we can run Hugo server and control click we're ready to go you can start developing Hugo site from there or you can run some simple tests so that's it for the video remember to hit that like button hit subscribe
and the bell notification I'm always releasing new videos every week on Hugo and other modern web Technologies and you'll find a heap of other videos on my YouTube channel as well as you'll find me on skillshare it's all in the description see you next week


Intro

welcome back to the channel 
we're going to be looking at a new cool feature
which is the Hugo skeleton theme 
it helps you get started with Hugo 
a little bit faster 
and it's also great for
testing for this video you need to have
 Requirements
the latest version of Hugo installed and
visual studio code set up I've got a
video on how to install Hugo along with
everything else you'll need that links
above on completing this video you'll be
able to create a skeleton project which
doesn't have a theme in it add a
skeleton theme to that project and also
create the same setup but without a
theme
 Creating the project
directory so open up Powershell in a
directory where i' would like to create
the project I use the command Hugo
new site and then I put the name in so
we'll call it
skeleton and it's been created however
we haven't got a theme in it but we'll
have a look at it first so so if we
right click and choose open with
code have a look all the folders are
created for us we've got a hug hugo.
tomal file but we don't have any themes
layouts uh content and that's where the
theme comes in
 Setting up the theme
handy we can now open up a new
terminal we'll run
Hugo new theme we'll just call it my
theme
and we have a look in there you'll
notice we've got some content and some
layouts uh it's all been set up for us
we going to go into our hugo. tml file
and
explain um that's the thing we want to
use so we'll type in the key of
theme and we'll use my
theme so we'll save that and we can run
Hugo server
and control
click and then we've got uh the site
setup the skeleton theme there isn't a
whole lot to it it is super basic if we
have a look at
the b. HTML you'll see we've got the
Bare Bones in
there and we've got a our head set up
with CSS
JS the basic are ready to
go it's been noted by the Hugo
developers that they've deliberately
left out intermediate and advanced
features and this is just for really
simple testing if You' like to set this
up with more advanced features that's
something you have to do
yourself so now I have look at doing the
exact same thing but without using a
theme
directory so this time we'll
run
Hugo
[Music]
new theme and we'll call
it
skeleton no theme di for
example and specify the theme
directory as the base of the
project run that it's then merged the
two
together and I'll put those in the
description for
you then open it up in Visual Studio
code
have a look in the layouts folder and
you'll see it's all been merged into the
one project we're not worrying about
that themes directory anymore we can go
to the terminal we can run Hugo
server and control
click we're ready to go you can start
developing Hugo site from there or you
can run some simple
 Outro
tests so that's it for the video
remember to hit that like button hit
subscribe and the bell notification I'm
always releasing new videos every week
on Hugo and other modern web
Technologies and you'll find a heap of
other videos on my YouTube channel as
well as you'll find me on skillshare
it's all in the description see you next
week


Commands used:

hugo new site skeletonSite
when in this site:  hugo new theme newTheme

combine the two

hugo new theme skeletonNoThemeDir --themesDir .


--------------
Intro

Welcome back to the channel.
We're going to be looking at a new cool feature, which is the Hugo skeleton theme.
It helps you get started with Hugo a little bit faster, and it's also great for testing.
For this video, you need to have the latest version of Hugo installed and Visual Studio Code set up.
I've got a video on how to install Hugo along with everything else you'll need; that links above.
On completing this video, you'll be able to create a skeleton project which doesn't have a theme in it, add a skeleton theme to that project, and also create the same setup but without a theme.
Creating the Project

Open up PowerShell in a directory where you'd like to create the project.
I use the command hugo new site and then put the name in, so we'll call it skeleton.
It's been created; however, we haven't got a theme in it.
But we'll have a look at it first.
If we right-click and choose "Open with Code", have a look, all the folders are created for us.
We've got a hugo.toml file, but we don't have any themes, layouts, or content, and that's where the theme comes in.
Setting up the Theme

We can now open up a new terminal.
We'll run hugo new theme and just call it "mytheme."
When we look in there, you'll notice we've got some content and some layouts; it's all been set up for us.
We're going to go into our hugo.toml file and explain that's the theme we want to use.
So we'll type in the key of theme and use mytheme.
We'll save that, and we can run hugo server and control-click.
Then we've got the site set up.
The skeleton theme is super basic.
If we look at the b.HTML, you'll see we've got the bare bones in there.
We've got our head set up with CSS and JS, and the basics are ready to go.
It's been noted by the Hugo developers that they've deliberately left out intermediate and advanced features, and this is just for really simple testing.
If you'd like to set this up with more advanced features, that's something you have to do yourself.
Now, let's look at doing the exact same thing but without using a theme directory.
This time, we'll run hugo new theme and we'll call it "skeleton-no-theme" for example, and specify the theme directory as the base of the project.
Run that, it's then merged the two together, and I'll put those in the description for you.
Then open it up in Visual Studio Code.
Have a look in the layouts folder, and you'll see it's all been merged into one project.
We're not worrying about that themes directory anymore.
We can go to the terminal, we can run hugo server and control-click.
We're ready to go.
You can start developing your Hugo site from there, or you can run some simple tests.
Outro

So that's it for the video.
Remember to hit that like button, hit subscribe, and the bell notification.
I'm always releasing new videos every week on Hugo and other modern web technologies.
You'll find a heap of other videos on my YouTube channel, as well as on Skillshare.
It's all in the description.
See you next week!

