import { createContext, useReducer } from "react";
import actions from "./SettingsActions";

export const Context = createContext();

const initialState = {
  includePunctuation: false,
  includeNumbers: false,
  mode: {
    type: "words",
    seconds: 30,
  },
};

const { TOGGLE_NUMBERS, TOGGLE_PUNCTUATION, SET_MODE, SET_SECONDS } = actions;

const reducer = (state, action) => {
  switch (action.type) {
    case TOGGLE_NUMBERS:
      return Object.assign({}, state, {
        includeNumbers: !state.includeNumbers,
      });
    case TOGGLE_PUNCTUATION:
      return Object.assign({}, state, {
        includePunctuation: !state.includePunctuation,
      });
    case SET_MODE:
      return Object.assign({}, state, {
        mode: Object.assign({}, state.mode, { type: action.payload.type }),
      });
    case SET_SECONDS:
      return Object.assign({}, state, {
        mode: Object.assign({}, state.mode, {
          seconds: action.payload.seconds,
        }),
      });
    default:
      return state;
  }
};

const SettingsContextProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <Context.Provider value={{ state, dispatch }}>{children}</Context.Provider>
  );
};

export default SettingsContextProvider;

