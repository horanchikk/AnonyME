const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: "media",
  theme: {
    extend: {
      colors: {
        rred: "#ef313d",
        "rred-50": "#7f1a21",
        "rred-100": "#8f1d24",
        "rred-200": "#bf2730",
        bblack: "#222429",
        wwhite: "#f8fffc",
        "msg-100": "#515861",
        "msg-200": "#33373d",
      },
      animation: {
        pulse: "pulse 3s cubic-bezier(0.4, 0, 0.6, 1);",
      },
    },
  },
  plugins: [],
};
