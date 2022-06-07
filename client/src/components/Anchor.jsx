import React from "react";
import { Anchor as MantineAnchor } from "@mantine/core";

const Anchor = ({ title, isChecked, clickCb }) => {
  return (
    <MantineAnchor
      sx={(theme) => ({
        color: isChecked ? theme.colors.red : theme.colors.claret,
        "&:hover": {
          color: theme.colors.red,
          textDecoration: "none",
          fontWeight: "bold",
        },
        paddingLeft: "5px",
      })}
      onClick={clickCb}
    >
      {title}
    </MantineAnchor>
  );
};

export default Anchor;

