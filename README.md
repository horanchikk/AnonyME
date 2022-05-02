<div align="center">

# AnonyME

Web application for hackathon

</div>

## Setting up a Workspace

1. Сlone this repo:
   ```bash
   git clone https://github.com/horanchikk/anonyme
   cd anonyme
   ```
2. Install `npm` and `python` packages:

   ```bash
   cd frontend
   npm install

   cd ../backend
   pip install requirements.txt
   ```

3. Launch application

- frontend:
  ```bash
  cd frontend && npm run dev
  ```
  or
  ```bash
  cd frontend && yarn && yarn dev
  ```
- backend
  ```bash
  cd backend
  uvicorn main:app --reload --host 127.0.0.1 --port 8000
  ```

Now you can navigate to http://localhost:3000/ where you can see start page of application.
