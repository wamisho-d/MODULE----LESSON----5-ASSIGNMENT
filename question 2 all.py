# Task 1:Implement the merge sort algorithm in Python to sort videos by their titles
# Video Sorting with Merge Sort
def merge_sort_videos(videos):
    if len(videos) <= 1:
        return videos
    
    def merge(left, right):
        sorted_list = []
        while left and right:
            if left[0]['title'].lower() <= right[0]['title'].lower():
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        sorted_list.extend(left)
        sorted_list.extend(right)
        return sorted_list
    
    middle = len(videos) // 2
    left_half = merge_sort_videos(videos[:middle])
    right_half = merge_sort_videos(videos[middle:])

    return merge(left_half, right_half)

# Example usage
videos = [{'title': 'The Matrix'}, {'title': 'Inception'}, {'title': 'Interstellar'}, {'title': 'A Beautiful Mind'}]
sorted_videos = merge_sort_videos(videos)
print(sorted_videos)  # Will print videos sorted by their titles

# Task 2: Develop another REST API endpoint using Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sort_videos', methods=['POST'])
def sort_videos():
    try:
        video_data = request.json.get('videos', [])
        sorted_videos = merge_sort_videos(video_data)
        return jsonify({'sorted_videos': sorted_videos}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# Task 3: Test the video sorting functionality using Postman or a similar tool.
# 1. Start your Flask server by running the script
# 2. Open Postman and create a new request:
  # - Set the request type to POST
  # - Enter the URL as http://localhost:5000/sort_videos.
  # - In the body of the request, select "raw" and type "JSON" data for the list of videos. For instance:
  
     # json
{
    "videos": [
        {"title": "The Matrix"},
        {"title": "Inception"},
        {"title": "Interstellar"},
        {"title": "A Beautiful Mind"}
    ]
}

# Send the request. The response should be a sorted list of videos:
      # json
{
    "sorted_videos": [
        {"title": "A Beautiful Mind"},
        {"title": "Inception"},
        {"title": "Interstellar"},
        {"title": "The Matrix"}
    ]
}