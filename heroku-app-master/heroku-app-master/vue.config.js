module.exports = {
  publicPath: '/',
  outputDir: './vue/static',
  filenameHashing: false,
  chainWebpack: (config) => {
    // Eject the webpack.config.js to determine what keys to delete
    config.plugins.delete('prefetch');
    config.plugins.delete('splitVendor');
    config.optimization.delete('splitChunks');
  },
  configureWebpack: {
    entry: {
      app: './vue/src/main.js',
    },
    optimization: {
      splitChunks: false,
    },
  },
};
