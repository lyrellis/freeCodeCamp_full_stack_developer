# HTML Notes

> Notes from the HTML curriculum within the freeCodeCamp Full Stack Developer curriculum

The source material can be found here:

<https://www.freecodecamp.org/learn/full-stack-developer>

## Table of Contents

1. [HTML Basics](#html-basics)
    1. [Void Elements](#void-elements)
    2. [Attributes](#attributes)
    3. [Comments](#comments)
    4. [Common HTML Elements](#common-html-elements)
        1. Heading Elements
        2. Paragraph Elements
        3. `img` Elements
        4. `body` Element
        5. `div` Elements
        6. Anchor Elements
        7. Unordered and Ordered List Elements
        8. Emphasis Element
        9. Strong Importance Element
        10. `figure` and `figcaption` Elements
        11. `main` Element
        12. `footer` Element
    5. [Identifiers and Grouping](#identifiers-and-grouping)
        1. IDs
        2. Classes
    6. [Special Characters and Linking](#special-characters-and-linking)
        1. HTML Entities
        2. `link` Element
        3. `script` Element
    7. [Boilerplate and Encoding](#boilerplate-and-encoding)
        1. HTML Boilerplate
        2. `DOCTYPE`
        3. `html` Element
        4. `head` Element
        5. `meta` Element
        6. `title` Element
    8. [SEO and Social Sharing](#seo-and-social-sharing)
        1. SEO
        2. Meta (`desription`) Element
        3. Open Graph Tags
            1. `og:title` Property
            2. `og:type` Property
            3. `og:image` Property
            4. `og:url` Property
    9. [Media Elements and Optimization](#media-elements-and-optimization)
        1. Replaced Elements
        2. Optimizing Media
            1. Image Formats
            2. Image Licenses
            3. SVGs
        3. Multimedia Integration
            1. `audio` and `video` Elements
            2. `loop` Attribute
            3. `muted` Attribute
            4. `source` Attribute
            5. `poster` Attribute
    10. [Target Attribute Types](#target-attribute-types)
        1. Target Attribute
            1. `_self` Value
            2. `_blank` Value
            3. `_parent` Value
            4. `_top` Value
    11. [Absolute vs. Relative Paths](#absolute-vs-relative-paths)
        1. Path Definition
        2. Path Syntax
        3. Absolute Path
        4. Relative Path
    12. [Link States](#link-states)
        1. `:link`
        2. `:visited`
        3. `:hover`
        4. `:focus`
        5. `:active`
2. [Semantic HTML](#semantic-html)
    1. [Importance of Semantic HTML](#importance-of-semantic-html)
    2. [Presentational HTML Elements](#presentational-html-elements)
        1. `font` Element
        2. `center` Element
        3. `big` Element
    3. [Semantic HTML Elements](#semantic-html-elements)
        1. Header Element
        2. Main Element
        3. Section Element
        4. Navigation Section Element
        5. Figure Element
        6. Emphasis Element
        7. Idiomatic Text Element
        8. Strong Importance Element
        9. Bring Attention To Element
        10. Description List Element
            1. Description Term Element
            2. Description Details Element
        11. Block Quotation Element
        12. Citation Element
        13. Inline Quotation Element
        14. Abbreviation Element
        15. Contact Address Element
        16. Date and Time Element
            1. ISO 8601 Date Attribute
        17. Superscript Element
        18. Subscript Element
        19. Inline Code Element
        20. Preformatted Text Element
        21. Unarticulated Annotation Element
        22. Ruby Annotation Element
            1. Ruby Fallback Parenthesis Element
            2. Ruby Text Element
        23. Strikethrough Element
3. [Forms and Tables](#forms-and-tables)
    1. [HTML Form Elements and Attributes](#html-form-elements-and-attributes)
    2. [HTML Table Elements and Attributes](#html-table-elements-and-attributes)
    3. [Working with HTML Tools](#working-with-html-tools)
4. [Accessibility](#accessibility)
5. [References](#references)

## HTML Basics

Role of HTML:

- HTML represents the content and structure of the web page.

HTML Elements:

- Elements are the building blocks for an HTML document. They represent headings, paragraphs, links, images and more. Most HTML elements consist of an opening tag (`<elementName>`) and a closing tag (`</elementName>`).

Here is the basic syntax:

```html
<elementName>Content goes here</elementName>
```

### Void Elements

Void elements cannot have any content and only have a start tag. Examples include img and meta elements.

```html
<img>
<meta>
```

It is common to see some codebases that include a forward slash `/` inside the void element. Both of these are acceptable:

```html
<img>
<img/>
```

### Attributes

An attribute is a value placed inside the opening tag of an HTML element. Attributes provide additional information about the element or specify how the element should behave. Here is the basic syntax for an attribute:

```html
<element attribute="value"></element>
```

A boolean attribute is an attribute that can either be present or absent in an HTML tag. If present, the value is true otherwise it is false. Examples of boolean attributes include `disabled`, `readonly`, and `required`.

### Comments

Comments are used in programming to leave notes for yourself and other developers in your code. Here is the syntax for a comment in HTML:

```html
<!--This is an HTML comment.-->
```

---

[Back to top](#table-of-contents)

---

### Common HTML elements

#### Heading Elements

There are six heading elements in HTML. The `h1` through h6 heading elements are used to signify the importance of content below them. The lower the number, the higher the importance, so `h2` elements have less importance than `h1` elements.

```html
<h1>most important heading element</h1>
<h2>second most important heading element</h2>
<h3>third most important heading element</h3>
<h4>fourth most important heading element</h4>
<h5>fifth most important heading element</h5>
<h6>least important heading element</h6>
```

#### Paragraph Elements

This is used for paragraphs on a web page.

```html
<p>This is a paragraph element.</p>
```

#### `img` Elements

The `img` element is used to add images to the web page. The `src` attribute is used to specify the location for that image. For image elements, it's good practice to include another attribute called the `alt` attribute. Here's an example of an `img` element with the `src` and `alt` attributes:

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="A slice of lasagna on a plate.">
```

#### `body` Element

This element is used to represent the content for the HTML document.

```html
<body>
  <h1>CatPhotoApp</h1>
  <p>This is a paragraph element.</p>
</body>    
section Elements: This element is used to divide up content into smaller sections.
Example Code
<section>
  <h2>About Me</h2>
  <p>Hi, I am Jane Doe and I am a web developer.</p>
</section>
```

#### `div` Elements

This element is a generic HTML element that does not hold any semantic meaning. It is used as a generic container to hold other HTML elements.

```html
<div>
  <h1>I am a heading</h1>
  <p>I am a paragraph</p>
</div>
```

#### Anchor (`a`) Elements

These elements are used to apply links to a web page. The `href` attribute is used to specify where the link should go when the user clicks on it.

```html
<a href="https://cdn.freecodecamp.org/curriculum/cat-photo-app/running-cats.jpg">cute cats</a>
```

#### Unordered (`ul`) and Ordered (`ol`) List Elements

To create a bulleted list of items you should use the ul element with one or more `li` elements nested inside like this:

```html
<ul>
  <li>catnip</li>
  <li>laser pointers</li>
  <li>lasagna</li>
</ul>
```

To create an ordered list of items you should use the ol element:

```html
<ol>
  <li>flea treatment</li>
  <li>thunder</li>
  <li>other cats</li>
</ol>
```

#### Emphasis (`em`) Element

This is used to place emphasis on a piece of text.

```html
<p>Cats <em>love</em> lasagna.</p>  
```

#### Strong Importance `(strong`) Element

This element is used to place strong emphasis on text to indicate a sense of urgency and seriousness.

```html
<p>
  <strong>Important:</strong> Before proceeding, make sure to wear your safety goggles. 
</p>
```

#### `figure` and `figcaption` Elements

The `figure` element is used to group content like images and diagrams. The `figcaption` element is used to represent a caption for that content inside the `figure` element.

```html
<figure>
  <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Two tabby kittens sleeping together on a couch.">
  <figcaption>Cats <strong>hate</strong> other cats.</figcaption>  
</figure>
```

#### `main` Element

This element is used to represent the main content for a web page.

#### `footer` Element

This element is placed at the bottom of the HTML document and usually contains copyright information and other important page links.

```html
<footer>
  <p>
    No Copyright - <a href="https://www.freecodecamp.org">freeCodeCamp.org</a>
  </p>
</footer>
```

---

[Back to top](#table-of-contents)

---

### Identifiers and Grouping

#### IDs

Unique element identifiers for HTML elements. ID names should only be used once per HTML document.

```html
<h1 id="title">Movie Review Page</h1>
```

ID names cannot have spaces. If your ID name contains multiple words then you can use dashes between the words like this:

```html
<div id="red-box"></div>
```

#### Classes

Classes are used to group elements for styling and behavior.

```html
<div class="box"></div>
```

Unlike IDs, you can reuse the same class name throughout the HTML document. The class value can also have spaces like this:

```html
<div class="box red-box"></div>
<div class="box blue-box"></div>
```

---

[Back to top](#table-of-contents)

---

### Special Characters and Linking

#### HTML entities

An HTML entity, or character reference, is a set of characters used to represent a reserved character in HTML. Examples include the ampersand (`&amp;`) symbol and the less than symbol (`&lt;`).

```html
<p>This is an &lt;img /&gt; element</p>
```

#### `link` Element

This element is used to link to external resources like stylesheets and site icons. Here is the basic syntax for using the `link` element for an external CSS file:

```html
<link rel="stylesheet" href="./styles.css" />
```

The `rel` attribute is used to specify the relationship between the linked resource and the HTML document. The `href` attribute is used to specify the location of the URL for the external resource.

#### `script` Element

This element is used to embed executable code.

```html
<body>
  <script>
    alert("Welcome to freeCodeCamp");
  </script>
</body>
```

While you can technically write all of your JavaScript code inside the script tags, it is considered best practice to link to an external JavaScript file instead. Here is an example of using the script element to link to an external JavaScript file:

```html
<script src="path-to-javascript-file.js"></script>
```

The `src` attribute is used here to specify the location for that external JavaScript file.

---

[Back to top](#table-of-contents)

---

### Boilerplate and Encoding

#### HTML boilerplate

This is a boilerplate that includes the basic structure and essential elements every HTML document needs.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>freeCodeCamp</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <!--Headings, paragraphs, images, etc. go inside here-->
  </body>
</html>
```

#### `DOCTYPE`

This is used to tell browsers which version of HTML you're using.

#### `html` Element

This represents the top level element or the root of an HTML document. To specify the language for the document, you should use the `lang` attribute.

#### `head` Element

The `head` section contains important meta data which is behind-the-scenes information needed for browsers and search engines.

#### `meta` Elements

These elements represent your site's metadata. These element have details about things like character encoding, and how websites like Twitter should preview your page's link and more.

#### `title` Element

This element is used to set the text that appears in the browser tab or window.
UTF-8 character encoding: UTF-8, or UCS Transformation Format 8, is a standardized character encoding widely used on the web. Character encoding is the method computers use to store characters as data. The charset attribute is used inside of a meta element to set the character encoding to UTF-8.

---

[Back to top](#table-of-contents)

---

### SEO and Social Sharing

#### SEO

Search Engine Optimization is a practice that optimizes web pages so they become more visible and rank higher on search engines.

#### Meta (`description`) Element

This is used to provide a short description for the web page and impacting SEO.

```html
<meta
  name="description"
  content="Discover expert tips and techniques for gardening in small spaces, choosing the right plants, and maintaining a thriving garden."
/>
```

#### Open Graph tags

The open graph protocol enables you to control how your website's content appears across various social media platforms, such as Facebook, LinkedIn, and many more.
By setting these open graph properties, you can entice users to want to click and engage with your content. You can set these properties through a collection of `meta` elements inside your HTML `head` section.

##### `og:title` Property

This is used to set the title that displays for social media posts.

```html
<meta content="freeCodeCamp.org" property="og:title" />
```

##### `og:type` Property

The type property is used to represent the type of content being shared on social media. Examples of this content include articles, websites, videos, or music.

```html
<meta property="og:type" content="website" />
```

##### `og:image` Property

This is used to set the image shown for social media posts.

```html
<meta
  content="https://cdn.freecodecamp.org/platform/universal/fcc_meta_1920X1080-indigo.png"
  property="og:image"
/>
```

##### `og:url` Property

This is used to set the URL that users will click on for the social media posts.

```html
<meta property="og:url" content="https://www.freecodecamp.org" />
```

---

[Back to top](#table-of-contents)

---

### Media Elements and Optimization

#### Replaced elements

A replaced element is an element whose content is determined by an external resource rather than by CSS itself. An example would be an `iframe` element. `iframe` stands for inline frame. It's an inline element used to embed other HTML content directly within the HTML page.

```html
<iframe src="https://www.example.com" title="Example Site"></iframe>
```

You can include the `allowfullscreen` attribute which allows the user to display the iframe in full screen mode.

```html
<iframe
  src="video-url"
  width="width-value"
  height="height-value"
  allowfullscreen
></iframe>
```

To embed a video within an `iframe` you can copy it directly from popular video services like YouTube and Vimeo, or define it yourself with the `src` attribute pointing to the URL of that video. Here's an example of embedding a popular freeCodeCamp course from YouTube:

```html
<h1>A freeCodeCamp YouTube Video Embedded with the iframe Element</h1>

<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/PkZNo7MFNFg?si=-UBVIUNM3csdeiWF"
  title="YouTube video player"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
```

There are some other replaced elements, such as `video`, and `embed`. And some elements behave as replaced elements under specific circumstances. Here's an example of an `input` element with the type attribute set to image:

```html
<input type="image" alt="Descriptive text goes here" src="example-img-url">
```

#### Optimizing media

There are three tools to consider when using media, such as images, on your web pages: the size, the format, and the compression. A compression algorithm is used to reduce the size for files or data.

##### Image formats

Two of the most common file formats are PNG and JPG, but these are no longer the most ideal formats for serving images. Unless you need support for older browsers, you should consider using a more optimized format, like WEBP or AVIF.

##### Image licenses

An image under the public domain has no copyright attached to it and is free to be used without any restrictions. Images licensed specifically under the Creative Commons 0 license are considered public domain. Some images might be released under a permissive license, like a Creative Commons license, or the BSD license that freeCodeCamp uses.

##### SVGs

Scalable Vector Graphics track data based on paths and equations to plot points, lines, and curves. What this really means is that a vector graphic, like an SVG, can be scaled to any size without impacting the quality.

#### Multimedia Integration

##### `audio` and `video` Elements

The `audio` and `video` elements allow you to add sound and video content to your HTML documents. The `audio` element supports popular audio formats like mp3, wav, and ogg. The video element supports mp4, ogg, and webm formats.

```html
<audio src="CrystalizeThatInnerChild.mp3"></audio>
```

If you want to see the audio player on the page, then you can add the `audio` element with the `controls` attribute:

```html
<audio src="CrystalizeThatInnerChild.mp3" controls></audio>
```

The `controls` attribute enables users to manage audio playback, including adjusting volume, and pausing, or resuming playback. The controls attribute is a boolean attribute that can be added to an element to enable built-in playback controls. If omitted, no controls will be shown.

##### `loop` Attribute

The `loop` attribute is a boolean attribute that makes the audio replay continuously.

```html
<audio
  src="https://cdn.freecodecamp.org/curriculum/js-music-player/can't-stay-down.mp3"
  loop
  controls
></audio>
```

##### `muted` Attribute

When present in the audio element, the `muted` boolean attribute will start the audio in a muted state.

```html
<audio
  src="https://cdn.freecodecamp.org/curriculum/js-music-player/can't-stay-down.mp3"
  loop
  controls
  muted
></audio>
```

##### `source` Element

When it comes to audio file types, there are differences in which browsers support which type. To accommodate this, you can use `source` elements inside the audio element and the browser will select the first source that it understands. Here's an example of using multiple source elements for an audio element:

```html
<audio controls>
  <source src="audio.ogg" type="audio/ogg" />
  <source src="audio.wav" type="audio/wav" />
  <source src="audio.mp3" type="audio/mpeg" />
</audio>
```

All the attributes we have learned so far are also supported in the `video` element. Here's an example of using a video element with the `loop`, `controls`, and `muted` attributes:

```html
<video
  src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
  loop
  controls
  muted
></video>
```

##### `poster` Attribute

If you wanted to display an image while the video is downloading, you can use the `poster` attribute. This attribute is not available for `audio` elements and is unique to the `video` element.

```html
<video
  src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
  loop
  controls
  muted
  poster="https://peach.blender.org/wp-content/uploads/title_anouncement.jpg?x11217"
  width="620"
></video>
```

---

[Back to top](#table-of-contents)

---

### Target attribute types

#### `target` Attribute

This attribute tells the browser where to open the URL for the anchor element. There are four important possible values for this attribute:

- `_self`
- `_blank`
- `_parent`
- `_top`

There is a fifth value, called `_unfencedTop`, which is currently used for the experimental FencedFrame API. You probably won't have a reason to use this one yet.

##### `_self` Value

This is the default value for the targ`et attribute. This opens the link in the current browsing context. In most cases, this will be the current tab or window.

```html
<a href="https://freecodecamp.org" target="_self">Visit freeCodeCamp</a>
```

##### `_blank` Value

This opens the link in a new browsing context. Typically, this will open in a new tab. But some users might configure their browsers to open a new window instead.

```html
<a href="https://freecodecamp.org" target="_blank">Visit freeCodeCamp</a>
```

##### `_parent` Value

This opens the link in the parent of the current context. For example, if your website has an `iframe`, a `_parent` value in that `iframe` would open in your website's tab/window, not in the embedded frame.

```html
<a href="https://freecodecamp.org" target="_parent">Visit freeCodeCamp</a>
```

##### `_top` Value

This opens the link in the top-most browsing context - think "the parent of the parent". This is similar to `_parent`, but the link will always open in the full browser tab/window, even for nested embedded frames.

```html
<a href="https://freecodecamp.org" target="_top">Visit freeCodeCamp</a>
```

---

[Back to top](#table-of-contents)

---

### Absolute vs. Relative Paths

#### Path definition

A path is a string that specifies the location of a file or directory in a file system. In web development, paths let developers link to resources like images, stylesheets, scripts, and other web pages.

#### Path Syntax

There are three key syntaxes to know. First is the slash, which can be a backslash (`\`) or forward slash (`/`) depending on your operating system. The second is the single dot (`.`). And finally, we have the double dot (`..`).

> The slash is known as the "path separator". It is used to indicate a break in the text between folder or file names. A single dot points to the current directory, and two dots point to the parent directory.

```bash
public/index.html
./favicon.ico
../src/index.css
```

#### Absolute Path

An absolute path is a complete link to a resource. It starts from the root directory, includes every other directory, and finally the filename and extension. The "root directory" refers to the top-level directory or folder in a hierarchy. An absolute path also includes the protocol - which could be http, https, and file and the domain name if the resource is on the web.

Here's an example of an absolute path that links to the freeCodeCamp logo:

```html
<a href="https://design-style-guide.freecodecamp.org/img/fcc_secondary_small.svg">
  View fCC Logo
</a>
```

#### Relative Path

A relative path specifies the location of a file relative to the directory of the current file. It does not include the protocol or the domain name, making it shorter and more flexible for internal links within the same website. Here's an example of linking to the `about.html` page from the `contact.html` page, both of which are in the same folder:

```html
<p>
  Read more on the
  <a href="about.html">About Page</a>
</p>
```

---

[Back to top](#table-of-contents)

---

### Link states

#### `:link`

This is the default state. This state represents a link which the user has not visited, clicked, or interacted with yet. You can think of this state as providing the base styles for all links on your page. The other states build on top of it.

#### `:visited`

This applies when a user has already visited the page being linked to. By default, this turns the link purple - but you can leverage CSS to provide a different visual indication to the user.

#### `:hover`

This state applies when a user is hovering their cursor over a link. This state is helpful for providing extra attention to a link, to ensure a user actually intends to click it.

#### `:focus`

This state applies when we focus on a link.

#### `:active`

This state applies to links that are being activated by the user. This typically means clicking on the link with the primary mouse button by left clicking, in most cases.

---

[Back to top](#table-of-contents)

---

## Semantic HTML

### Importance of Semantic HTML

Semantics are the meaning of words, or phrases, in a language. In HTML, which is a language, elements have their own semantic meaning too. In fact, you can think of your HTML document like you would a text document. And much like a text document, you might have headings, images, bold text, and other formatting.

Most elements have semantic meaning. The `div` element is one of the very few that does not. But why is this important?

First and foremost, using proper semantic HTML will ensure the best experience for users with assistive technology like screen readers. But also, semantic HTML can improve your search rankings. This is referred to as search engine optimization, or SEO.

Finally, using correct semantic elements can improve your development experience. Rather than having to sift through a bunch of developments to find your navigation bar, you can edit the nav element directly and know what you're changing. Throughout this section, you will learn more about these topics, how to use semantic elements, and why semantic HTML is so important.

It is important to use the correct heading element to maintain the structural hierarchy of the content. The `h1` element is the highest level of heading and the `h6` element is the lowest level of heading.

---

[Back to top](#table-of-contents)

---

### Presentational HTML elements

Presentational HTML focuses on the appearance and style of the content. In the early days of HTML, developers would use elements like the `center`, `big`, and `font` elements. But in modern web development you shouldn't use these types of elements, because of their limitations and negative impact on accessibility and maintainability.

Many presentational HTML elements are deprecated, which means that they are outdated and no longer recommended. There are better ways to get the same results. However, it is helpful to know that they exist, so we'll take a look at some examples.

#### `font` Element

The `font` element is a deprecated element used to set the font size and color of the text. Here's an example of a font element:

```html
<font size="5" color="blue">This text is blue and large.</font>
```

> This example sets the color of the text to blue and the size to a value of `5`. The range for the size attribute is from `1` to `7`, with `1` being the smallest and `7` being the largest. The default value is `3`, if you don't set the value explicitly.

*While this element still works, you should not use it because the font size and color should always be set in CSS, not in HTML.*

#### `center` Element

The `center` element is another deprecated element that is used to center the content horizontally within its container. Here's an example of the center element that contains text and a paragraph element:

```html
<center>
  This text is centered.
  <p>HTML is awesome.</p>
</center>
```

In the browser, you would see all of the content within the `center` element centered horizontally.

#### `big` Element

And next, we have the `big` element. This is another deprecated presentational HTML element that makes the enclosed text one level bigger than its surrounding text. Here we have an example that defines a paragraph with two parts:

```html
<p>
  This text has a normal font size.
  <big>This text is larger.</big>
</p>
```

The first part has normal sized text, while the second part enclosed within the `big` element will be displayed in a larger font size. In the browser, you would see the text within the `big` element looks larger compared to the surrounding text.

*However, remember that font size should always be set with CSS, so you should not use this element in modern HTML.*

---

[Back to top](#table-of-contents)

---

### Semantic HTML Elements

#### Header element

Used to define the header of a document or section.

#### Main element

Used to contain the main content of the web page.

#### Section element

Used to divide up content into smaller sections.

#### Navigation Section (`nav`) element

Represents a section with navigation links.

#### Figure element

Used to contain illustrations and diagrams.

#### Emphasis (`em`) element

Marks text that has stress emphasis.

```html
<p>
  Never give up on <em>your</em> dreams.
</p>
```

#### Idiomatic Text (`i`) element

Used for highlighting alternative voice or mood, idiomatic terms from another language, technical terms, and thoughts.

```html
<p>
  There is a certain <i lang="fr">je ne sais quoi</i> in the air.
</p>
```

The `lang` attribute inside the open `i` tag is used to specify the language of the content. In this case, the language would be French. The `i` element does not indicate if the text is important or not, it only shows that it's somehow different from the surrounding text.

#### Strong Importance (`strong`) element

Marks text that has strong importance.

```html
<p>
  <strong>Warning:</strong> This product may cause allergic reactions.
</p>
```

#### Bring Attention To (`b`) element

Used to bring attention to text that is not important for the meaning of the content. It's commonly used to highlight keywords in summaries or product names in reviews.

```html
<p>
  We tested several products, including the <b>SuperSound 3000</b> for audio quality, the <b>QuickCharge Pro</b> for fast charging, and the <b>Ecoclean Vacuum</b> for cleaning. The first two performed well, but the <b>Ecoclean Vacuum</b> did not meet expectations.
</p>
```

#### Description List (`dl`) element

Used to represent a list of term-description groupings.

##### Description Term (`dt`) element

Used to represent the term being defined.

##### Description Details (`dd`) element

Used to represent the description of the term.

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
</dl>
```

#### Block Quotation (`blockquote`) element

Used to represent a section that is quoted from another source. This element has a `cite` attribute. The value of the `cite` attribute is the URL of the source.

```html
<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
  "Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?"
</blockquote>
```

#### Citation (`cite`) element

Used to attribute the source of the referenced work visually. Marks up the title of the reference.

```html
<div>
  <blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    "Can you imagine what it would be like to be a successful developer? To have built software systems that people rely upon?"
  </blockquote>
  <p>
    -Quincy Larson, <cite>How to learn to Code and Get a Developer Job [Full Book].</cite>
  </p>
</div>
```

#### Inline Quotation (`q`) element

Used to represent a short inline quotation.

```html
<p>
  As Quincy Larson said,
  <q cite="https://www.freecodecamp.org/news/learn-to-code-book/">
    Momentum is everything.
  </q>
</p>
```

#### Abbreviation (`abbr`) element

Used to represent an abbreviation or acronym. To help users understand what the abbreviation or acronym is, you can show its full form, a human readable description, with the title attribute.

```html
<p>
  <abbr title="HyperText Markup Language">HTML</abbr> is the foundation of the web.
</p>
```

#### Contact Address (`address`) element

Used to represent the contact information.

#### Date and Time (`time`) element

Used to represent a date and/or time. The datetime attribute is used to translate dates and times into a machine-readable format.

```html
<p>
  The reservations are for the <time datetime="20:00">20:00 </time>
</p>
```

##### ISO 8601 Date (`datetime`) attribute

Used to represent dates and times in a machine-readable format. The standard format is `YYYY-MM-DDThh:mm:ss`, with the capital `T` being a separator between the date and time.

#### Superscript (`sup`) element

Used to represent superscript text. Common use cases for the `sup` element would include exponents, superior lettering and ordinal numbers.

```html
<p>
  2<sup>2</sup> (2 squared) is 4.
</p>
```

#### Subscript (`sub`) element

Used to represent subscript text. Common use cases for the subscript element include chemical formulas, footnotes, and variable subscripts.

```html
<p>
  CO<sub>2</sub>
</p>
```

#### Inline Code (`code`) element

Used to represent a fragment of computer code.

#### Preformatted Text (`pre`) element

Represents preformatted text

```html
<pre>
  <code>
    body {
      color: red;
    }
  </code>
</pre>
```

#### Unarticulated Annotation (`u`) element

Used to represent a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation.

```html
<p>
  You can use the unarticulated annotation element to highlight
  <u>inccccort</u> <u>spling</u> <u>issses</u>.
</p>
```

#### Ruby Annotation (`ruby`) element

Used for annotating text with pronunciation or meaning explanations. An example usage is for East Asian typography.

##### Ruby fallback parenthesis (`rp`) element

Used as a fallback for browsers lacking support for displaying ruby annotations.

##### Ruby text (`rt`) element

Used to indicate text for the ruby annotation. Usually used for pronunciation, or translation details in East Asian typography.

```html
<ruby>
  明日 <rp>(</rp><rt>Ashita</rt><rp>)</rp>
</ruby>
```

#### Strikethrough (`s`) element

Used to represent content that is no longer accurate or relevant.

```html
<p>
  <s>Tomorrow's hike will be meeting at noon.</s>
</p>
<p>
  Due to unforeseen weather conditions, the hike has been canceled.
</p>
```

---

[Back to top](#table-of-contents)

---

## Forms and Tables

### HTML Form Elements and Attributes

- `form` element: used to create an HTML form for user input.

- `action` attribute: used to specify the URL where the form data should be sent.

- `method` attribute: used to specify the HTTP method to use when sending the form data. The most common methods are `GET` and `POST`.

```html
<form method="value-goes-here" action="url-goes-here">
  <!-- inputs go inside here -->
</form>
```

- `input` element: used to create an input field for user input.

- `type` attribute: used to specify the type of input field. Ex. `text`, `email`, `number`, `radio`, `checkbox`, etc.

- `placeholder` attribute: used to show a hint to the user to show them what to enter in the input field.

- `value` attribute: used to specify the value of the input. If the input has a `button` type, the `value` attribute can be used to set the button text.

- `name` attribute: used to assign a name to an input field, which serves as the key when form data is submitted. For `radio` buttons, giving them the same `name` groups them together, so only one option in the group can be selected at a time.

- `size` attribute: used to define the number of characters that should be visible as the user types into the input.

- `min` attribute: can be used with input types such as `number` to specify the minimum value allowed in the input field.

- `max` attribute: can be used with input types such as `number` to specify the maximum value allowed in the input field.

- `minlength` attribute: used to specify the minimum number of characters required in an input field.

- `maxlength` attribute: used to specify the maximum number of characters allowed in an input field.

- `required` attribute: used to specify that an input field must be filled out before submitting the form.

- `disabled` attribute: used to specify that an input field should be disabled.

- `readonly` attribute: used to specify that an input field is read-only.

```html
<!-- Text input -->
<input 
  type="text"
  id="name"
  name="name"
  placeholder="e.g. Quincy Larson" 
  size="20"
  minlength="5"
  maxlength="30"
  required
/>

<!-- Number input -->
<input 
  type="number"
  id="quantity"
  name="quantity"
  min="2"
  max="10"
  disabled
/>

<!-- Button -->
<input type="button" value="Show Alert" />
```

- `label` element: used to create a label for an input field.

- `for` attribute: used to specify which input field the label is for.

**Implicit form association:** inputs can be associated with labels by wrapping the input field inside the `label` element.

```html
<form action="">
  <label>
    Full Name:
    <input type="text" />
  </label>
</form>
```

**Explicit form association:** inputs can be associated with labels by using the `for` attribute on the `label` element.

```html
<form action="">
  <label for="email">Email Address: </label>
  <input type="email" id="email" />
</form>
```

- `button` element: used to create a clickable button. A button can also have a `type` attribute, which is used to control the behavior of the button when it is activated. Ex. `submit`, `reset`, `button`.

```html
<button type="button">Show Form</button>
<button type="submit">Submit Form</button>
<button type="reset">Reset Form</button>
```

- `fieldset` element: used to group related inputs together.

- `legend` element: used to add a caption to describe the group of inputs.

```html
<!-- Radio group -->
<fieldset>
  <legend>Was this your first time at our hotel?</legend>

  <label for="yes-option">Yes</label>
  <input id="yes-option" type="radio" name="hotel-stay" value="yes" />

  <label for="no-option">No</label>
  <input id="no-option" type="radio" name="hotel-stay" value="no" />
</fieldset>

<!-- Checkbox group -->
<fieldset>
  <legend>
    Why did you choose to stay at our hotel? (Check all that apply)
  </legend>

  <label for="location">Location</label>
  <input type="checkbox" id="location" name="location" value="location" />

  <label for="price">Price</label>
  <input type="checkbox" id="price" name="price" value="price" />
</fieldset>
```

**Focused state:** this is the state of an input field when it is selected by the user.

---

[Back to top](#table-of-contents)

---

### HTML Table Elements and Attributes

- `table` element: used to create an HTML table.

- Table Head (`thead`) element: used to group the header content in an HTML table.

- Table Row (`tr`) element: used to create a row in an HTML table.

- Table Header (`th`) element: used to create a header cell in an HTML table.

- Table body (`tbody`) element: used to group the body content in an HTML table.

- Table Data Cell (`td`) element: used to create a data cell in an HTML table.

- Table Foot (`tfoot`) element: used to group the footer content in an HTML table.

- `caption` element: used to add a title of an HTML table.

- `colspan` attribute: used to specify the number of columns a table cell should span.

```html
<table>
  <caption>Exam Grades</caption>

  <thead>
    <tr>
      <th>Last Name</th>
      <th>First Name</th>
      <th>Grade</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Davis</td>
      <td>Alex</td>
      <td>54</td>
    </tr>

    <tr>
      <td>Doe</td>
      <td>Samantha</td>
      <td>92</td>
    </tr>

    <tr>
      <td>Rodriguez</td>
      <td>Marcus</td>
      <td>88</td>
    </tr>
  </tbody>

  <tfoot>
    <tr>
      <td colspan="2">Average Grade</td>
      <td>78</td>
    </tr>
  </tfoot>
</table>
```

### Working with HTML Tools

**HTML validator:** a tool that checks the syntax of HTML code to ensure it is valid.

**DOM inspector:** a tool that allows you to inspect and modify the HTML structure of a web page.

**Devtools:** a set of web developer tools built directly into the browser that helps you debug, profile, and analyze web pages.

---

[Back to top](#table-of-contents)

---

## Accessibility

### What is Accessability?

Accessibility involves creating products and services that everyone can use. In the context of web development, it's making websites that everyone can understand and interact with, including people with visual, auditory, motor, and cognitive disabilities.

> Some examples of disabilities that can impact users' online experience include:
>
> - Blindness.
> - Low vision.
> - Color blindness.
> - Deafness.
> - Difficulty using keyboards, mice, or touchscreens.
> - Attention disorders
> - Memory issues.
> - Difficulty speaking or understanding spoken language.
> - Sensitivity to flashing lights.

To help you create accessible websites, the **World Wide Web Consortium**, known as **W3C**, developed a set of international standards that you can follow to make your websites more accessible and easier to use for people with disabilities.

These standards are known as "**The Web Content Accessibility Guidelines**" (**WCAG**).

These guidelines are designed with four core principles in mind, known as ***POUR***.

- **P** stands for *Perceivable*. Users must be able to perceive the information that you are presenting. For example, you can provide alternative text for images, so users who access your website with a screen reader can understand them.

- **O** stands for *Operable*. Users must be able to interact with the user interface. For example, you can make sure that all functionality is accessible through the keyboard too, not just the mouse.

- **U** stands for *Understandable*. Users must be able to understand the information. For example, you can avoid complex sentences and use simple language as much as possible.

- **R** stands for *Robust*. A wide range of browsers and other tools, including assistive technologies, must be able to interpret the content.
Using semantic HTML is very helpful for making your website compatible with different browsers and assistive technologies.

If your content doesn't follow any one of these core principles, not everyone will be able to use your website.

> To check if you are following these guidelines correctly, you can access the Quick Reference of the World Wide Web Consortium. There, you will find a comprehensive list of criteria and techniques.

Accessibility is essential for web development. By developing with inclusivity in mind, you can ensure that everyone can access and engage with your content, promote equality and create a better user experience for everyone around the world.

---

[Back to top](#table-of-contents)

---

### Screen Readers

Screen readers are assistive technology programs that help blind and visually impaired people use computers and mobile devices.

Screen readers are not just tools for the blind and visually impaired to access computers and mobile devices. They empower these individuals to access education, work opportunities, and social media. This ensures digital inclusion and enhances their ability to participate fully in society.

There's a common misconception that screen readers are text-to-speech devices. However, text-to-speech is just one of the features of a screen reader. Some screen readers even render the text to braille output instead of speech.

Apart from text-to-speech and braille output, other notable features of screen readers are navigation aids and web browsing assistance.

Screen reader programs are also not only made for the blind and visually impaired. Dyslexic individuals and people with cognitive disabilities also use screen readers. All the popular operating systems out there have screen readers built into them.

> **macOS** and **iOS** both have ***VoiceOver*** built-in. You can turn it on on your computer by pressing CMD + F5. You can access it on iPhones through Settings.
>
> **Windows** computers have ***Narrator*** built-in. You can turn it on by pressing WIN + CTRL + ENTER. ***NonVisual Desktop Access*** (NVDA) and ***Job Access With Speech*** (JAWS) are also available for Windows computers. NVDA is free and open-source, while JAWS is paid.
>
> **Linux** has ***Orca*** for the desktop environment and ***Speakup*** for the Linux terminal.
>
> **Android** phones have ***TalkBack*** built-in. You can turn it on by accessing Settings > Special Function > Accessibility > Talkback.
>
> Some **Android** devices also have ***Ella*** and ***Select to Speak*** built in.

One major challenge for screen reader users is that many software developers don't design their products with screen-reader friendliness and accessibility in mind.

Even though accessibility is a broad topic, every developer needs to learn how to make their web software accessible for the blind and visually impaired, as well as other groups of people with disabilities.

This demonstrates empathy and a commitment to inclusivity, ensuring that all users can benefit from their work.

---

[Back to top](#table-of-contents)

---

### Large Text and Braille Keyboards

**Large Text** and **Braille** keyboards are designed for users with visual disabilities. In Large Text Keyboards, also called Large Print Keyboards, the letters, numbers, and symbols are larger compared to standard keyboards. This design is helpful for people who may find smaller text in the keys difficult to see. Most of them also have enhanced contrast and brightness.

While large print keyboards provide visual cues for users with low vision, braille keyboards provide a completely tactile experience for people with more severe vision disabilities, including people who are blind.

---

Braille is a tactile reading and writing system. It consists of raised dots arranged in specific patterns to represent letters, numbers, and punctuation.

Braille keyboards use this system to help users find the right keys on the keyboard by feeling these patterns with their fingers. The keys have raised dots in patterns that represent letters, numbers and symbols.

---

Some keyboards combine both approaches- large fonts and braille patterns in the keys. This is helpful for people with visual disabilities and for people who are learning braille.

Large text and braille keyboards are tools that empower people with visual disabilities. By providing alternative input methods, these assistive technologies ensure that everyone can be part of the digital world.

---

[Back to top](#table-of-contents)

---

### Alternative Pointing Devices

Alternative pointing devices are input devices that make good alternatives to the traditional mouse. They are essential for improving computer accessibility for those with disabilities, forelimb impairments, and limited mobility.

> Common examples of alternative pointing devices are trackballs, joysticks, and touchpads.

---

A **Trackball** is a stationary pointing device that consists of a large, movable ball within a socket. It also includes additional buttons for clicking and performing other functions.

Unlike the traditional mouse, which requires movement around a surface to control the cursor, a trackball remains in place. Users manipulate the ball directly with their fingers, thumb, or palm to move the cursor on the screen.

Some traditional mice also have a trackball on the top or side. These mice could make a good starting point if you want to gradually switch to a trackball.

Trackballs reduce the physical movement the user needs for navigation, making them ideal for users with mobility issues. Apart from that, if you need high precision and have limited desk space, a trackball is more ideal than a traditional mouse.

---

A **Joystick** is a pointing device primarily designed for games and certain industrial applications like machinery control. It consists of a lever that pivots up, down, left, and right, and often includes additional buttons for various actions

Joysticks provide precise control over movement and actions within digital environments. This makes them popular for flight simulators, cranes, driving games, and other applications requiring precise directional input.

Because joysticks accommodate larger and more deliberate movements, they are beneficial for individuals with tremors and unsteady hands.

They also reduce the strain and pain that comes with repetitive movements, making them ideal for individuals with arthritis and carpal tunnel syndrome.

---

A **Touchpad** is a flat, touch-sensitive device built into laptops and some keyboards. It allows users to control the cursor on the screen by sliding their fingers across its surface.

Apart from the surface for cursor control, touchpads also feature buttons that emulate the actions of a traditional mouse, such as right-click and left-click.

Most people see touchpads as a better alternative to a mouse because they significantly enhance navigation by supporting multi-touch gestures like pinch-to-zoom, two-finger scrolling, tap-to-click, and three-finger swipes.

Touchpad is ideal for individuals with low arm or hand movement because the forelimb is almost always stationary while using it. It is also suitable for people with arthritis and joint pain because they don't get to move their arms too much.

---

[Back to top](#table-of-contents)

---

### Screen Magnifiers

Screen magnifiers are tools that help people with low vision and other visual impairments better access digital content and the web.

Let's delve deeper into what these tools are and the role they play in digital content accessibility.

Screen magnifiers work by enlarging texts, graphics, and other elements on a computer or mobile device screen. Many screen magnifiers allow users to enlarge the display by more than 200%. Users can then navigate the page using their pointing device or keyboard. Additionally, most magnifiers offer customizable zoom percentages and other features in their settings.

Screen magnifiers primarily help people with low vision read text, as small fonts in documents or applications can be challenging for them. By enlarging the text, they can read emails, articles, and other content without straining their eyes. Screen magnifiers also assist with web browsing. They help users locate and click on buttons, links, and other interactive elements that might be difficult to see. This improved visibility ensures that users can browse websites, fill out forms, and engage in online activities without difficulty.

Therefore, software developers need to make their digital products accessible to people with low vision. Some considerations include:

Using scalable fonts so the user can resize the page without the layout breaking.
Ensuring the user interface adapts to different screen sizes through responsive design.
Using high-contrast color schemes and customizable colors.
Implementing a non-sticky and tiny navbar so users can still see content when using magnifiers.
Using regular HTML text instead of images of text.
Providing feedback directly next to the element that triggers it, and more.

> All the mainstay Operating Systems have at least one magnifier built into them by their manufacturers:
>
> - **macOS** and **iOS** both have ***Zoom***. You can turn it on on macOS by going to Settings, filter by Accessibility, and then click on "Zoom". Toggle the "Use keyboard shortcuts to zoom" option to enable it.
You can turn it on on iPhone through Settings > Accessibility > Zoom.
> - **Android** devices have ***Magnification***. To turn it on, go to Settings > Special Function > Accessibility> Magnification. Since this may vary from device to device, you can search for "Magnification" on the settings homepage to access it.
> - **Windows** has ***Magnifier***. You can use it by going to Settings > Ease of Access > Magnifier.
The magnifiers for Linux operating systems vary. It is either Zoom or Magnifier.

---

> Apart from the ones built into operating systems, some useful third party screen magnifiers are:
>
> - ZoomText for Windows.
> - ClaroView for both macOS and Windows.
> - iZoom for Windows.
> - Zoomify - Screen Magnifier for macOS.
> - LunarPluse for Windows.
> - Loupe for macOS.

---

[Back to top](#table-of-contents)

---

### Voice Recognition Software

Voice recognition software helps people with disabilities interact with computers and other digital devices. Let's discuss what voice recognition software is and the role it plays in digital inclusion.

In the context of accessibility, voice recognition tools let people with disabilities use their voice to pass commands to perform various tasks instead of using traditional input devices like keyboards and mice. This includes writing emails and other documents, surfing the net, and controlling smart home devices.

Because voice recognition software tools eliminate the need for physical interaction, they empower people with disabilities with significant independence and control over their environment.

Here are the specific people who may find voice recognition software significantly helpful:

- People with visual impairments, including those with low-vision or blindness.
- Individuals with mobility impairments, such as limited use of hands and arms or conditions like arthritis and carpal tunnel syndrome.
- Those recovering from hand or arm injuries.
- Individuals with cognitive disorders, like memory issues or attention deficit disorders.
- Elderly individuals who might find it easier to use voice commands.

Note that people with disabilities are not the only ones who use voice recognition technology. Law enforcement agencies, gamers, drivers, and busy professionals also use voice recognition tools.

> A few examples of voice recognition software that allows people to interact with their computer include:
>
> - ***Voice Control*** for **macOS/iOS**
> - ***Voice Access*** for **Android**
> - ***Windows Speech Recognition*** for **Windows** (referred to as Voice Access in the most recent versions of Windows).
> - ***Dragon*** by Nuance is a popular third-party voice recognition software for Windows.

---

[Back to top](#table-of-contents)

---

### Accessability Auditing Tools

An accessibility auditing tool is an application that helps you improve the accessibility of your digital content by reporting accessibility issues that can be easily found through automated testing. This content includes websites, web applications, and mobile apps.

It is important to note that while automated accessibility tools have a role in improving accessibility, they typically will only find about a third of all possible accessibility issues. Therefore, it is important not to rely on them entirely to evaluate the accessibility of your content. Manual testing, preferably by people with disabilities, will always be required to ensure that your content is as accessible as possible.

---

Let's look at some free tools that can help you improve the accessibility of your digital content.

**Google Lighthouse** is a popular web metric checker you can use directly within Chrome DevTools or online. This means you can check not only live websites but also locally-developed ones.

The metrics you can check include accessibility, SEO, best practices, and performance.

To use Lighthouse, open your DevTools by pressing F12 and switching to the Lighthouse tab. Select the metrics you want to check, choose the device you want to test on, and click the "Analyze page load" button.

An accessibility score will appear after the check is complete, along with a list of any issues that need fixing.

If you want more reliable metrics, consider using the web version. The downside is that it doesn't support testing local websites. You can access the web version on pagespeed.web.dev.

**WAVE** is another reliable accessibility checker you can use as a Chrome extension or on the web. All you need to do is enter the URL of your website and a comprehensive accessibility report will be generated for you. This report includes accessibility features implemented, ARIA, and contrasts.

The **IBM Equal Accessibility Checker** is another robust tool for improving digital content accessibility. With it, you can scan your websites for accessibility issues and generate a detailed report.

You can use it as a Chrome extension or Firefox add-on.

To use the IBM Accessibility Checker as a Chrome extension, download it from the Chrome web store. Open your Devtools by pressing F12 and selecting the "Accessibility Checker" tab located in the Elements panel. Click the scan button to start the check and a report will be generated for you. You can export the report as a spreadsheet and an HTML file by clicking the "Export XLS" button.

> Please keep in mind, while these automated tools help you make your content more accessible, a perfect score from any of them does not mean that your content is entirely accessible. The range of issues that these tools test for is limited, and manual testing will always be needed to ensure a more accessible experience for everyone.

---

[Back to top](#table-of-contents)

---

### Introduction to ARIA

---

[Back to top](#table-of-contents)

---

## References

*Certified Full Stack Developer Curriculum*. freecodecamp.org. (n.d.). <https://www.freecodecamp.org/learn/full-stack-developer/>

---

[Back to top](#table-of-contents)

---
