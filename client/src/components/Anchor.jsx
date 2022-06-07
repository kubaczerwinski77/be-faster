import React from "react";
import { Anchor as MantineAnchor } from "@mantine/core";

const Anchor = ({ text }) => {
  return (
    <MantineAnchor
      sx={(theme) => ({
        color: theme.colors.claret,
        "&:hover": {
          color: theme.colors.red,
          textDecoration: "none",
          fontWeight: "bold",
        },
        paddingLeft: "5px",
      })}
    >
      {text}
    </MantineAnchor>
  );
};

export default Anchor;

