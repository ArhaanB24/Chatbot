/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["templates/*.html"],
	theme: {
		extend: {
			colors: {
				text: "#000000",
				background: "#ffffff",
				primary: "#8fb3ff",
				secondary: "#ebf1ff",
				accent: "#ff8f94",
			},
		},
	},
	plugins: [],
};
