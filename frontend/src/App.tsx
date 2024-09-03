import {
  Box,
  ChakraProvider,
  Stack,
} from "@chakra-ui/react";
import theme from "./theme";
import { ForecastsProvider } from "./hooks/forecasts";
import SearchInput from "./components/SearchInput";
import Forecasts from "./components/Forecasts";
import WeatherCard from "./components/WeatherCard";


export const App = () => (
  <ChakraProvider theme={theme}>
    <ForecastsProvider>
      <Box
        display='flex'
        flexDirection={{ base: 'column', md: 'row' }}
        minHeight='100vh'
        minWidth='100vw'
        justifyContent='space-between'
        padding='10px'
      >
        <Stack spacing={10} padding='70px' minWidth='1050px'>
          <SearchInput />
          <Forecasts />
        </Stack>
        <WeatherCard />
      </Box>
    </ForecastsProvider>
  </ChakraProvider>
)
