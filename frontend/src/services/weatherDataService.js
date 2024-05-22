import Dexie from 'dexie';

// Initialize Dexie database
const db = new Dexie('WeatherDatabase');

// Define your database schema
db.version(1).stores({
  fireRiskPredictions: '++id, location, timestamp, risks' // risks is an array of fire risk data
});

export default db;

// Function to save fire risk predictions
export const saveFireRiskPrediction = async (fireRiskPrediction) => {
    await db.fireRiskPredictions.add(fireRiskPrediction);
  };

  
  // Function to get the latest fire risk prediction
export const getLatestFireRiskPrediction = async () => {
    return await db.fireRiskPredictions
      .orderBy('timestamp')
      .reverse() // We use reverse to get the most recent data first
      .first(); // Returns the most recent prediction
  };
  