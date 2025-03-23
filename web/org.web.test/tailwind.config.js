/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './apps/**/*.{html,ts}', // Angular 앱의 경로에 맞게 수정
    './libs/**/*.{html,ts}',  // Nx 라이브러리 모듈 경로에 맞게 수정
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

