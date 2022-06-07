import { Box } from "@mantine/core";
import Anchor from "./Anchor";

const Settings = () => {
  return (
    <Box sx={{ paddingLeft: "300px" }}>
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          alignItems: "center",
        }}
      >
        <Anchor text={"punctuation"}></Anchor>
        <Anchor text={"numbers"}></Anchor>
      </Box>
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          alignItems: "center",
        }}
      >
        <Anchor text={"time"}></Anchor>
        <Anchor text={"words"}></Anchor>
        <Anchor text={"quote"}></Anchor>
      </Box>
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          alignItems: "center",
        }}
      >
        <Anchor text={"15"}></Anchor>
        <Anchor text={"30"}></Anchor>
        <Anchor text={"60"}></Anchor>
        <Anchor text={"120"}></Anchor>
      </Box>
    </Box>
  );
};

export default Settings;

