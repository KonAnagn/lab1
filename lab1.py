import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

##    url = input("Enter URL: ")
url = 'http://google.com/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
##    html = response.text
##    print("\nRESPONSE HEADER")
##    more(html)

    print(f"Website headers: {url} \n, {response.headers}\n\n")

    server = response.headers.get("Server")

    if server:
        print(f"Server: {server}")
    else:
        print("No server found")

    cookies = response.headers.get("Set-Cookie")

    if cookies:
        print(f"Cookies: {cookies}")
    else:
        print("No cookies found :C")


    
