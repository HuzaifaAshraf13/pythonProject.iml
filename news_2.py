import tkinter as tk
import requests

# Replace 'YOUR_API_KEY' with your actual NewsAPI key
api_key = '3836096af74d47e3991542f31432d5c1'


def get_news():
    category = category_var.get()
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'category': category.lower(),
        'language': 'en',  # Fetch news only in English
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']

        # Clear any previous news displayed
        news_text.delete(1.0, tk.END)

        for article in articles:
            title = article['title']
            source = article['source']['name']
            news_text.insert(tk.END, f"Title: {title}\nSource: {source}\n\n")

        # Recommend news sources for the selected category
        recommended_sources = set()
        for article in articles:
            recommended_sources.add(article['source']['name'])

        recommended_sources_text.delete(1.0, tk.END)
        recommended_sources_text.insert(tk.END, "Recommended Sources:\n")
        for source in recommended_sources:
            recommended_sources_text.insert(tk.END, f"- {source}\n")
    else:
        news_text.delete(1.0, tk.END)
        news_text.insert(tk.END, f"Error: {response.status_code}")


# Create the main window
root = tk.Tk()
root.title("News Viewer")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the main window size to fit the screen
window_width = int(screen_width * 0.8)  # 80% of the screen width
window_height = int(screen_height * 0.8)  # 80% of the screen height
root.geometry(f"{window_width}x{window_height}")

# Create a label and dropdown menu for selecting news categories
category_label = tk.Label(root, text="Select a news category:")
category_label.pack()

categories = ["business", "entertainment", "health", "science", "sports", "technology"]
category_var = tk.StringVar(root)
category_var.set(categories[0])
category_menu = tk.OptionMenu(root, category_var, *categories)
category_menu.pack()

# Create a button to fetch news
fetch_button = tk.Button(root, text="Fetch News", command=get_news)
fetch_button.pack()

# Create a text widget for displaying news
news_text = tk.Text(root, wrap=tk.WORD, height=int(window_height * 0.6), width=int(window_width * 0.7))
news_text.pack()

# Create a text widget for recommending sources
recommended_sources_text = tk.Text(root, wrap=tk.WORD, height=int(window_height * 0.2), width=int(window_width * 0.7))
recommended_sources_text.pack()

# Start the GUI event loop
root.mainloop()
