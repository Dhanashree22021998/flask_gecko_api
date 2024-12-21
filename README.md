API Endpoints

1. List All Coins

GET /api/coins

Fetch a list of all available coins with their CoinGecko ID.

2. List Coin Categories

GET /api/coin-categories

Fetch a list of all available coin categories.

3. List Coins by Criteria

GET /api/coins/markets?page=<page>&per_page=<per_page>&order=<order>

Fetch coins based on pagination, order, and other criteria. Market data is displayed against the Canadian Dollar (CAD).

Query Parameters:

page: The page number (default: 1).

per_page: Number of items per page (default: 10).

order: Sorting order (e.g., market_cap_desc).

4. Authentication

POST /login

Login with a username and password to obtain a JWT token.

Request Body:
{
  "username": "testuser",
  "password": "password123"
}

GET /protected

Access a protected route using the JWT token.

Headers:
{
  "Authorization": "Bearer <your_token>"
}

6. Health Check

   GET /healthcheck

Check the health of the application and its third-party services.

7. Version Information

GET /version

Retrieve version details of the application.


Run the Docker container:
   docker run -p 5000:5000 flask-crypto-api
