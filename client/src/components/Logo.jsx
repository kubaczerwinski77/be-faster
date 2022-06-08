import React from "react";
import { Title, Text } from "@mantine/core";
import { Link } from "react-router-dom";

const Logo = () => {
  return (
    <Title
      component={Link}
      to={"/"}
      sx={(theme) => ({
        fontSize: "50px",
        color: theme.colors.claret,
        margin: "10px 30px",
        letterSpacing: "2px",
        textDecoration: "none",
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

