import React, { FC, createContext, useContext, useState } from 'react';
import { Forecast, ForecastContext } from '../types/weather';
import { getForecasts } from '../services/weather';


const ForecastsContext = createContext<ForecastContext>({} as ForecastContext);


const ForecastsProvider: FC<any> = ({ children }) => {
    const [search, setSearch] = useState<string>('');
    const [entries, setEntries] = useState<Forecast[]>([]);
    const [loading, setLoading] = useState<boolean>(false);
    const [activeEntryIndex, setActiveEntryIndex] = useState<number>(0);

    const executeLoading = async (_func: (params?: any) => any, params?: any) => {
        // Encapsulates function in a loading state
        setLoading(true);
        setTimeout(() => {
            setLoading(false);
        }, 10000);
        try {
            const res = await _func(params);
            setLoading(false);
            return res;
        } finally {
            setLoading(false);
        };
    };

    const fetchForecasts = async () => {
        setEntries([]);
        if (search && search.length > 0)
            return executeLoading(async () => {
                let res: Forecast[] = await getForecasts(search);
                if (res) {
                    setEntries([...res]);
                    return res;
                }
            });
    };

    return (
        <ForecastsContext.Provider value={{
            entries,
            setEntries,
            loading,
            setLoading,
            fetchForecasts,
            search,
            setSearch,
            activeEntryIndex,
            setActiveEntryIndex,
        }}>
            {children}
        </ForecastsContext.Provider>
    );
};

export default function useForecasts() {
    const context = useContext(ForecastsContext);

    if (!context) {
        throw new Error('useForecasts must be used within an ForecastsProvider')
    }

    return context;
}

export { ForecastsProvider };

