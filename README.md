# Waste Classification

End-to-End Deep Learning implementation for waste classification to predict whether waste is **recyclable** or **organic**. This project uses PyTorch-based computer vision models to automatically classify waste materials, enabling automated sorting systems and efficient waste management.

---

## 🎯 Project Overview

This project implements a complete machine learning pipeline for waste classification, from data ingestion to model training and evaluation. It leverages transfer learning with popular deep learning architectures to achieve high accuracy in classifying waste into recyclable and organic categories.

**Key Features:**
- 📥 **Data Ingestion Pipeline** - Automated dataset downloading and preparation
- 🧠 **Model Training Pipeline** - Transfer learning with PyTorch and torchvision
- 📊 **Model Evaluation Pipeline** - Comprehensive model evaluation metrics
- 📝 **Modular Architecture** - Well-organized components for easy maintenance
- 🔧 **Configuration Management** - YAML-based configuration for easy customization

---

## 📋 Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.14+** (as specified in `pyproject.toml`)
- **pip** or **uv** (for dependency management)
- **Git** (for cloning the repository)
- **Disk Space** - At least 5GB for datasets and model files

### System Requirements

- **CPU**: Dual-core processor minimum
- **RAM**: 8GB minimum (16GB recommended)
- **GPU** (Optional): CUDA-capable GPU for faster training (NVIDIA recommended)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/HimmatMagar/waste_classification.git
cd waste_classification
```

### 2. Set Up Python Environment

#### Option A: Using `uv` (Recommended - Fast)
```bash
# Install uv if not already installed
pip install uv

# Install dependencies
uv pip install -e .
```

#### Option B: Using `pip` with Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -e .
```

### 3. Verify Installation

```bash
python -c "import torch; print('PyTorch version:', torch.__version__)"
python -c "from src.wasteClassification import logger; print('Package installed successfully!')"
```

---

## 📦 Project Structure

```
waste_classification/
├── src/wasteClassification/
│   ├── components/              # Core ML components
│   │   ├── data_ingestion.py   # Dataset download and preparation
│   │   ├── training.py         # Model training logic
│   │   ├── model_eval.py       # Model evaluation
│   │   └── model.py            # Model architecture
│   ├── pipeline/               # ML pipelines
│   │   ├── data_ingestion_pipeline.py
│   │   ├── model_training_pipeline.py
│   │   └── model_eval_pipeline.py
│   ├── config/                 # Configuration management
│   ├── entity/                 # Data entity definitions
│   ├── constants/              # Project constants
│   ├── utils/                  # Utility functions
│   └── __init__.py            # Package initialization
├── api/                        # API endpoints (if applicable)
├── config/                     # Configuration files (YAML)
├── notebook/                   # Jupyter notebooks for exploration
├── templates/                  # HTML templates (if web app)
├── main.py                     # Entry point for the project
├── setup.py                    # Package setup configuration
├── pyproject.toml             # Project metadata and dependencies
└── README.md                   # This file
```

---

## 🏃 Running the Project

### Option 1: Run the Complete Pipeline (Recommended)

```bash
python main.py
```

This will execute the model evaluation pipeline by default. To enable other stages, uncomment the relevant sections in `main.py`:

```python
# Uncomment these blocks in main.py to run:

# STAGE_NAME = "Data Ingestion Stage"
# try:
#       logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#       obj = DataIngestionPipeline()
#       obj.main()
#       logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
# except Exception as e:
#       logger.exception(e)
#       raise e

# stage_name = "Model Training Stage"
# try:
#       logger.info(f">>>>>> {stage_name} started <<<<<<")
#       obj = ModelTrainingPipeline()
#       obj.Train_Model()
#       logger.info(f">>>>>> {stage_name} completed <<<<<<")
# except Exception as e:
#       logger.exception(e)
#       raise e
```

### Option 2: Run Individual Stages

#### Data Ingestion
```python
from src.wasteClassification.pipeline.data_ingestion_pipeline import DataIngestionPipeline
pipeline = DataIngestionPipeline()
pipeline.main()
```

#### Model Training
```python
from src.wasteClassification.pipeline.model_training_pipeline import ModelTrainingPipeline
pipeline = ModelTrainingPipeline()
pipeline.Train_Model()
```

#### Model Evaluation
```python
from src.wasteClassification.pipeline.model_eval_pipeline import ModelEvalPipeline
pipeline = ModelEvalPipeline()
pipeline.main()
```

### Option 3: Use Jupyter Notebooks

Explore the project interactively:

```bash
jupyter notebook
# Navigate to the notebook/ directory
```

---

## 📚 Key Dependencies

| Package | Purpose |
|---------|---------|
| **torch** (2.10.0+) | Deep learning framework |
| **torchvision** (0.25.0+) | Computer vision utilities & datasets |
| **scikit-learn** (1.9.0+) | ML preprocessing & metrics |
| **pandas** (3.0.3+) | Data manipulation |
| **numpy** (2.5.0+) | Numerical computations |
| **notebook** (7.6.0+) | Jupyter environment |
| **gdown** (6.1.0+) | Google Drive file downloads |
| **pyyaml** (6.0.3+) | YAML configuration parsing |

---

## ⚙️ Configuration

Configuration files are stored in the `config/` directory using YAML format. Modify these files to customize:

- Model hyperparameters (learning rate, batch size, epochs)
- Data paths and preprocessing settings
- Model architecture details
- Evaluation metrics

Example configuration structure:
```yaml
# config/config.yaml
training:
  batch_size: 32
  epochs: 50
  learning_rate: 0.001
  
data:
  train_path: data/train
  test_path: data/test
  
model:
  architecture: resnet50
  pretrained: true
```

---

## 🔍 Troubleshooting

### Issue: Module not found error
```bash
# Solution: Reinstall the package in editable mode
pip install -e .
```

### Issue: CUDA not available
```bash
# Solution: Install CPU version or check NVIDIA driver
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### Issue: Out of memory during training
```bash
# Solution: Reduce batch size in config
# Modify batch_size in config/config.yaml
```

---

## 📊 Expected Results

After running the complete pipeline, you should see:

1. **Data Ingestion**: Dataset downloaded and processed (~3-5GB)
2. **Model Training**: Training logs with loss and accuracy metrics
3. **Model Evaluation**: Classification report with precision, recall, and F1-score

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Himmat Magar**
- GitHub: [@HimmatMagar](https://github.com/HimmatMagar)
- Email: himmatmagar007@gmail.com

---

## 🎓 References & Resources

- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [Torchvision Models](https://pytorch.org/vision/stable/models.html)
- [Transfer Learning Guide](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
- [Waste Classification Dataset](https://www.kaggle.com/techsash/waste-classification-data)

---

## 📝 Notes

- First run may take longer due to dataset downloading
- GPU usage is optional but significantly speeds up training
- Keep the `config/` directory updated with your preferences
- Check logs in the console or log files for debugging information

---

**Happy Waste Classifying! ♻️**