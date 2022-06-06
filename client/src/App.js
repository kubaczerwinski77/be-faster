import { MantineProvider } from "@mantine/core";
import Shell from "./components/Shell";
import "@fontsource/poppins";

function App() {
  return (
    <MantineProvider
      withGlobalStyles
      withNormalizeCSS
      theme={{
        fontFamily: "Poppins, sans-serif",
        headings: { fontFamily: "Poppins, sans-serif" },
        colors: {
          red: "#4E9F3D",
          dark: "#191A19",
          claret: "#D8E9A8",
          livid: "#1E5128",
        },
        primaryColor: "red",
        colorScheme: "dark",
      }}
    >
      <Shell />
    </MantineProvider>
  );
}

export default App;

