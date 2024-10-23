/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/socialproject/templates/**/*.html",
    "./users/templates/**/*.html", // Add this line if your templates are here
    "./templates/**/*.html", // Add this if there are other templates
  ],

  theme: {
    extend: {},
  },
  plugins: [],
};
