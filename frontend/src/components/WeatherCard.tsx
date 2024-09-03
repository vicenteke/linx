import { FC } from "react";
import {
  Card,
  CardBody,
  CardHeader,
  Stack,
  Text,
} from "@chakra-ui/react";

import WeatherIcon from "./WeatherIcon";
import WeatherCardTemperature from "./WeatherCardTemperature";
import WeatherCardData from "./WeatherCardData";

import useForecasts from "../hooks/forecasts";
import { ACCENT_COLOR } from "../theme";


const WeatherCard: FC = () => {
  const { entries, activeEntryIndex } = useForecasts();
  if (!entries || entries.length === 0) return <></>;

  const entry = entries[activeEntryIndex];
  const weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
  const dayOfWeek = new Date(entry.forecast_date).getDay();

  return <Card width='500px' borderRadius='20px' padding='10px'>
    <CardHeader display='flex' flexDirection='row' justifyContent='space-between'>
      <Stack>
        <Text fontSize='3xl'>
          {new Date() === new Date(entry.forecast_date) ? 'Today' : weekdays[dayOfWeek]}
        </Text>
        <Text fontSize='3xl' fontWeight='semibold'>{entry.city}</Text>
      </Stack>
      <WeatherIcon condition={entry.cloudiness} color={ACCENT_COLOR} size='100'/>
    </CardHeader>
    <CardBody>
      <WeatherCardTemperature accentColor={ACCENT_COLOR} entry={entry} />
      <WeatherCardData entry={entry} />
    </CardBody>
  </Card>;
};

export default WeatherCard;
