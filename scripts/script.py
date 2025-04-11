import os
import sys
import requests
import json

def detect_language(file_path):
    extension = os.path.splitext(file_path)[1]
    language_map = {
        ".py": "Python",
        ".cpp": "C++",
        ".c": "C",
        ".java": "Java",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".rs": "Rust",
        ".go": "Go",
        ".html": "HTML",
        ".css": "CSS",
        ".txt": "text",
    }
    return language_map.get(extension, "Unknown")

def get_comment_syntax(language):
    comment_map = {
        "Python": "# ",
        "C++": "// ",
        "C": "// ",
        "Java": "// ",
        "JavaScript": "// ",
        "TypeScript": "// ",
        "Rust": "// ",
        "Go": "// ",
        "HTML": "<!-- ",
        "CSS": "/* ",
        "text": "# ",
    }
    return comment_map.get(language, "# ")

def extract_code_from_response(response):
    """Extract code blocks from markdown response"""
    code_blocks = []
    in_code_block = False
    current_block = []
    
    for line in response.split('\n'):
        if line.startswith('```'):
            if in_code_block:
                code_blocks.append('\n'.join(current_block))
                current_block = []
            in_code_block = not in_code_block
        elif in_code_block:
            current_block.append(line)
    
    return '\n\n'.join(code_blocks) if code_blocks else response

def call_openrouter_api(code, language, instruction):
    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": "Bearer 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"}
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{instruction}\n\n```{language}\n{code}\n```"}]
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")

def format_output(original_code, analysis, language, modify):
    comment_prefix = get_comment_syntax(language)
    formatted_output = ""
    inside_code_block = False
    for line in analysis.split("\n"):
        if line.startswith("```"):
            inside_code_block = not inside_code_block
            continue
        if inside_code_block:
            formatted_output += line + "\n"
        else:
            formatted_output += comment_prefix + line + "\n"
    return formatted_output

def main():
    args = sys.argv[1:]
    
    if len(args) < 2:
        print("Usage: script.py <input_file> <output_file>")
        print("For --modify mode: output_file = input_file")
        sys.exit(1)
    
    input_file = args[0]
    output_file = args[1]
    modify_mode = (input_file == output_file)
    
    language = detect_language(input_file)
    if language == "Unknown":
        print("⚠️ Unsupported file type.")
        sys.exit(1)
    
    try:
        with open(input_file, "r") as f:
            original_code = f.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    instruction = "Analyze and provide improved implementation"
    analysis = call_openrouter_api(original_code, language, instruction)
    formatted_output = format_output(original_code, analysis, language, modify_mode)
    
    try:
        with open(output_file, "w") as f:
            f.write(formatted_output)
        print(f"✅ Output written to: {output_file}")
    except IOError:
        print(f"Error: Could not write to '{output_file}'")
        sys.exit(1)

if __name__ == "__main__":
    main()
