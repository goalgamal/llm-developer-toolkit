# 🤖 AI-Powered Developer Toolkit

A suite of LLM-powered tools designed to accelerate the software development lifecycle. This project leverages **OpenAI (GPT-4o)** and **open-source models (Qwen 2.5-Coder via Hugging Face)** to automate code optimization, testing, and documentation.

## 🚀 Features

This toolkit includes three distinct tools accessible via a **Gradio** interface:

### 1. Python to C++ Transpiler (High Performance)

* **Goal:** Converts Python logic into high-performance, O3-optimized C++ code.
* **Capabilities:**
* Automatically handles type conversion (e.g., avoiding int overflows).
* Includes a built-in compiler runner to execute the generated C++ and benchmark speed against the original Python.
* **Benchmarking:** Often achieves 100x+ speed improvements for computational tasks.



### 2. Automated Unit Test Generator

* **Goal:** Ensures code reliability by generating comprehensive test suites.
* **Capabilities:**
* Detects the language and uses standard frameworks (e.g., `unittest` for Python).
* Covers edge cases, normal inputs, and exception handling.
* Includes a runner to execute the generated tests immediately within the UI.



### 3. Smart Documentation & Commenter

* **Goal:** Improves code maintainability/readability.
* **Capabilities:**
* Adds professional docstrings (Google/NumPy style).
* Injects inline comments for complex logic without stating the obvious.
* Preserves original code structure and logic.



## 🛠️ Tech Stack

* **LLM Orchestration:** OpenAI API, Hugging Face Inference Client (Nebius).
* **Models:** GPT-4o-mini, Qwen/Qwen2.5-Coder-32B-Instruct.
* **Interface:** Gradio (for rapid UI prototyping).
* **Environment:** Python 3.11+, Dotenv for security.

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/llm-developer-toolkit.git
cd llm-developer-toolkit

```


2. **Install dependencies**
```bash
pip install -r requirements.txt

```


3. **Set up Environment Variables**
* Rename `.env.example` to `.env`.
* Add your API keys:


```bash
OPENAI_API_KEY=sk-...
HF_TOKEN=hf_...

```



## 💻 Usage

To launch any of the tools, navigate to the `notebooks/` directory and run the Jupyter Notebooks, or convert them to scripts.

**Example: launching the Unit Test Tool**

1. Open `notebooks/UnitTestTool.ipynb`.
2. Run all cells.
3. The Gradio interface will launch in your browser (or inline).

## 📸 Screenshots

...

## 🔮 Future Improvements

* [ ] Convert Notebooks to modular `.py` scripts for CLI usage.
* [ ] Add support for Anthropic Claude 3.5 Sonnet.
* [ ] Containerize the application using Docker.

## 📄 License

This project is licensed under the MIT License.
