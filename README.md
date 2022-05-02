<div align="center">

# AnonyME
web-app for hackathon

</div>

## Get Stared
1. clone this repo:
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

## Deployment
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

