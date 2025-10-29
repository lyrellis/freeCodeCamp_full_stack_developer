# CSS Notes

> Notes from the CSS curriculum within the freeCodeCamp Full Stack Developer curriculum

The source material can be found here:

<https://www.freecodecamp.org/learn/full-stack-developer>

## Table of Contents

1. [Basic CSS](#basic-css)

## Basic CSS

### What is CSS?

CSS, which stands for Cascading Style Sheets, is a crucial component of modern web development. It's a markup language used to apply styles for HTML. In simpler terms, if HTML is the structure of a web page, CSS is what makes it look good.

Here is an example of styling a navbar.

[HTML](./css-notes-sandbox/what-is-css/1/index.html)

[CSS](./css-notes-sandbox/what-is-css/1/styles.css)

The primary role of CSS is to separate the content of a web page from its visual presentation. This separation allows web developers to create more flexible and maintainable websites.

With CSS, you can control the layout, colors, fonts, and overall visual appearance of web pages without altering the HTML structure.

Let's consider a simple analogy. If you think of a website as a house, HTML would be the foundation and framework, while CSS would be the paint, wallpaper, and decorations that make the house visually appealing and unique.

CSS works by selecting HTML elements and applying styles to them.

Here is an example showing an unstyled `button` element and a styled one.

[HTML](./css-notes-sandbox/what-is-css/2/index.html)

[CSS](./css-notes-sandbox/what-is-css/2/styles.css)

These styles can include properties like color, font size, and many more. By changing these properties, you can dramatically alter how a web page looks without changing its content.

One of the most powerful aspects of CSS is its ability to create responsive designs.

This means that with CSS, you can make your website look great on any device, whether it's a desktop computer, a tablet, or a smartphone.

CSS allows you to adjust layouts, font sizes, and other visual elements based on the screen size of the device viewing the website.

Try adjusting the size of the preview window to see how the layout adapts to the screen size.

[HTML](./css-notes-sandbox/what-is-css/3/index.html)

[CSS](./css-notes-sandbox/what-is-css/3/styles.css)

Another important feature of CSS is its cascading nature, which is where the "cascading" in its name comes from.

This means that styles can be inherited and overridden, allowing for a hierarchical structure of styling. You will learn more about how this works in future lessons.

CSS also supports the use of external stylesheets.

This means you can keep all your styling rules in a separate file, which can then be linked to multiple HTML pages.

This feature greatly enhances the maintainability of websites, especially larger ones. Instead of having to change styles on each individual page, you can make changes in one CSS file that will affect all linked pages.

In the world of web development, CSS plays a vital role in creating visually appealing, responsive, and user-friendly websites.

It allows developers to transform simple HTML documents into engaging web experiences that capture users' attention and enhance their interaction with web content.

#### Basic Anatomy

CSS is responsible for the styles of a web page. All of these styles are made up of various CSS rules.

A CSS rule is made up of two main parts: a **selector** and a **declaration** block.

Let's take a look at the basic syntax:

```css
selector {
  property: value;
}
```

A selector is a pattern used in CSS to identify and target specific HTML elements for styling.

Examples of selectors include type selectors, class selectors, and ID selectors.

The curly braces provided in the basic syntax are known as a declaration block. A declaration block applies a set of styles for a given selector, or selectors.

Inside the declaration block, you will have a series of declarations. Each declaration consists of a property and a value.

The property is the CSS identifier that specifies which feature is being styled. An example of a property would be the background-color property.

The value would be the specific setting applied to that property. For example, if the property is background-color, a value could be purple, which sets the background color to purple.

After each property name, you need to place a colon, and after each value, you should have a semicolon.

Now that you know the syntax for a CSS rule, let's take a look at an example. Click on the `styles.css` tab in the interactive editor to see the CSS code.

[HTML](./css-notes-sandbox/basic-anatomy/1/index.html)

[CSS](./css-notes-sandbox/basic-anatomy/1/styles.css)

In this CSS rule, a type selector targets all paragraph elements on the page.

Inside the declaration block, there is a one declaration.

The declaration consists of the color property with a value set to blue. This will change the text color for all paragraph elements to blue.

If you want to apply the same set of styles to multiple selectors, you can create a selector list with each selector separated by a comma.

Here is an example of styling multiple selectors:

[HTML](./css-notes-sandbox/basic-anatomy/2/index.html)

[CSS](./css-notes-sandbox/basic-anatomy/2/styles.css)

In this selector list, there is an `id` selector targeting the HTML element with the `id` value of `title`. All id selectors must start with a hash `#` symbol.

Then there is a comma followed by a `class` selector that targets all HTML elements with the `class` value of `subheading`. All class selectors must start with a dot `.`

The entire selector list will receive the same styling, with the text color set to `navy`.

#### Meta Viewport Element

The meta viewport element is a crucial component in responsive web design.

It's a special HTML meta element that gives the browser instructions on how to control the page's dimensions and scaling on different devices, particularly on mobile phones and tablets.

Let's take a look at the basic syntax of the meta viewport element:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

This element is typically placed in the `head` section of your HTML document. But what does each part of the element mean?

The `width=device-width` part tells the browser to set the width of the page to match the screen width of the device. This is essential for creating responsive layouts that adapt to different screen sizes.

The `initial-scale=1.0` sets the initial zoom level when the page is first loaded. A value of `1.0` means that the page is displayed at 100% zoom, without any scaling.

By using the meta viewport element, you're ensuring that your web pages are displayed properly on mobile devices.

Without it, mobile browsers will typically render the page at a desktop screen width and then scale it down, which can result in a poor user experience with tiny, hard-to-read text.

The meta viewport element also allows you to control whether users can zoom in and out of your web pages.

While it's possible to disable zooming with the `user-scalable=no` attribute, it's generally recommended to avoid this for accessibility reasons.

Many users rely on the ability to zoom for better readability, especially those with visual impairments.

Here's an example of what not to do:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
```

Instead, it's better to design your website to be responsive and readable at different zoom levels, ensuring that all users can comfortably access your content.

The meta viewport element plays a crucial role in creating mobile-friendly websites.

It ensures that your carefully crafted responsive designs are displayed as intended on various devices, providing a better user experience for all visitors to your site.

#### Default Browser Styles

When you start working with HTML and CSS, you'll notice that some styles are applied to your web pages even before you write any CSS. These styles are called "default browser styles" or "user-agent styles".

These default browser styles provide basic formatting to ensure that HTML elements are displayed in a readable way across all browsers.

However, these styles can vary slightly from one browser to another, which is why it's important to understand them when designing a consistent look for your website.

Let’s take a look at some common default browser styles applied to various HTML elements.

Headings are one of the most commonly used HTML elements and are styled by default to have varying sizes and weights.

For example, h1 (the highest-level heading) is usually bold and larger in font size compared to lower-level headings like `h2`, `h3`, and so on.

These heading tags help define the hierarchy and structure of your content.

Another element with default styles is the `hr` element, which creates a horizontal rule often used to visually separate sections of content. Browsers generally apply a simple line style to this element.

The horizontal rule appears as a thin line with spacing above and below the text to distinguish between sections of content.

Next, we will look at the `blockquote` element.

Blockquotes are used to indicate a section of text that is a quotation from another source. Browsers typically add indentation and sometimes italicize the text.

The indentation helps set blockquotes apart from the rest of the text, making it clear that this content is quoted from another source.

Another element with default styles is the anchor element (`<a>`), which is styled with a default blue color and underlining to make it recognizable as a link.

Finally, we'll look at the unordered and ordered list elements.

Browsers add basic formatting to lists, including indentation and bullets or numbers, depending on whether you are using an unordered list (`ul`) or an ordered list (`ol`).

In later lessons, you will learn how to reset some of these default styles using a CSS reset.

#### Inline, Internal and External CSS

CSS can be applied to a webpage in three main ways: inline, internal, or external.

Each method has its own use case, advantages, and limitations, and knowing when to use each one is essential for writing clean, efficient, and maintainable code.

Let’s break down the three types of CSS and when you should use them.

Inline CSS is written directly within an HTML element using the `style` attribute. It applies styles to a specific element.

Here's an example using inline CSS:

```html
<p style="color: green;">This is an inline-styled paragraph.</p>
```

In this example, we are using the `style` attribute to set the paragraph text to `green`.

Inline CSS is generally used for quick, one-off styles or to override other styles for a specific element.

However, it should be avoided in most cases because it can clutter the HTML and make the code harder to maintain.

Most of the time, it's better to use internal or external CSS to keep your styles organized and maintainable.

Internal CSS is written within the `style` tags inside the `head` section of an HTML document. It applies styles to the entire page and is useful when you need to style a single document.

Here's an example of internal CSS:

```html
<head>
  <style>
    p {
      color: blue;
    }
  </style>
</head>
<body>
    <p>This paragraph is styled using internal CSS.</p>
</body>
```

In the above example, the internal CSS applies `blue` text to all `p` elements on the page.

Internal CSS is best used when you need to apply styles to a specific page rather than across multiple pages. It’s useful for single-page websites or when the styles don’t need to be reused elsewhere.

However, there are some downsides, such as not promoting reusability across multiple pages. Additionally, like inline CSS, it mixes HTML and CSS, making the code harder to maintain in larger projects.

External CSS is written in a separate `.css` file and linked to the HTML document using the `link` element in the `head` section.

It allows you to style multiple pages consistently and is the preferred method in professional web development.

Here is an example of styling all paragraph elements:

[HTML](./css-notes-sandbox/inline-internal-and-external-css/1/index.html)

[CSS](./css-notes-sandbox/inline-internal-and-external-css/1/styles.css)

In an earlier lesson, you learned that the `link` element has a `rel` attribute that specifies the relationship between the current document and the linked resource, such as linking to a stylesheet or an external resource.

On the other hand, the `href` attribute specifies the URL of the linked resource, indicating where the resource should be retrieved from.

External CSS is ideal for large projects where you want to maintain a consistent style across multiple pages.

It promotes separation of concerns by having HTML handle the structure and CSS handle the styling, which makes the code more maintainable and scalable.

Understanding when to use each type of CSS is crucial for efficient and effective web development.

In most cases, external CSS should be your go-to approach, especially for larger and more complex projects.

#### Width & Height

In CSS, the `width` and `height` properties are used to control the dimensions of elements on a webpage.

These properties can be defined in different units such as pixels (`px`), percentages (`%`), viewport units (`vw`, `vh`), and more.

The `width` property specifies the width of an element. If you do not specify a width, then the default is set to `auto`. This means the element will take up the full width of its parent container.

The `height` property specifies the height of an element. Similarly, the height is `auto` by default, which means it will adjust to the content inside.

Here's an example using the `width` and `height` properties:

```html
<head>
  <style>
    .box {
      width: 100px;
      height: 100px;
      background-color: skyblue
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
```

In this example, we have a `div` element with class named `box`. This element will be occupying `100px` in height and width, whereas the background color will be `skyblue`.

Pixels are a fixed-size unit of measurement in CSS, providing precise control over dimensions.

The `min-width` property specifies the minimum width an element can be. Even if the content inside is smaller, the element won’t shrink below this value.

The `min-height` specifies the minimum height an element can be. It ensures that the element does not become shorter than the set value.

Here is an example:

```html
<head>
  <style>
    .box {
      width: 50px;
      min-width: 100px;
      height: 50px;
      min-height: 100px;
      background-color: lightcoral;
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
```

The above example demonstrates how `min-width` and `min-height` work.

Even though the box has its `width` and `height` set to `50px`, it will actually be `100px` by `100px`. This is because the `min-width` and `min-height` are set to `100px`, which are larger than the specified width and height.

Remember, if `min-width` or `min-height` are larger than the `width` or `height`, they will override the smaller values. This ensures that elements don't become too small, which is important for maintaining a consistent and usable design.

The `max-width` specifies the maximum width an element can grow to, even if there is enough space for it to be wider.

The `max-height` specifies the maximum height an element can grow to, regardless of the content size.

Here is an example:

```html
<head>
  <style>
    .box {
      width: 200px;
      max-width: 150px;
      height: 200px;
      max-height: 150px;
      background-color: lightgreen;
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
```

The above example demonstrates how `max-width` and `max-height` override `width` and `height`. Even though the box is set to `200px` by `200px`, it will actually be `150px` by `150px`. This is because the `max-width` and `max-height` are set to `150px`, which is smaller.

Remember, when `max-width` or `max-height` are smaller than `width` or `height`, they take precedence. This is important for controlling the maximum size of elements in your layouts.

CSS prioritizes `min-width` and `min-height` over `width` and `height`. `max-width` and `max-height` restrict dimensions if values exceed their limits.

For example, if you set `width` to `600px` and `max-width` to `500px`, the element will be limited to `500px` wide. The `max-width` overrides the wider setting, keeping the element within the specified maximum size.

This ensures elements stay within desired size ranges, regardless of standard `width` and `height` values.

#### CSS Combinators

CSS combinators are used to define the relationship between selectors in CSS. They help in selecting elements based on their relationship to other elements, which allows for more precise and efficient styling.

We will discuss some primary CSS combinators and their use cases, starting with the descendant combinator.

A descendant combinator is used to target elements matched by the second selector if they are nested within an ancestor element that matches the first selector. An ancestor can be a parent element or a parent's parent.

To better understand how this works, let's take a look at an example.

```html
<link rel="stylesheet" href="styles.css">

<figure>
  <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="Relaxing Cat">
  <figcaption>A relaxing cat with a border</figcaption>
</figure>
```

```css
figure img {
  border: 4px solid red;
}
```

In the above example, we use the descendant combinator to select all image elements inside figure elements and apply a solid red border on all four sides.

Note that a `space` is used between the parent and child selector.

In this case, the `figure` would be the parent and the img would be the child.

If you had multiple images inside a `figure` element, using the descendant combinator would be a good way to apply a solid black border around each of those images.

Another type of combinator would be the child combinator.

The child combinator (`>`) in CSS is used to select elements that are direct children of a specified parent element.

This combinator targets only elements with a specific parent, making your CSS rules more precise and preventing unintended styling of deeper nested elements.

Let's take a look at the following HTML example:

```html
<div class="container">
  <p>First</p>
  <div>
    <p>Second</p>
  </div>
  <div>
    <p>Third</p>
  </div>
</div>
```

In above HTML structure, the `container` class is applied to a `div` element.

Inside this container, there is a direct child `p` element ("First"), followed by two additional `div` elements, each containing a `p` element ("Second" and "Third").

The first `p` element is a direct child of the `.container` element, while the other two `p` elements are nested inside other `div` elements, making them deeper descendants.

To apply styles to just the direct child of the `container` class, you can use the child combinator like this:

```html
<link rel="stylesheet" href="styles.css">

<div class="container">
  <p>First</p>
  <div>
    <p>Second</p>
  </div>
  <div>
    <p>Third</p>
  </div>
</div>
```

---

```css
.container > p {
  color: blue;
}
```

In the above example, we are only targeting the direct child of `container` class. This will give the direct child the text color of blue.

Because the other two paragraph elements are nested inside `div` elements, they are not considered direct children of the container class and will not get the text color of blue.

Another common combinator would be the next-sibling combinator.

The next-sibling combinator (`+`) in CSS selects an element that immediately follows a specified sibling element. This combinator is useful when you want to apply styles to an element that directly follows another element, allowing for targeted styling based on the element's position relative to its siblings.

Let's take a look at the following HTML example:

```html
<figure>
  <img
    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
    alt="A cute orange cat lying on its back."
  />
  <figcaption>A cute orange cat lying on its back.</figcaption>
</figure>
```

Here, we have a `figure` element containing an `img` element followed by a `figcaption` element. The `figcaption` element is the immediate sibling of the `img` element.

If you wanted to apply a black border around the `figcaption` element, you can use the next-sibling combinator like this:

```html
<link rel="stylesheet" href="styles.css">

<figure>
  <img
    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
    alt="A cute orange cat lying on its back."
  />
  <figcaption>A cute orange cat lying on its back.</figcaption>
</figure>
```

---

```css
img + figcaption {
  border: 4px solid black;
}
```

In this example, the next-sibling combinator (`+`) selects the `figcaption` element that immediately follows the `img` element. The applied CSS rule adds a `4px` `solid` `black` `border` around the `figcaption`.

Another common combinator is the subsequent-sibling combinator.

The subsequent-sibling combinator (`~`) in CSS selects all siblings of a specified element that come after it.

Unlike the next-sibling combinator, which targets only the immediately following sibling, the subsequent-sibling combinator (`~`) can target any siblings that follow the specified element, offering greater flexibility in styling.

Let's take a look at the following HTML example:

```html
<div class="container">
  <h2>Subheading</h2>
  <p>First paragraph.</p>
  <p>Second paragraph.</p>
  <p>Third paragraph.</p>
  <p>Another paragraph element</p>
</div>
```

In this HTML structure, we have an `h2` element followed by four paragraph elements. The paragraph elements are siblings of the `h2` element.

If you want to style all of the paragraph elements that come after the `h2` element, then you can use the subsequent-sibling combinator like this:

```html
<link rel="stylesheet" href="styles.css">

<div class="container">
  <h2>Subheading</h2>
  <p>First paragraph.</p>
  <p>Second paragraph.</p>
  <p>Third paragraph.</p>
  <p>Another paragraph element</p>
</div>
```

---

```css
h2 ~ p {
  color: green;
}
```

In this example, all paragraph elements following the `h2` element will have the text color green.

The subsequent-sibling combinator (`~`) targets all paragraph siblings that appear after the `h2` element, regardless of whether they are immediate siblings.

In conclusion, understanding and using various CSS combinators allows you to apply precise styles to your HTML elements, enhancing the control and flexibility of your design.

By mastering these selectors, you can create more sophisticated and targeted styling rules that improve both the appearance and functionality of your web pages.

#### Inline and Block-Level Elements

In HTML and CSS, elements are classified as either inline elements or block-level elements, and this classification dictates how they behave in the document layout.

Understanding this difference is crucial for controlling how your content is displayed on a webpage.

Block-level elements are elements that take up the full width available to them by default, stretching across the width of their container.

These elements always start on a new line and push other content to the next line, creating a "block" of content.

Block-level elements have the CSS property `display: block;` applied by default. This property ensures that the element stretches to fill the container's width and appears on a new line.

Some common block-level elements are `div` elements, paragraphs, headings, ordered lists, unordered lists, and section elements.

Here is a code example of a block-level element:

```html
<p style="border: 2px solid red;">
  First paragraph
</p>
<p>Second paragraph</p>
```

In this example, we have two paragraph elements where the first one has a red border around it.

The two paragraph elements do not share the same line because they are block level elements by default.

So, both paragraph elements will take up the full width of its container, which in this case is the `body` element.

Block-level elements are ideal when you want content to stack vertically, such as paragraphs, sections, or larger blocks of content. They're commonly used to define the layout and structure of a webpage.

Inline elements, unlike block-level elements, only take up as much width as they need and do not start on a new line. These elements flow within the content, allowing text and other inline elements to appear alongside them.

Inline elements have the CSS property `display: inline;` applied by default. This property ensures that the element remains within the flow of the content and does not break onto a new line.

Common inline elements are `span`, `anchor`, and `img` elements.

Here's an example to better understand inline elements:

```html
<p>This is a
  <span style="color: red; border: 2px solid green;">red</span>
  word inside a paragraph.
</p>
```

In this example, we have a `span` element nested inside of a paragraph element. The `span` element has a `red` text color with a `green` border around it so you can see the highlighted word better.

As you can see, the `span` element only takes up as much space as the word "red" and does not push the following content to a new line.

Inline elements are best used for styling smaller portions of text or content within a line, such as emphasizing a word, creating hyperlinks, or applying specific styles to parts of a paragraph.

#### Inline-Block

When working with CSS, you often encounter three different types of display behaviors for elements: `inline`, `block`, and `inline-block`.

Each of these properties affects how elements are positioned and how they interact with other elements on the page.

In this lesson, we will focus on how the `inline-block` property works and how it differs from both inline and block-level elements.

Block-level elements behave like large containers or "blocks" that take up the full width of their parent container. They always start on a new line, and their height and width can be adjusted.

Inline elements only take up as much space as they need. They flow within the surrounding content and do not break onto a new line.

The `inline-block` property is a hybrid of these two behaviors. Like `inline` elements, `inline-block` elements remain in the text flow without starting on a new line.

However, unlike `inline` elements, you can adjust the width and height of an `inline-block` element, just as you would with block-level elements.

In short, the key difference between `inline` and `inline-block` is that `inline` elements cannot have their size controlled, whereas `inline-block` elements allow for full control over dimensions while still staying inline with other content.

Let's take a look at an example.

```html
<link href="styles.css" rel="stylesheet">

<div class="container">
  <span class="inline-block-element element1">Inline-Block Element 1</span>
  <span class="inline-block-element element2">Inline-Block Element 2</span>
</div>
```

---

```css
.inline-block-element {
  display: inline-block;
  width: 150px;
  height: 100px;
}

.element1 {
  background-color: lightblue;
}

.element2 {
  background-color: lightgreen;
}
```

In the above example, we have a `div` with a class of `container`. Inside that `div` element, we have two `span` elements.

Each of the span elements is set to `display:inline-block` and has a width and height set as well.

The inline-block elements will appear side by side because they behave like inline elements, but they also have a specified width and height, which gives them block-like properties.

But, if you remove the `display: inline-block` property, neither the `height` nor the `width` will be applied even though you defined it clearly.

Here is the revised CSS:

```html
<link href="styles.css" rel="stylesheet">

<div class="container">
  <span class="inline-block-element element1">Inline-Block Element 1</span>
  <span class="inline-block-element element2">Inline-Block Element 2</span>
</div>
```

---

```css
.inline-block-element {
  width: 150px;
  height: 100px;
}

.element1 {
  background-color: lightblue;
}

.element2 {
  background-color: lightgreen;
}
```

In this code, we removed the `display: inline-block;` property but kept everything else intact. Here, the sp`an elements revert to their default behavior as inline elements.

As a result, the specified width and height are ignored, and the elements only take up the space needed for their content.

Understanding how `inline-block` works is useful because you can use it for creating layouts that require both alignment and dimension control within a continuous text flow.

#### Margins and Padding



---

[Back to Top](#table-of-contents)

---

## References

*Certified Full Stack Developer Curriculum*. freecodecamp.org. (n.d.). <https://www.freecodecamp.org/learn/full-stack-developer/>
