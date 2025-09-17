# Ubuntu Image Fetcher

A Python-based tool for mindfully collecting images from the web. This utility allows users to download multiple images from provided URLs and save them locally in an organized manner.

## Features

- Download multiple images simultaneously
- Automatically create storage directory
- Preserve original filenames when possible
- Handle various types of download errors gracefully
- User-friendly command-line interface

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Ubuntu_Requests.git
cd Ubuntu_Requests
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

1. Run the script:
```bash
python ubuntu_requests.py
```

2. Choose from the following options:
   - Option 1: Enter URLs (multiple URLs can be entered, separated by commas or new lines)
   - Option 2: Start downloading images and exit

3. Images will be saved in the `Fetched_Images` directory within the project folder

## Example

```bash
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Options:
1. Enter URLs
2. Fetch images and exit
Enter your choice (1 or 2): 1

Enter image URLs (separated by commas or new lines).
Enter an empty line to finish this batch.

https://example.com/image1.jpg
https://example.com/image2.jpg

Options:
1. Enter URLs
2. Fetch images and exit
Enter your choice (1 or 2): 2
```

## Error Handling

The script handles various types of errors including:
- Network connection issues
- Invalid URLs
- Timeout errors
- File system errors

## License

[Add your chosen license here]

## Contributing

Feel free to submit issues and enhancement requests!

## Author

[Your Name]