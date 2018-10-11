Because this package uses [Transcrypt](http://www.transcrypt.org/) to transpile Python to JavaScript, browser support depends on the version of Transcrypt installed in your project.

Currently this package supports Transcrypt versions 3.6 and 3.7, which transpile Python code into different versions of JavaScript:

| Transcrypt Version | JavaScript Version | Browser Support |
| ------------------ | ------------------ | --------------- |
| 3.6                | ES5                | 100%            |
| 3.7                | ES6                | [>75%](https://caniuse.com/#feat=es6-module) |


!!! note
    This plugin will respect whether you have Transcrypt 3.6 or 3.7 installed, so you can choose whether to generate newer or better-supported JavaScript by specifying the Transcrypt version in your project's requirements.
