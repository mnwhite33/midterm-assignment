import requests
import random
import time

# Define base URL
base_url = 'http://localhost:3000/post'

# Function to create a post
def create_post(title, topic, message):
    post_data = {
        "title": title,
        "topic": topic,
        "message": message
    }
    response = requests.post(base_url, json=post_data)
    if response.status_code == 200:
        print("Post created successfully.")
        return response.json()
    else:
        print(f"Failed to create post, status code: {response.status_code}")
        return None

# Function to get all posts
def get_all_posts():
    response = requests.get(base_url)
    if response.status_code == 200:
        print("\nAll posts retrieved successfully.")
        return response.json()
    else:
        print(f"\nFailed to retrieve posts, status code: {response.status_code}")
        return None

# Function to get a post by ID
def get_post_by_id(post_id):
    response = requests.get(f"{base_url}/{post_id}")
    if response.status_code == 200:
        print(f"\nPost {post_id} retrieved successfully.")
        return response.json()
    else:
        print(f"\nFailed to retrieve post {post_id}, status code: {response.status_code}")
        return None

# Function to delete all posts
def delete_all_posts():
    response = requests.delete(base_url)
    if response.status_code == 200:
        print("\nAll posts deleted successfully.")
    else:
        print(f"\nFailed to delete all posts, status code: {response.status_code}")

# Function to delete a specific post by ID
def delete_post_by_id(post_id):
    response = requests.delete(f"{base_url}/{post_id}")
    if response.status_code == 200:
        print(f"\nPost {post_id} deleted successfully.")
    else:
        print(f"\nFailed to delete post {post_id}, status code: {response.status_code}")

# Function to edit a specific post by ID
def edit_post_by_id(post_id, new_data):
    response = requests.patch(f"{base_url}/{post_id}", json=new_data)
    if response.status_code == 200:
        print(f"\nPost {post_id} updated successfully.")
        return response.json()
    else:
        print(f"\nFailed to update post {post_id}, status code: {response.status_code}")
        return None

# Function to get a random post ID
def get_random_post_id():
    response = requests.get(base_url)
    if response.status_code == 200:
        posts = response.json()
        if posts:
            # Use '_id' instead of 'id'
            post_ids = [post['_id'] for post in posts]
            return random.choice(post_ids)
        else:
            print("No posts available to select a random ID.")
            return None
    else:
        print("Failed to retrieve posts for selecting a random ID.")
        return None

post1 = create_post("First Entry", "science", "First message")
post2 = create_post("Second Entry", "politics", "Another message here")

print("Post 1:", post1)
print("Post 2:", post2)

#get all posts
all_posts = get_all_posts()
print("All Posts:", all_posts)


# Get a random post ID and perform operations
post_id = get_random_post_id()
if post_id:
    print("Random Post ID selected:", post_id)
    print(get_post_by_id(post_id))
    
    # Edit the randomly selected post
    edited_post = edit_post_by_id(post_id, {'title': 'Updated Title', 'message': 'Updated message'})
    print("Edited Post:", edited_post)

delete_post_by_id(post_id)

all_posts = get_all_posts()
print("All Posts:", all_posts)

post_id = get_random_post_id()
if post_id:
    print("Random Post ID selected:", post_id)
    print(get_post_by_id(post_id))
    
    # Edit the randomly selected post
    edited_post = edit_post_by_id(post_id, {'title': 'Updated Title 2', 'message': 'Updated message 2'})
    print("Edited Post:", edited_post)

delete_post_by_id(post_id)

delete_all_posts()