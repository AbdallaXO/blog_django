from django.shortcuts import render
from datetime import date

# Create your views here.
posts = [
    {
        "slug": "mountain-khabib",
        "image": "mountains.jpg",
        "author": "abdi",
        "date": date(2024, 7, 2),
        "title": "Mountain Hiking",
        "excerpt": "Nothing better than being on the mountain chilling and enjoying the view",
        "content": """ 
          Lorem ipsum dolor, sit amet consectetur 
          adipisicing elit. Voluptas, omnis nisi. Fuga, 
          suscipit blanditiis. Rerum amet adipisci sit modi rem aut, 
          dolores tempore reprehenderit eos dolore, quos voluptates fugiat ipsa.
        """,
    },
    {
        "slug": "khabib-bootcamp",
        "image": "mcgreg.jpg",
        "author": "abdi",
        "date": date(2025, 1, 3),
        "title": "Khabib Bootcamp",
        "excerpt": "Nothing better than being on the mountain chilling and enjoying the view",
        "content": """ 
          Exciting news! The legendary Khabib Nurmagomedov will be making a special appearance at our 
          upcoming Khabib Bootcamp. This is your chance to witness the champion in action, gain insights from his world-class training, and experience the discipline and dedication that made him a legend in MMA.
        """,
    },
    {
        "slug": "fighting-bears",
        "image": "frank.jpg",
        "author": "abdi",
        "date": date(2025, 1, 23),
        "title": "Fighting Bears",
        "excerpt": "Nothing better than being on the mountain chilling and enjoying the view",
        "content": """ 
          Get ready to push your limits at the Fighting Bears Bootcamp, where strength, endurance, and discipline come together. Whether you're a beginner or a seasoned athlete, this intense training experience will challenge you like never before.
          Train with elite coaches, master combat techniques, and develop the mindset of a warrior. 
        It's time to awaken the fighter within and join the pack!
        """,
    },
]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts_list(request):
    return render(request, "blog/posts.html", {
        "all_posts": posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
