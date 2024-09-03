# Weather Forecast

This project is a simple interface for the Open Weather API (more info at https://openweathermap.org/forecast5).

The back-end is implemented in Python using FastAPI, while the front-end is implemented in React TypeScript using Chakra UI.

The video below shows the working system:

[![Video of the system in action](./media/linx-screenshot.png)](./media/linx-showcase.mp4)

## Running
Everything is containerized, so it should be as easy as going to each folder and running docker-compose.

The following is valid for Linux. If you are running on a different OS or don't have a dependency installed (e.g. Docker, Docker-Compose, Git...), please look for specific instructions for your setup.

### Back-End
```
cd backend
sudo docker-compose up -d
```

### Front-End
```
cd ../frontend
sudo docker-compose up -d
```
