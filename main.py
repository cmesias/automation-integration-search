import webbrowser

def open_integration_tabs(search_term):
    # Define the base search URL
    base_url = "https://www.google.com/search?q="

    # Define the integration types
    integrations = [
        "Zapier integration",
        "Make integration",
        "MS AppSource integration",
        "MS Power Automate integration",
        "API",
        "Webhooks"
    ]

    # Open a new browser tab for each integration search
    for integration in integrations:
        search_query = f"{search_term} {integration}"
        webbrowser.open_new_tab(base_url + search_query)

if __name__ == "__main__":
    while True:
        # Ask for user input
        search_term = input("Enter the platform/tool you want to search for (or type 'exit' to quit): ").strip()
        
        if search_term.lower() == 'exit':
            break
        
        open_integration_tabs(search_term)
        print(f"Opened tabs for: {search_term}")