import { FC } from "react";
import {
  Box,
  Stack,
  Text,
} from "@chakra-ui/react";

import WeatherIcon from "./WeatherIcon";


interface Props {
  cloudiness: string;
  date: string;
  humidity: number;
  isActive?: boolean;
  onClick: () => void;
  temperature: number;
  wind: number;
};


const ForecastItem: FC<Props> = (params: Props) => {
  const weekdays = ["SUN","MON","TUE","WED","THU","FRI","SAT"];
  const dayOfWeek = new Date(params.date).getDay();

  return <Box
    border='1px solid #8c6da3'
    borderRadius='20px'
    width='160px'
    cursor={params.isActive ? 'default' : 'pointer'}
    display='flex'
    flexDirection='column'
    padding='20px'
    paddingBottom='0'
    bg={params.isActive ? '#6A4981' : 'transparent'}
    _hover={params.isActive ? {} : {
      border: '1px solid transparent',
      bg: '#6A4981',
      boxShadow: '0 0 15px 2px #6A4981',
    }}
    onClick={params.onClick}
  >
    <Box
      display='flex'
      justifyContent='space-between'
      width='100%'
      marginBottom='30px'
    >
      <WeatherIcon condition={params.cloudiness} size='50' />
      <Text fontSize='sm'>{weekdays[dayOfWeek]}</Text>
    </Box>
    <Stack justifyContent='flex-start' spacing={0} paddingLeft='10px'>
      <Text fontSize='lg' fontWeight='semibold'>{params.temperature.toFixed(1)} °C</Text>
      <Text>{params.wind} m/s</Text>
      <Text>Humidity: {params.humidity}%</Text>
    </Stack>
    <Box
      height='2px'
      bgGradient='linear(to-r, yellow, red)'
      width={params.temperature * 3}
      maxWidth={120}
      marginTop='20px'
      marginBottom='-2px'
      borderRadius='1px'
    />
  </Box>;
};

export default ForecastItem;
