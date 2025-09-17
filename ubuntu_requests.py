import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    try:
        os.makedirs("Fetched_Images", exist_ok=True)
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    #fetching multiple images from multiple urls
    
    urls = []

    while True:
        print("\nOptions:")
        print("1. Enter URLs")
        print("2. Fetch images and exit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            print("Enter image URLs (separated by commas or new lines).")
            print("Enter an empty line to finish this batch.\n")
            while True:
                line = input()
                if not line.strip():
                    break
                # Split input by commas, strip whitespace, and add non-empty URLs
                urls.extend([u.strip() for u in line.split(",") if u.strip()])

        elif choice == "2":
            if not urls:
                print("No URLs provided. Exiting.")
                break  # Changed return to break assuming this is not inside a function
            # Fetch images for all collected URLs
            for url in urls:
                fetch_image(url)
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()