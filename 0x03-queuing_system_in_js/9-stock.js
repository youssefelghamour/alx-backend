import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

// Initialize Express app
const app = express();
const port = 1245;

// Initialize the Redis client
const redisClient = createClient();
redisClient.on('error', (err) => {
  console.error('Redis error:', err);
});

// Promisify Redis methods
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

// Sample product data
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Function to get product by ID
function getItemById(id) {
  return listProducts.find(item => item.id === id);
}

// Function to reserve stock by ID, updates the stock for the item
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

// Async function to get current reserved stock by ID
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}

// Route to get list of products
app.get('/list_products', (req, res) => {
  const products = listProducts.map(({ id, name, price, stock }) => ({
    itemId: id,
    itemName: name,
    price,
    initialAvailableQuantity: stock,
  }));
  res.json(products);
});

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.stock - reservedStock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  if (reservedStock >= product.stock) {
    return res.json({
      status: 'Not enough stock available',
      itemId,
    });
  }

  await reserveStockById(itemId, reservedStock + 1);
  res.json({
    status: 'Reservation confirmed',
    itemId,
  });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
