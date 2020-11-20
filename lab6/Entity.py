class News:
    def __init__(self, id, site, title, link, description, published):
        self.id = id
        self.site = site
        self.title = title
        self.link = link
        self.description = description
        self.published = published


class Site:
    def __init__(self, id_site, name, url):
        self.id_site = id_site
        self.name = name
        self.url = url