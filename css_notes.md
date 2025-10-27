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

---

[Back to Top](#table-of-contents)

---

## References

*Certified Full Stack Developer Curriculum*. freecodecamp.org. (n.d.). <https://www.freecodecamp.org/learn/full-stack-developer/>
