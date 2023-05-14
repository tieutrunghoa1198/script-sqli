import PassFinder
url = "https://0a03002f0431b755858681be007800c5.web-security-academy.net/filter?category=Gifts"
object = PassFinder.PassFinder(url)
object.findPass()