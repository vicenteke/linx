import { FC } from "react";
import {
  IconButton,
  Input,
  InputGroup,
  InputRightElement,
  Stack,
  Text,
} from "@chakra-ui/react";
import { MdSearch } from "react-icons/md";
import useForecasts from "../hooks/forecasts";


const SearchInput: FC = () => {
  const { loading, search, setSearch, fetchForecasts } = useForecasts();

  return <Stack spacing={3}>
    <Stack>
      <Text fontSize='4xl'>Welcome!</Text>
      <Text fontSize='4xl' fontWeight='bold'>Select a city</Text>
    </Stack>
    <InputGroup
      size='lg'
      variant='outline'
      colorScheme='black'
      opacity={0.9}
    >
      <Input
        value={search}
        onChange={(e) => setSearch(e.target.value || '')}
        onKeyDown={(e) => {
          if (e.key === 'Enter') fetchForecasts();
        }}
        placeholder="Search for a city"
        disabled={loading}
        focusBorderColor='white'
        colorScheme="black"
        // opacity={0.9}
        _placeholder={{ color: 'white' }}
      />
      <InputRightElement>
        <IconButton
          onClick={fetchForecasts}
          isLoading={loading}
          aria-label="Search forecast"
          icon={<MdSearch />}
          bg='trasnparent'
          color='white'
          fontSize='2xl'
        />
      </InputRightElement>
    </InputGroup>
  </Stack>
};

export default SearchInput;
