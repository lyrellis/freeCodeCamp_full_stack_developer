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



---

[Back to Top](#table-of-contents)

---

## References

*Certified Full Stack Developer Curriculum*. freecodecamp.org. (n.d.). <https://www.freecodecamp.org/learn/full-stack-developer/>
