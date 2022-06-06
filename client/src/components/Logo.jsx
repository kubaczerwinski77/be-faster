import React from "react";
import { Title, Text } from "@mantine/core";

const Logo = () => {
  return (
    <Title
      sx={(theme) => ({
        fontSize: "50px",
        color: theme.colors.claret,
        padding: "10px 30px",
        letterSpacing: "2px",
      })}
      order={3}
    >
      be
      <Text
        sx={(theme) => ({
          color: theme.colors.red,
        })}
        inherit
        component="span"
      >
        faster
      </Text>
    </Title>
  );
};

export default Logo;

