import { extendTheme } from "@chakra-ui/react";

const theme = extendTheme({
  styles: {
    global: {
      body: {
        bgGradient: "linear(to-br, #674480, #482561)",
        color: "white",
        fontFamily: "Roboto, sans-serif",
        fontWeight: 'light',
      },
    },
  },
});

export default theme;
export const ACCENT_COLOR = '#735488';
