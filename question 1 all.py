# Video Search Application with Binary Search
# Task 1: Implement the binary search algorithm for searching videos by title.

def binary_search(titles, search_query):
    low, high = 0, len(titles) - 1
    while low <= high:
        mid = (low + high) // 2
        if titles[mid] == search_query:
            return mid  # Item found
        elif titles[mid] < search_query:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Item not found

# Ensure the list is sorted
video_titles = sorted([
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
])

# Test the binary search function
search_query = "Exploring the Cosmos"
index = binary_search(video_titles, search_query)
print(f"Title found at index: {index}" if index != -1 else "Title not found")

# Task 2: Develop a REST API endpoint using Flask.
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_video():
    search_query = request.args.get('title', '')
    index = binary_search(video_titles, search_query)
    if index != -1:
        return jsonify({"video_title": video_titles[index]}), 200
    else:
        return jsonify({"message": "Video title not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

# Task 3: Test the video search functionality using Postman or a similar tool:
# 1. Install Postman or a similar tool.
# 2. Ensure your Flask application is running on localhost or a specific server.
# 3. Send a GET request to the / search endpoint with a query parameter title. For instance, http:// localhost:5000/search?title=Exploring%20the%20Cosmos.
# 4. Verfiy the response for various inputs, both for titles present in the list and those not present .
# Example API Requests
  # - Exsisting title: /search?title=Exploring%20the20Cosmos
  # - Non-existing title: /search?title=Non-existing%20Title


