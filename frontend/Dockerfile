# frontend/Dockerfile
FROM node:18

WORKDIR /app

COPY . .

RUN npm install

# Run the Svelte development server on port 5173
CMD ["npm", "run", "dev", "--", "--host"]