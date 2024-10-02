module.exports = {
  content: [
    './templates/**/*.html',      // All template files
    './static/**/*.js',           // All JS files in the static folder
    '!./node_modules/**',         // Exclude node_modules
    'node_modules/flowbite/**/*.js',  // Include Flowbite components
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')     // Use the Flowbite plugin
  ],
}
