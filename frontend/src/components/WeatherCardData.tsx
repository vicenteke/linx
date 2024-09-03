import { FC } from "react";
import { Stack } from "@chakra-ui/react";

import WeatherCardDataRow from "./WeatherCardDataRow";
import { Forecast } from "../types/weather";


interface Props {
  entry: Forecast;
};


const WeatherCardData: FC<Props> = (params: Props) => {
  const timestampToTimeString = (timestamp: number) => {
    const date = new Date(timestamp);
    const hours = `${date.getHours()}`.padStart(2, '0');
    const minutes = `${date.getMinutes()}`.padStart(2, '0');
    return `${hours}:${minutes}`;
  };

  return <Stack paddingX='5px'>
    <WeatherCardDataRow
      title='Wind'
      value={`${params.entry.wind} m/s`}
    />
    <WeatherCardDataRow
      title='Cloudiness'
      value={params.entry.cloudiness}
    />
    <WeatherCardDataRow
      title='Pressure'
      value={`${params.entry.pressure} hpa`}
    />
    <WeatherCardDataRow
      title='Humidity'
      value={`${params.entry.humidity}%`}
    />
    <WeatherCardDataRow
      title='Sunrise'
      value={timestampToTimeString(params.entry.sunrise * 1000)}
    />
    <WeatherCardDataRow
      title='Sunset'
      value={timestampToTimeString(params.entry.sunset * 1000)}
    />
    <WeatherCardDataRow
      title='Geo coords'
      value={`[${params.entry.latitude}, ${params.entry.longitude}]`}
    />
  </Stack>
};

export default WeatherCardData;
