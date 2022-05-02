<div align="center">

# AnonyME
web-app for hackathon

</div>

## Get Started
1. Сlone this repo:
   ```bash
   git clone https://github.com/horanchikk/anonyme
   cd anonyme
   ```
2. Install `npm` packages:
   ```bash
   cd frontend
   npm install
   ```
3. Install `python` packages:
   ```bash
   cd ../backend
   pip install requirements.txt
   ```

## Setting up a Workspace
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

