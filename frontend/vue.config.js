const webpack = require('webpack');

module.exports = {
    configureWebpack: {
        plugins: [
            new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/) // Ignore all locale files of moment.js
        ]
    }
    
};