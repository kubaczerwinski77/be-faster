import { AppShell, Box, Text } from "@mantine/core";
import Footer from "./Footer";
import Header from "./Header";

const Shell = () => {
  return (
    <AppShell
      header={<Header />}
      footer={<Footer />}
      sx={(theme) => ({
        backgroundColor: theme.colors.dark,
      })}
    >
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "77vh",
        }}
      >
        <Text
          sx={(theme) => ({ color: theme.colors.claret, fontSize: "80px" })}
        >
          Main content
        </Text>
      </Box>
    </AppShell>
  );
};

export default Shell;

