const express = require("express");
const router = express.Router();
const cropController = require("../controllers/cropController");

// POST endpoint for crop recommendation
router.post("/crop-recommendation", cropController.getCropRecommendation);

module.exports = router;
