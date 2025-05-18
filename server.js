const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");

const app = express();

// Set EJS as the view engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "api/views"));

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public"))); // For static assets (CSS, images, etc.)

// Home Page
app.get("/", (req, res) => {
  res.render("Home", { currentPage: "home" });
});

// Crop Recommendation Form
app.get("/crop-recommendation", (req, res) => {
  res.render("pages/cropRec", { currentPage: "crop-recommendation" });
});

// Handle Crop Recommendation Submission
app.post("/crop-recommendation/result", (req, res) => {
  // Extract form data
  const { n, p, k, temperature, humidity, ph, rainfall } = req.body;

  // TODO: Replace this with your ML model prediction logic
  // For now, we'll use a placeholder
  const recommendedCrop = "Wheat"; // Replace with actual prediction

  res.render("pages/cropRes", {
    currentPage: "crop-recommendation",
    recommendedCrop,
    n,
    p,
    k,
    temperature,
    humidity,
    ph,
    rainfall,
  });
});

// Farm Monitoring Page (placeholder)
app.get("/farm-monitoring", (req, res) => {
  res.render("pages/farmMonitoring", { currentPage: "farm-monitoring" });
});

// Documentation Page
app.get("/docs", (req, res) => {
  res.render("pages/Docs/Docs", { currentPage: "docs" });
});

// 404 Handler
app.use((req, res) => {
  res.status(404).send("<h2>404 - Page Not Found</h2>");
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});
