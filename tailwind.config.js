/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './main/templates/main/parts/*.html',
    './main/templates/main/views/*.html',
  ],
  theme: {
    extend: {
      width: {
        '500': '500px',
        '550': '550px',
        '600': '600px',
        '700' : '700px',
        '130': '130px',

      },
    },
  },
  plugins: [],
}

