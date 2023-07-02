FROM node:latest
WORKDIR /frontend
COPY package.json ./
RUN npm install
ADD . .
EXPOSE 3000
CMD ["npm", "start"]