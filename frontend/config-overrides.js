const webpack = require('webpack');

module.exports = function override(config) {
  config.resolve.fallback = {
    ...config.resolve.fallback,
    "http": require.resolve("stream-http"),
    "https": require.resolve("https-browserify"),
    "stream": require.resolve("stream-browserify"),
    "url": require.resolve("url"),
    "util": require.resolve("util"),
    "assert": require.resolve("assert"),
    "zlib": require.resolve("browserify-zlib"),
    "buffer": require.resolve("buffer"),
      "process": require.resolve("process/browser"),
      "http2": false, // http2 n'a pas de polyfill navigateur, on le désactive
  };

  config.resolve.alias = {
    ...(config.resolve.alias || {}),
    'process/browser': require.resolve('process/browser.js')
  };

  config.plugins = [
    ...config.plugins,
    new webpack.ProvidePlugin({
      process: 'process/browser',
      Buffer: ['buffer', 'Buffer'],
    }),
  ];

  // Ignorer les warnings de source-map-loader pour les modules node
  config.ignoreWarnings = [/Failed to parse source map/];

  return config;
};
