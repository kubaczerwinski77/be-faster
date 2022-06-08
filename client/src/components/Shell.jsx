import { AppShell } from "@mantine/core";
import Footer from "./Footer";
import Header from "./Header";
import TypeTest from "./TypeTest";
import { Routes, Route } from "react-router-dom";

const Shell = () => {
  return (
    <AppShell
      header={<Header />}
      footer={<Footer />}
      sx={(theme) => ({
        backgroundColor: theme.colors.dark,
        border: "none",
        overflow: "hidden",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
      })}
      styles={(theme) => ({
        body: { flexGrow: "2", backgroundColor: theme.colors.dark },
        main: {
          display: "flex",
          backgroundColor: theme.colors.dark,
          padding: 0,
        },
      })}
    >
      <Routes>
        <Route path="/account" element={"Account"} />
        <Route path="/leaderboard" element={"Leaderboard"} />
        <Route path="/*" element={<TypeTest />} />
      </Routes>
    </AppShell>
  );
};

export default Shell;

