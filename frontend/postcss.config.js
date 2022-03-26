// const purgecss = require("@fullhuman/postcss-purgecss");

// const plugins = [];

// if (process.env.NODE_ENV === "production") {
//     plugins.push(
//         purgecss({
//             content: ['./**/*.html'],
//             safelist: {
//                 standard: [/red$/],
//                 deep: [/is$/, /hero$/, /has$/, /column$/, /container$/, /button$/, /hero$/,
//                  /section$/, /carousel$/, /navbar$/, /navbar-item$/, /section$/, /panel$/,
//                  /pt$/, /mt$/, /has-navbar$/
//                 ]
//             },
//             whitelistPatterns: [/^navbar-/, /^panel/, /^has-text-/, /^has-/, /^fa-/, /^has-numberinput-/],
//             whitelistPatternsChildren: [/^token/, /^pre/, /^code/],
//         })
//     );
// }

// module.exports = { plugins };

const purgecss = require("@fullhuman/postcss-purgecss");

const plugins = [];

if (process.env.NODE_ENV === "production") {
    plugins.push(
        purgecss({
            content: [
              "./src/**/*.html", 
              "./src/**/*.vue",
              "./src/**/*.js",
              "./node_modules/buefy/**/*.vue",
              "./node_modules/buefy/**/*.js",
              "./node_modules/buefy/**/*.scss",
            ],
            safelist: {
                standard: ['navbar-start', 'navbar-end', 'animation-content',
                 'enter-active-class', 'leave-active-class', 'carousel-item', 'fade-out', 'fade-in'],
                deep: [/fade$/, /zoom$/, /slide$/]
            }
        })
    )
}

module.exports = { plugins };