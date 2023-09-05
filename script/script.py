import requests
import random
import time
import json
from faker import Faker

with open("config.json", "r") as config_file:
    config_data = json.load(config_file)

number_of_users = config_data["number_of_users"]
max_posts_per_user = config_data["max_posts_per_user"]
max_likes_per_user = config_data["max_likes_per_user"]

fake = Faker()

users_data = []

for _ in range(number_of_users):
    email = fake.email()
    password = fake.password()
    first_name = fake.first_name()

    user_data = {"email": email, "password": password, "first_name": first_name}
    users_data.append(user_data)

base_url = 'http://127.0.0.1:5000'
created_posts = []

def register_user(email, password, first_name):
    registration_url = f'{base_url}/api/register'
    data = {
        "email": email,
        "password": password,
        "first_name": first_name
    }

    response = requests.post(registration_url, json=data)

    if response.status_code == 201:
        print(f"User {first_name} registered successfully.")
    else:
        print(f"User {first_name} registration failed. Status code:", response.status_code)


def get_jwt_token(email, password):
    login_url = f'{base_url}/api/login'
    data = {
        "email": email,
        "password": password
    }

    response = requests.post(login_url, json=data)

    if response.status_code == 200:
        jwt_token = response.json()["result"]["access_token"]
        return jwt_token
    else:
        print(f"Login failed for {email}. Status code:", response.status_code)
        return None


def create_post(jwt_token):
    post_url = f'{base_url}/api/posts'
    headers = {"Authorization": f"Bearer {jwt_token}"}
    data = {
        "title": "Random Title",
        "description": "Random Description"
    }

    response = requests.post(post_url, json=data, headers=headers)

    if response.status_code == 200:
        post_id = response.json()["result"]["id"]
        created_posts.append(post_id)
        print(f"Post created successfully with ID {post_id}")


def like_post(post_id, jwt_token):
    like_url = f'http://127.0.0.1:5000/api/{post_id}/like'
    headers = {'Authorization': f'Bearer {jwt_token}'}

    response = requests.post(like_url, headers=headers)

    if response.status_code == 200:
        print(f"Post {post_id} liked successfully.")
    else:
        print(f"Failed to like post {post_id}. Status code: {response.status_code}")


def dislike_post(post_id, jwt_token):
    dislike_url = f'http://127.0.0.1:5000/api/{post_id}/dislike'
    headers = {'Authorization': f'Bearer {jwt_token}'}

    response = requests.post(dislike_url, headers=headers)

    if response.status_code == 200:
        print(f"Post {post_id} disliked successfully.")
    else:
        print(f"Failed to like post {post_id}. Status code: {response.status_code}")


likes_per_post = 3

for user_data in users_data:
    register_user(user_data["email"], user_data["password"], user_data["first_name"])
    jwt_token = get_jwt_token(user_data["email"], user_data["password"])

    if jwt_token:
        post_count = random.randint(0, max_posts_per_user)

        for _ in range(post_count):
            create_post(jwt_token)

total_likes = 0
likes_count_per_user = {user_data["email"]: 0 for user_data in users_data}
stop = False
while total_likes < (len(created_posts) * likes_per_post) and not stop:
    for user_data in users_data:
        jwt_token = get_jwt_token(user_data["email"], user_data["password"])

        if jwt_token and created_posts:
            post_id = random.choice(created_posts)

            if likes_count_per_user[user_data["email"]] < max_likes_per_user:
                like_post(post_id, jwt_token)
                likes_count_per_user[user_data["email"]] += 1
                total_likes += 1
                time.sleep(1)
            else:
                print("likes_count_per_user reached")
                stop = True
                break
