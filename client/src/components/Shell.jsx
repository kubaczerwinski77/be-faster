import { AppShell } from "@mantine/core";
import Header from "./Header";

const Shell = () => {
  return (
    <AppShell
      header={<Header />}
      sx={(theme) => ({
        backgroundColor: theme.colors.dark,
      })}
    >
      Main content
    </AppShell>
  );
};

export default Shell;

