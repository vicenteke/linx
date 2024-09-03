import { FC } from "react";
import {
  Box,
  Text,
  Wrap,
  WrapItem,
} from "@chakra-ui/react";
import ForecastItem from "./ForecastItem";

import useForecasts from "../hooks/forecasts";


const Forecasts: FC = () => {
  const { entries, setActiveEntryIndex, activeEntryIndex } = useForecasts();
  if (!entries || entries.length === 0) return <></>;

  return <Box display='flex' flexDirection='column'>
    <Text fontWeight='semibold' marginBottom='10px'>
      Weekly forecast:
    </Text>
    <Wrap spacing='30px'>
      {entries.map((entry, index) => <WrapItem key={index}>
        <ForecastItem
          cloudiness={entry.cloudiness}
          wind={entry.wind}
          temperature={entry.temperature}
          humidity={entry.humidity}
          date={entry.forecast_date}
          onClick={() => setActiveEntryIndex(index)}
          isActive={index === activeEntryIndex}
        />
      </WrapItem>)}
    </Wrap>
  </Box>
};

export default Forecasts;
