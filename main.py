import instaloader

def get_link():
    f = open("links.txt" , "r" , encoding="utf-8")
    return f.read().split('\n')
def main():
    USER = input("enter username > ")
    PASSWORD = input("enter password > ")
    shortcode = input("enter shortcode psot > ")

    L = instaloader.Instaloader()

    L.login(USER, PASSWORD)        # (login)

    links = get_link()

    u = []
    for link in links:
        P = instaloader.Post.from_shortcode(L.context , shortcode)
        for like in P.get_likes():
            if like.username not in u:
                print(like.username)
                u.append(like.username)

    with open("LIKEscrape.txt" , "a" , encoding="utf-8") as f:
        f.write('\n'.join(u))

    print("[+] finish scrape")

if __name__ == "__main__":
    main()
