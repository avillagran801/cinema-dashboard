import { Box } from '@mui/material';
import CircularProgress from '@mui/material/CircularProgress';

export default function Loading() {
  return(
    <Box sx={{
      display: "flex",
      flexDirection: "column",
      flex: 1,
      justifyContent: "center",
      alignItems: "center",
      gap: "1.5rem"
    }}>
      <CircularProgress />
      <Box>
        Cargando datos...
      </Box>
    </Box>
  )
}