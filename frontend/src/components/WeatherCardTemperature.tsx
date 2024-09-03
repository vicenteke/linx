import { FC } from "react";
import {
  Box,
  Text,
} from "@chakra-ui/react";
import { Forecast } from "../types/weather";

interface Props {
  accentColor: string;
  entry: Forecast;
}

const WeatherCardTemperature: FC<Props> = (params: Props) => {
  return <Box
    width='100%'
    aspectRatio='1'
    display='flex'
    alignItems='center'
    justifyContent='center'
    flexDirection='column'
    backgroundImage='url("/images/linx-weather-bg.png")'
    backgroundPosition='bottom'
    backgroundSize='680px'
    backgroundRepeat='no-repeat'
  >
    <Text
      fontSize='90px'
      fontWeight='semibold'
      color='black'
      display='flex'
      alignItems='flex-start'
    >
      {params.entry.temperature.toFixed(0)}
      <span style={{fontSize: '50px'}}>°C</span>
    </Text>
    <Text fontSize='xl' fontWeight='semibold' color={params.accentColor}>
      {params.entry.cloudiness}
    </Text>
    <Text fontSize='md' fontWeight='semibold' color={params.accentColor}>
      {new Date(params.entry.forecast_date).toDateString()}
    </Text>
  </Box>;
};

export default WeatherCardTemperature;
