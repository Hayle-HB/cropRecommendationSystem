const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");

// Helper to check if model exists
function modelExists() {
  const modelPath = path.join(__dirname, "../../ML_Model/trained_model.pkl");
  return fs.existsSync(modelPath);
}

// Helper to run main.py if model doesn't exist
function runMainPy() {
  return new Promise((resolve, reject) => {
    const py = spawn("python", [path.join(__dirname, "../../main.py")]);
    py.stdout.on("data", (data) => process.stdout.write(data));
    py.stderr.on("data", (data) => process.stderr.write(data));
    py.on("close", (code) => {
      if (code === 0) resolve();
      else reject(new Error("main.py failed"));
    });
  });
}

// POST /api/crop-recommendation
exports.getCropRecommendation = async (req, res) => {
  try {
    // 1. Ensure model exists
    if (!modelExists()) {
      await runMainPy();
    }

    // 2. Prepare input data for Python script
    const { n, p, k, temperature, humidity, ph, rainfall } = req.body;
    const inputData = JSON.stringify({
      n,
      p,
      k,
      temperature,
      humidity,
      ph,
      rainfall,
    });

    // 3. Call a Python script to load model and predict
    const py = spawn("python", [
      path.join(__dirname, "../../ML_Model/predict.py"),
      inputData,
    ]);

    let result = "";
    py.stdout.on("data", (data) => {
      result += data.toString();
    });

    py.stderr.on("data", (data) => {
      process.stderr.write(data);
    });

    py.on("close", (code) => {
      if (code !== 0) {
        return res.status(500).json({ error: "Prediction failed" });
      }
      try {
        const prediction = JSON.parse(result);
        res.json(prediction);
      } catch (err) {
        res.status(500).json({ error: "Invalid prediction output" });
      }
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
