# Webxplus specifications

## HTML++ 

description: ''HTML++ The version of html that WebX uses. This is different from HTML5 and has less features.''

## Html++ Elements

### A

description :''An anchor or link in the site.''
example usage:
'''
<html>
  ...
  <body>
    <a href="buss://site.tld">Link</a>
    ...
  </body>
</html>
'''
content: ''Text''
Attributes: ''Class - classes it has, HREF - link to another website or page''

### Audio

description :''A audio player. Self-closing. Note: Unlike html, the controls are always shown.''
example usage:
'''
<html>
<html>
  ...
  <body>
    <audio src="<url>">
    ...
  </body>
</html>
'''
content: ''None''
Attributes: ''Class - classes it has, Src - the source of the audio, autoplay - play on website load''

### Body

description :''The body element of a page which contains the main content about the site.''
example usage:
'''
<html>
  ...
  <body>
    ...
  </body>
</html>
'''
Attributes: ''Class - classes it has''

### Button

description :''A button in the site.''
example usage:
'''
<html>
  ...
  <body>
    <button>Click me</button>
    ...
  </body>
</html>
'''
content: ''Text''
Attributes: ''Class - classes it has''

### Div

description :''A section of content in the site.''
example usage:
'''
<html>
  ...
  <body>
    <div>
      ...
    </div>
    ...
  </body>
</html>
'''
Attributes: ''Class - classes it has''

### H1-6

description :''A heading from level 1 to 6, where smaller the number the more important.''
example usage:
'''
<html>
  ...
  <body>
    <h1>Section heading</h1>
    <h2>Sub-heading</h2>
    ...
  </body>
</html>
'''
content: ''Text''
Attributes: ''Class - classes it has''

### HR

description :''A horizontal rule aka a horizontal line. Self-closing.''
example usage:
'''
<html>
  ...
  <body>
    <hr>
    ...
  </body>
</html>
'''
content: ''none''
Attributes: ''Class - classes it has''

### Head

description :''The head element of a page which contains metadata about the site.''
example usage:
'''
<html>
  <head>
    ...
  </head>
  ...
</html>
'''
Attributes: ''none''

### Html

description :''The main element of a page.''
example usage:
'''
<html>
    ...
</html>
'''
Attributes: ''Class - classes it has''

### Img

description :''A image in a site. Self-closing.''
example usage:
'''
<html>
  ...
  <body>
    <img src="<url>">
    ...
  </body>
</html>
'''
content: ''none''
Attributes: ''Class - classes it has, Src - the source of the image''

### Input

description :''A one line text input. Self-closing.''
example usage:
'''
<html>
  ...
  <body>
    <input>
    ...
  </body>
</html>
'''
content: ''none''
Attributes: ''Class - classes it has, Placeholder - placeholder text, Type - the type of input''

### Li

description :''A list item.''
example usage:
'''
<html>
  ...
  <body>
    <li>Item</li>
    ...
  </body>
</html>
'''
content: ''text''
Attributes: ''Class - classes it has''

### Link

description :''A url that points to the favicon / style sheets. Self-closing.''
example usage:
'''
<html>
  <head>
    ...
    <link href=".../favicon.png">
    <link href=".../style.css">
  </head>
  ...
</html>
'''
content: ''none''
Attributes: ''HREF - the url to link to''
HREF: ''The first link will be the favicon unless its a css file, the rest will just be trated as css.''

### Meta

description :''Metadata about the site. Self-closing.''
example usage:
'''
<html>
  <head>
    ...
    <meta name="description" content="My cool web">
    <meta name="theme-color" content="#000000">
  </head>
  ...
</html>
'''
content: ''none''
Attributes: ''Name - the name of the metadata to target, Content - the content to assign it''
Name: ''Currently the following names are supported/used: description - a description of the site, theme-color - a color to show for embeds, Other names can be used but will be ignored by most programs/browsers.''

### OL

description :''An ordered list.''
example usage:
'''
<html>
  ...
  <body>
    <ol>
      <li>Item</li>
    </ol>
    ...
  </body>
</html>
'''
Attributes: ''Class - classes it has''

### Option

description :''A option inside a select.''
example usage:
'''
<html>
  ...
  <body>
    <select>
      <option>A</option>
      <option>B</option>
      <option>C</option>
    <select>
    ...
  </body>
</html>
'''
Content: ''Text''
Attributes: ''Class - classes it has''

### P

description :''A paragraph in the site.''
example usage:
'''
<html>
  ...
  <body>
    <p>Some paragraph</p>
    ...
  </body>
</html>
'''
Content: ''Text''
Attributes: ''Class - classes it has''

### Script

description :''A script that will run lua code. Self-closing.''
example usage:
'''
<html>
  <head>
    ...
    <script src="script.lua" version="legacy">
  </head>
  <body>
    ...
    <script src="script.lua" version="2">
  </body>
</html>
'''
Content: ''none''
Attributes: ''Class - classes it has, Version - the lua version to use''
Version: ''Can be: legacy - for the legacy api, 2 - for the v2 api''

### Select

description :''A input that allows to select between several options.''
example usage:
'''
<html>
  ...
  <body>
    <select>
      <option>A</option>
      <option>B</option>
      <option>C</option>
    <select>
    ...
  </body>
</html>
'''
Attributes: ''Class - classes it has''

### Textarea

description :''A multi line text input. Self-closing.''
example usage:
'''
<html>
  ...
  <body>
    <textarea>
    ...
  </body>
</html>
'''
Content: ''none''
Attributes: ''Class - classes it has, Placeholder - placeholder text''

### Title

description :''The title of the website.''
example usage:
'''
<html>
  <head>
    <title>WebX Site</title>
    ...
  </head>
  ...
</html>
'''
Content: ''text''
Attributes: ''none''

### UL

description :''An unordered list.''
example usage:
'''
<html>
  ...
  <body>
    <ul>
      <li>Item</li>
    </ul>
    ...
  </body>
</html>
'''
Attributes: ''Class - classes it has''

## Lua

Description: 'The programming language of WebX.'
Versions: '
The lua api is separated in versions, currently Legacy and v2 are available.
These can be set like:
'''
<script src="..."> <!-- Defaults to legacy -->
<script api="legacy" src="...">
<script api="v2" src="...">
'''
If no version provided will default to legacy.
'

## Legacy API

Description: ''The original api version of webx made by Facedev.''
DEPRECATED: ''The legacy api is deprecated and no longer mantained.''

Globals: 
'''
fetch(options)
get(selector, all)
print(text)
window
'''
Tables: ''Element''

### Lua Legacy Element

description : ''A table representing actions that can be done to a html element.''
Contents:
'''
Functions:

get_contents() - get the text contents / value of a element
set_contents(text) - set the text contents / value of a element
get_content() - alias of get_contents()
set_content(text) - alias of set_contents()
get_href() - gets the href of a element
set_href(url) - sets the href of a element
get_source() - gets the src of a element
set_source(url) - sets the src of a element
get_opacity() - gets the opacity of a elment 0 to 1
set_opacity(opacity) - sets the opacity of a element 0 to 1
get_css_name() - get the class or tag of a element
set_value(value) - sets the value of a input
Events:

on_click => callback() - when the element is clicked
on_input => callback(value) - when text is written/changed in an input
on_submit => callback(value) - when a form is submited
'''

### Lua Legacy Fetch

Description: ''This global function fetches content from the web in a synchronous way.''
example usage:
'''
local res = fetch({
  url = "https://dns-one.webxplus.org/",
  method = "GET",
  headers = { ["Content-Type"] = "application/json" },
  body = "{ "test": "cat" }
})
'''
Inputs:
'''
Options
URL - if to get the first or all ocurrences
Method - if to get the first or all ocurrences
Headers - if to get the first or all ocurrences
Body - if to get the first or all ocurrences
'''
Return: ''String or Table (JSON/Object like structure) depending on the response of the fetch.''

### Lua Legacy Get

Description: This global function gets a element with the name or class passed to it.
example usage: ''get('links', true)''
Inputs: 
'''
Name - the name of the tag or class to get
All - if to get the first or all ocurrences
'''
Return:
'''
If all set to false: Element
If all set to true: array of Elements
'''

### Lua Legacy Print  

Description: ''This global function prints text passed to it.''
example usage: ''print('Hello')''
Inputs: ''Text - any text to print''
Return: ''No return.''

### Lua Legacy Window  

Description: ''This global table holds data about some things.''
example usage: ''window.browser''
Editable: 'yes'
Contents:
'''
browser - the name of the browser used
location - url of the website
query - query parameters
Query
The query is a table with key being the param name and value its value. Some important things:

Duplicate last overwrites others. ?cat=1&cat=2 then { cat: '2' }.
Case sensitive. ?Cat=1&cat=2 then { Cat: '1', cat: '2' }.
Multi = are not ignored. ?cat=1=2 then { cat: '1=2' }.
Spaces are not encoded. ?kitty cat=makes meow then { 'kitty cat': 'makes meow' }.
Trailing spaces are not trimmed. ? cat = 1 then { ' cat ': ' 1 ' }.
Blank keys or values are fine. ?cat=&=cat&dog then { cat: '', '': 'cat', dog: '' }.
Trailing ? & are ignored. ?cat& then { cat: '' } or ? then {}. But ?= then { '': '' }.
'''

### V2 API
Description: ''The new lua api that is more powerful easy to work with.''
Globals:
'''
browser
global
location
fetch(options)
get(selector, all)
getClass(class, all)
getId(id)
getTag(tag, all)
print(text)
printe(text)
printw(text)
'''
--ToBe Documented


### Lua Script Separation
Description:
'''
In webx multiple scripts don’t share things like variables, this may cause some issues for sharing values.
In the v2 api you can use the global table to share values between scripts.
'''

