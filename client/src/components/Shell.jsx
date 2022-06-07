import { AppShell, Box, Button } from "@mantine/core";
import { useContext } from "react";
import { Context } from "../contexts/SettingsContextProvider";
import Footer from "./Footer";
import Header from "./Header";

const Shell = () => {
  const { state } = useContext(Context);

  const handleClick = () => {
    console.log(state);
  };
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
        <Button onClick={() => handleClick()}>Check state</Button>
      </Box>
    </AppShell>
  );
};

export default Shell;

