import { Box, Footer as MantineFooter } from "@mantine/core";
import Anchor from "./Anchor";
import { RiContactsLine } from "react-icons/ri";
import { BsCodeSlash } from "react-icons/bs";
import { BiDonateHeart } from "react-icons/bi";
import { MdOutlinePrivacyTip, MdOutlineSecurity } from "react-icons/md";

const Footer = () => {
  return (
    <MantineFooter height={80} p={"md"}>
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-around",
          alignItems: "center",
        }}
      >
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              padding: "0 30px 0 100px",
            }}
          >
            <RiContactsLine color="#D8E9A8" />
            <Anchor text={"Contact"} />
          </Box>
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              padding: "0 30px",
            }}
          >
            <BsCodeSlash color="#D8E9A8" />
            <Anchor text={"Github"} />
          </Box>
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              padding: "0 30px",
            }}
          >
            <MdOutlinePrivacyTip color="#D8E9A8" />
            <Anchor text={"Privacy"} />
          </Box>
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              padding: "0 30px",
            }}
          >
            <MdOutlineSecurity color="#D8E9A8" />
            <Anchor text={"Security"} />
          </Box>
        </Box>
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              paddingRight: "100px",
            }}
          >
            <BiDonateHeart color="#D8E9A8" />
            <Anchor text={"Buy me a coffee"} />
          </Box>
        </Box>
      </Box>
    </MantineFooter>
  );
};

export default Footer;

