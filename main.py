import requests
def get_facebook_posts(page_id, access_token):
    url = f"https://graph.facebook.com/v12.0/{page_id}/posts"
    params = {
        'access_token': access_token,
        'fields': 'id,message,created_time'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
def main():
    # Replace 'your_page_id' with the actual Facebook Page ID
    page_id = 'your_page_id'
    # Replace 'your_access_token' with your actual access token
    access_token = 'your_access_token'
    posts = get_facebook_posts(page_id, access_token)
    if posts:
        for post in posts.get('data', []):
            print(f"Post ID: {post['id']}")
            print(f"Message: {post.get('message', 'No message available')}")
            print(f"Created Time: {post['created_time']}")
            print('-' * 40)
if __name__ == "__main__":
    main()
