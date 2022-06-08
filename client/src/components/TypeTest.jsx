import { Box, Button, Text, Textarea } from "@mantine/core";
import React, { useContext, useEffect, useState } from "react";
import { Context } from "../contexts/SettingsContextProvider";
import { BsArrowRepeat } from "react-icons/bs";
import { BiWorld } from "react-icons/bi";

const TypeTest = () => {
  const { state } = useContext(Context);
  const [userInput, setUserInput] = useState("");
  const [isActive, setIsActive] = useState(false);
  const [timer, setTimer] = useState(state.mode.seconds);
  const [finished, setFinished] = useState(false);

  const resetTimer = () => {
    setTimer(state.mode.seconds);
    setIsActive(false);
    setFinished(false);
    setUserInput("");
  };

  const startTimer = () => {
    if (isActive) {
      return;
    }
    setIsActive(true);
  };

  useEffect(() => {
    let interval = null;
    if (isActive && timer === 0) {
      clearInterval(interval);
      setIsActive(false);
      setFinished(true);
      console.log(userInput);
    } else if (isActive) {
      interval = setInterval(() => {
        setTimer((timer) => timer - 1);
      }, 1000);
    }
    return () => {
      clearInterval(interval);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isActive, timer]);

  useEffect(() => {
    resetTimer();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [state]);

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        width: "100%",
      }}
    >
      <Box
        sx={{
          width: "51%",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <Text
          sx={(theme) => ({
            color: theme.colors.claret,
            fontSize: "26px",
            marginBottom: "10px",
            textAlign: "left",
            marginRight: "auto",
          })}
        >
          {timer}
        </Text>
        <BiWorld color="#808080" size={20} />
        <Text color="#808080" sx={{ marginLeft: "6px", letterSpacing: "1px" }}>
          english
        </Text>
      </Box>
      <Box sx={{ width: "50.9%", marginBottom: "1%" }}>
        <Text sx={(theme) => ({ color: theme.colors.red, fontSize: "20px" })}>
          move much must my name near need never new next night no not now
          number of off often oil old on once one only open or other our out
          over own page paper part people picture place plant play point put
          question
        </Text>
      </Box>
      <Textarea
        size={20}
        sx={(theme) => ({
          width: "52%",
          ".mantine-Textarea-input": {
            backgroundColor: "#1e1f1e",
            caretColor: theme.colors.red,
            color: theme.colors.red,
            padding: "1px 10px",
            overflow: "hidden",
          },
        })}
        placeholder="start typing to begin the test..."
        autosize
        minRows={3}
        maxRows={3}
        value={userInput}
        disabled={finished}
        onChange={(event) => {
          startTimer();
          setUserInput(event.currentTarget.value);
        }}
      />
      <Box
        sx={{ display: "flex", justifyContent: "center", alingItems: "center" }}
      >
        <Button
          size="md"
          leftIcon={<BsArrowRepeat color="#808080" size={26} />}
          sx={{
            background: "transparent",
            color: "gray",
            marginTop: "24px",
          }}
          onClick={() => resetTimer()}
        >
          reset
        </Button>
      </Box>
    </Box>
  );
};

export default TypeTest;

