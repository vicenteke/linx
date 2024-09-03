import { FC } from "react";
import {
  Box,
  Text,
} from "@chakra-ui/react";
import { ACCENT_COLOR } from "../theme";


interface Props {
  title: string;
  value: string | number;
};


const WeatherCardDataRow: FC<Props> = (params: Props) => {
  return <Box
    key={params.title}
    display='flex'
    justifyContent='space-between'
  >
    <Text color={ACCENT_COLOR} fontWeight='semibold'>{params.title}</Text>
    <Text color='#555'>{params.value}</Text>
  </Box>
};

export default WeatherCardDataRow;
