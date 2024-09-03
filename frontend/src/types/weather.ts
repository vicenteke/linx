interface Forecast {
  city: string;
  forecast_date: string;
  temperature: number;
  wind: number;
  cloudiness: string;
  pressure: number;
  humidity: number;
  sunrise: number;
  sunset: number;
  latitude: number;
  longitude: number;
};


interface ForecastContext {
  activeEntryIndex: number;
  entries: Forecast[];
  loading: boolean;
  search: string;
  fetchForecasts: () => void;
  setActiveEntryIndex: (val: number) => void;
  setEntries: (val: Forecast[]) => void;
  setLoading: (val: boolean) => void;
  setSearch: (val: string) => void;
};


export type {
  Forecast,
  ForecastContext,
};
