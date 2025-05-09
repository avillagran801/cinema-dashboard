import { Box, Typography } from "@mui/material";
import { Limelight } from "next/font/google";

const limelight = Limelight({
  weight: "400",
  subsets: ["latin"],
});

export default function Header() {
  return(
    <>
      <Box
        sx={{
          position: "relative",
          padding: "2rem",
          overflow: "hidden",
          background: 'linear-gradient(45deg, #1a1a1a 30%, #2d2d2d 90%)',

          "&::after": {
            content: '""',
            position: "absolute",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            backgroundImage: `
              repeating-radial-gradient(
                0deg,
                rgba(255,255,255,0.1) 0px,
                rgba(255,255,255,0.1) 1px,
                transparent 1px,
                transparent 3px
              )
            `,
            opacity: 0.5,
            pointerEvents: "none",
            zIndex: 1,
          },
        }}
      >
        <Box
          sx={{
            border: '2px solid #fff',
            padding: "1.5rem"
          }}
        >
          <Typography
            variant="h2"
            className={limelight.className}
            sx={{
              textAlign: "center",    
              color: "#fff",
              fontFamily: limelight.style.fontFamily,
              fontSize: { xs: "2rem", md: "3.5rem" },
              textTransform: "uppercase",
              letterSpacing: "0.2em",
            }}
          >
            El cine en números
          </Typography>
        </Box>
      </Box> 
    </>
  )
}