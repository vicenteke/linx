import { FC } from "react";

import {
  WiCloudy,
  WiDaySunny,
  WiDust,
  WiRain,
  WiSnow,
  WiStormShowers,
} from "react-icons/wi";
import { IconBaseProps } from "react-icons";


interface Props extends IconBaseProps {
  condition: string;
};


const WeatherIcon: FC<Props> = ({
  condition,
  ...props
}: Props) => {
  if (condition.includes('snow') || condition.includes('sleet'))
    return <WiSnow {...props} />;

  if (condition.includes('clear'))
    return <WiDaySunny {...props} />;

  if (condition.includes('thunderstorm'))
    return <WiStormShowers {...props} />;

  if (condition.includes('rain') || condition.includes('drizzle'))
    return <WiRain {...props} />;

  if (condition.includes('cloud'))
    return <WiCloudy {...props} />;

  return <WiDust {...props} />;
};

export default WeatherIcon;
