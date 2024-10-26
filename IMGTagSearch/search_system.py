import requests

def search_by_image(image_path):
    url = "http://127.0.0.1:5000/search"  # Changed port to 5001
    try:
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            response = requests.post(url, files=files)

        if response.status_code == 200:
            print("Image search request successful.")
            print(response.text)
        else:
            print("Image search request failed.")
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response content: {response.text}")
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found. Please provide a valid image path.")

def search_by_text(query):
    url = "http://127.0.0.1:5000/search_text"  # Changed port to 5001
    data = {'query': query}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Text search request successful.")
        print(response.text)
    else:
        print("Text search request failed.")
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response content: {response.text}")

# Example usage
search_by_image('/Users/arturo/Documents/CodingProjects/IMGTagSearch/uploads/sample_image.jpg')
search_by_text('A beautiful mountain landscape')
