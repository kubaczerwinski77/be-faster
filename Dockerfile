# == CLIENT ==
FROM node:12.22.12-bullseye AS client_build

# Install dependencies
WORKDIR /client
COPY client/package.json client/package-lock.json ./
RUN npm ci

# Build client
COPY client .
RUN npm run build

# == SERVER ==
FROM python:3.9-bullseye AS production
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --requirement requirements.txt

# Run server
COPY . .
COPY --from=client_build /client/build client/build
CMD python -m uvicorn --host=0.0.0.0 --port=3000 main:app