import { Box } from "@mantine/core";
import { useContext } from "react";
import Anchor from "./Anchor";
import { Context } from "../contexts/SettingsContextProvider";
import actions from "../contexts/SettingsActions";

const Settings = () => {
  const { state, dispatch } = useContext(Context);
  return (
    <Box sx={{ paddingLeft: "300px" }}>
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          alignItems: "center",
        }}
      >
        <Anchor
          clickCb={() => {
            dispatch({
              type: actions.TOGGLE_PUNCTUATION,
            });
          }}
          isChecked={state.includePunctuation}
          title={"punctuation"}
        ></Anchor>
        <Anchor
          clickCb={() => {
            dispatch({
              type: actions.TOGGLE_NUMBERS,
            });
          }}
          isChecked={state.includeNumbers}
          title={"numbers"}
        ></Anchor>
      </Box>
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          alignItems: "center",
        }}
      >
        <Anchor
          clickCb={() => {
            dispatch({
              type: actions.SET_MODE,
              payload: { type: "time" },
            });
          }}
          isChecked={state.mode.type === "time"}
          title={"time"}
        ></Anchor>
        <Anchor
          clickCb={() => {
            dispatch({
              type: actions.SET_MODE,
              payload: { type: "words" },
            });
          }}
          isChecked={state.mode.type === "words"}
          title={"words"}
        ></Anchor>
        <Anchor
          clickCb={() => {
            dispatch({
              type: actions.SET_MODE,
              payload: { type: "quote" },
            });
          }}
          isChecked={state.mode.type === "quote"}
          title={"quote"}
        ></Anchor>
      </Box>
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          alignItems: "center",
        }}
      >
        <Anchor
          clickCb={() => {
            dispatch({
              type: actions.SET_SECONDS,
              payload: { seconds: 15 },
            });
          }}
          isChecked={state.mode.seconds === 15}
          title={15}
        ></Anchor>
        <Anchor
          clickCb={() => {
            dispatch({
              type: actions.SET_SECONDS,
              payload: { seconds: 30 },
            });
          }}
          isChecked={state.mode.seconds === 30}
          title={30}
        ></Anchor>
        <Anchor
          clickCb={() => {
            dispatch({
              type: actions.SET_SECONDS,
              payload: { seconds: 60 },
            });
          }}
          isChecked={state.mode.seconds === 60}
          title={60}
        ></Anchor>
        <Anchor
          clickCb={() => {
            dispatch({
              type: actions.SET_SECONDS,
              payload: { seconds: 120 },
            });
          }}
          isChecked={state.mode.seconds === 120}
          title={120}
        ></Anchor>
      </Box>
    </Box>
  );
};

export default Settings;

