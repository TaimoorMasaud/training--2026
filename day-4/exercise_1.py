import requests
import sys

def fetch_github_user(username):
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"

    try:
        # Fetch user profile
        user_res = requests.get(user_url)

        if user_res.status_code == 404:
            print("Error: User not found.")
            return
        elif user_res.status_code == 403:
            print("Error: API rate limit exceeded. Try again later.")
            return

        user_res.raise_for_status()
        user_data = user_res.json()

        # Fetch repositories
        repos_res = requests.get(repos_url)

        if repos_res.status_code == 403:
            print("Error: API rate limit exceeded while fetching repos.")
            return

        repos_res.raise_for_status()
        repos_data = repos_res.json()

        # Sort repos by stars (descending)
        top_repos = sorted(
            repos_data,
            key=lambda repo: repo.get("stargazers_count", 0),
            reverse=True
        )[:5]

        # Print user info
        print("\n=== GitHub Profile ===")
        print(f"Username: {user_data.get('login')}")
        print(f"Bio: {user_data.get('bio')}")
        print(f"Public Repos: {user_data.get('public_repos')}")
        print(f"Followers: {user_data.get('followers')}")

        # Print top repos
        print("\n=== Top 5 Repositories by Stars ===")
        for repo in top_repos:
            print(f"- {repo.get('name')}")
            print(f"  Stars: {repo.get('stargazers_count')}")
            print(f"  Language: {repo.get('language')}")
            print()

    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


if __name__ == "__main__":
    # Bonus: take username from command line
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Enter GitHub username: ")

    fetch_github_user(username)