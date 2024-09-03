import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";


export const getForecasts = async (city: string) => {
  const searchInput = city.replaceAll(' ', '+');
  const response: any = await axios.get(`${API_URL}/forecast/${searchInput}`);

  if (response && response.request) {
    const status = response.request.status;
    if (status === 200 && response.data) {
      return await response.data;
    }
  }

  throw new Error(`Unable to get weather data from "${city}"`);
};
