import React from "react";
import { Anchor as MantineAnchor } from "@mantine/core";

const Anchor = ({ text }) => {
  return (
    <MantineAnchor
      sx={(theme) => ({
        color: "#D8E9A8",
        "&:hover": {
          color: "#4E9F3D",
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

