import React from "react";
import { Header as MantineHeader, Box } from "@mantine/core";
import { BsKeyboard } from "react-icons/bs";
import { TbCrown } from "react-icons/tb";
import { CgProfile } from "react-icons/cg";
import Logo from "./Logo.jsx";
import Settings from "./Settings.jsx";

const Header = () => {
  return (
    <MantineHeader p="md" height={100}>
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Logo />
        <Box sx={{ display: "flex", alignItems: "center", padding: "0 15px" }}>
          <BsKeyboard color="#D8E9A8" size={40} />
        </Box>
        <Box sx={{ display: "flex", alignItems: "center", padding: "0 15px" }}>
          <TbCrown color="#D8E9A8" size={40} />
        </Box>
        <Box sx={{ display: "flex", alignItems: "center", padding: "0 15px" }}>
          <CgProfile color="#D8E9A8" size={32} />
        </Box>
        <Settings />
      </Box>
    </MantineHeader>
  );
};

export default Header;

