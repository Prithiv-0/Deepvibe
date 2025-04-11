# DeepVibe 
**AI-powered code modification tool**

![CLI Demo](https://via.placeholder.com/800x400?text=DeepVibe+Terminal+Demo) *(Replace with actual screenshot)*

## Features
- **Code Refactoring** – Automatically improves existing code
- **Multi-Language Support**

      Python
      C++
      C
      Rust
      Java
      Go
      Javascript
      Typescript
      HTML
      CSS
      Text(.txt)

- **CLI Interface** – Simple commands like `deepai <file> --modify`
- **Code Generation** - Generates new code and files from a single prompt

## Quick Start

### Prerequisites
- [Rust](https://www.rust-lang.org/tools/install) (for the CLI)
- [Python 3.10+](https://www.python.org/downloads/) (for the AI script)
- API Key([you can get a free one here](https://openrouter.ai/))

### Pre-Installation Steps
- Open script.py and add your API-KEY, API-url and other required details in the Correct location (The comments will point you to the location)
- Save and exit

### Installation
```bash
git clone https://github.com/yourusername/deepvibe.git
cd deepvibe
chmod +x install.sh && ./install.sh
```
- You can delete the repo after installation

## Post-Installation
- Refresh the Terminal or open another Terminal.
- To use the tool,write Comments of what you want to change in your code.

### Usage
- To start the Cli:
```bash
deepvibe
```
- To modify your existing file:
```bash
#insert file name or path in the place of input.py
deepai input.py --modify
```
- To Create a new file from existing code/Prompt
```bash
#insert input file-name / path in the place of input.rs
#insert name of choice for your output file in the place of output.rs
deepai input.rs --newfile output.rs
```



