/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './main/templates/main/parts/*.html',
    './main/templates/main/views/*.html',
  ],
  theme: {
    extend: {
      width: {
        '500': '40rem',
        '550': '550px',
        '600': '600px',
        '700' : '700px',
        '130': '130px',
        '10xl' : '800px',
        '84' : '22rem',
      },
      maxWidth : {
        '10xl' : '800px',
      },
      minWidth : {
        '10xl' : '800px',
        '84' : '22rem',
      },
    },
  },
  plugins: [],
}

