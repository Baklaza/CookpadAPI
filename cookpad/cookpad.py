from bs4 import BeautifulSoup as bs
import requests


class CookpadApi:

    def __init__(self):

        with requests.Session() as self.se:

            cookies = {
                'ab_session': '0.8266948770862544',
                'f_unique_id': '8ce80f17-7291-47e9-9e6d-6062452dbf8a',
                '_pxhd': 'CAG4uy429QKSgL4mO5iGm5pZfdeSTLeCITFqJtU7yJcQZt-wCUP5FviEQaYT-yEQgEYZIgzGUemXJksBpQUbEw==:wis7FIxRdqz9--X8VAqEP72DX5lF-iuUCiQXqYQuAZ28oy6t4NVZqk6SXN6kSEiXZZKP3N5d5KxOuO7Ea3qoN2ZIMuJekx893eLUlJz0W/Y=',
                '_ym_uid': '1634711346189481235',
                '_ym_d': '1634711346',
                '_ga': 'GA1.2.1277879269.1634711346',
                '_pxvid': '01d3506e-316f-11ec-a3e1-6a456943415a',
                'accept_cookies_and_privacy_and_terms': '1',
                'country_code': 'RU',
                'keyword_history_ru': '%5B%22%D1%88%D0%B0%D1%88%D0%BB%D1%8B%D0%BA%22%2C%22%D0%B2%D0%B0%D1%80%D0%B5%D0%BD%D0%B8%D0%BA%D0%B8%22%2C%22%D1%80%D1%8B%D0%B1%D0%B0%22%2C%22%D1%82%D1%8B%D0%BA%D0%B2%D0%B0%22%2C%22%D0%BF%D0%B5%D0%BB%D1%8C%D0%BC%D0%B5%D0%BD%D0%B8%22%2C%22%D0%BF%D0%B8%D1%80%D0%BE%D0%B3+%D1%81%D0%BE+%D1%81%D0%B3%D1%83%D1%89%D0%B5%D0%BD%D0%BA%D0%BE%D0%B9%22%2C%22%D0%BF%D0%B8%D1%80%D0%BE%D0%B3%D0%B8%22%2C%22%D0%BC%D1%8F%D1%81%D0%BE%22%2C%22meat%22%2C%22%D1%82%D1%8B%D0%BA%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9+%D1%81%D1%83%D0%BF%22%5D',
                '__gads': 'ID=91df97bb452c6380-226ca208fdca0047:T=1634922364:RT=1634922364:S=ALNI_Ma9PLGw1aJQ4PE_SvdwVbvoxuaiWQ',
                'keyword_history_en': '%5B%22meat%22%2C%22egg%22%2C%22pumpkin+soup%22%5D',
                'saves_limit_promotion': '1',
                '_global_web_session': 'vATC4J1TD7Ji1Ewc5KkAN3w1BJUbXLJdTWdu%2FoBsZKtrSGI0TINmldmpnaraKeQwADSPJxD48qvcqOG0lnSvU41jx5Y5LKulElBww0N6Tn8YiRewtLTH7Mrh04tIJKDfqo%2BLwC3JYPKo%2BHNkcKVZYZEj27X%2BVs728Nd1UT1gYXUVfiHkWGTrT4zmsX2SDt8RMbKb5LHeLTg%2Bw6Bx5%2BhPApXGgfQKrsH8yd6Q6KTcltzhG4qpv6ZIWpel5THSWlVOB6l%2B%2FmeWxhMKw4xI%2FfCOhOZySJ3xP7XS9MnRnXXTHoASK5pZCiMkriA%2FYFOhGIZjmQfCjJVJOQxqrzEC4%2Fm0--LbKE5IozVBF0L2Dx--UgOZDNBPDS%2BMfi1vycxePQ%3D%3D',
                'pxcts': 'b0bb8930-3caa-11ec-95bf-c5dd90426dcf',
                '_gid': 'GA1.2.1902817788.1636446541',
                '_ym_isad': '2',
                '_px2': 'eyJ1IjoiNGU0MGU4ZDAtNDEzZC0xMWVjLTkzZGItYzVlMzFkOWVjNzY2IiwidiI6IjAxZDM1MDZlLTMxNmYtMTFlYy1hM2UxLTZhNDU2OTQzNDE1YSIsInQiOjE1NjE1MDcyMDAwMDAsImgiOiJiYTY5ODQ0Zjc5Y2FhZTNhZDY3ODY0Mzg4NGI1YmI4ZmQzYzEzMGYxNTIyZTg5OTgzNDRmNmMyMmJhOTVjOWM2In0=',
                'access_token_global': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltWTBZVGhoTVdKbU1qRTJOVEV4WmpFME5qUTJaakprWTJVeU5EaGlaV0l3TnpRME9UVmpabUU1TkRNeE0yWm1ObVUyT1dJd01UWTRPR1l5TkdSa05XVWkiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5hY2Nlc3NfdG9rZW5fZ2xvYmFsIn19--34c7feb26246846f19310067764ea6e898ce3b82',
                '_ym_visorc': 'b',
                '_pxff_rf': '1',
                '_pxff_fp': '1',
                '_gat': '1',
                '_pxff_ne': '1',
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'If-None-Match': 'W/7a0a2295d120dbb9dc2a0418ead0ea85',
                'Cache-Control': 'max-age=0',
                'TE': 'trailers',
            }

            # params = (
            #     ('via', 'jp'),
            # )

            self.se.cookies.update(cookies)
            self.se.headers.update(headers)


    def set_language(self, lang):
        '''Set language for cookpad.com'''
        self.link_with_lang = f"https://cookpad.com/{lang}"
        return self.link_with_lang


    def find_recipes(self, search = "chicken"):
        '''Find recipes with ingridients or name'''
        self.recipes = requests.get(self.link_with_lang + f"")


    def get_all_recipes_ids(self, search, lang = "us"):
        '''Get recipe id from search request'''
        url = f"https://cookpad.com/{lang}/search/{search}?event=search.typed_query"
        r = self.se.get(url)
       
        if r.status_code == 200:
            print(r.status_code)
            soup = bs(r.text, "lxml")
           
            recipes_id = soup.find_all("a", class_="block-link__main")#.get_attribute("data-search-tracking-result-id")

            print(len(recipes_id))

            return [recipe_id["data-search-tracking-result-id"] for recipe_id in recipes_id]

        else:
            print(f"Connection is not established. statuscode: {r.status_code}")


    def get_recipe_title_by_id(self, recipe_id: str):
        r = self.se.get(f"https://cookpad.com/us/recipes/{recipe_id}")
        if r.status_code == 200:
            print(f"connection accepted. statuscode: {r.status_code}")
            soup = bs(r.text, "lxml")
            title = soup.find("h1", class_="break-words mb-xs text-cookpad-18 xs:text-cookpad-24 md:text-cookpad-36 font-semibold leading-tight clear-both field-group--no-container-xs")
            return title.text.strip()

        else:
            print(f"Connection is not established. statuscode: {r.status_code}")

    
    def get_recipe_ingridients_by_id(self, recipe_id: str):       
        r = self.se.get(f"{self.link_with_lang}/recipes/{recipe_id}")
        if r.status_code == 200:
            soup = bs(r.text, "lxml")
            ingridients = soup.find_all("div", itemprop="ingredients")
            # print(ingridients)
            list_ingridiens = [ingridient.text.strip() for ingridient in ingridients]

            return list_ingridiens

        else:
            print(f"Connection is not established. statuscode: {r.status_code}")


    def get_recipe_instructions_by_id(self, recipe_id: str):
        r = self.se.get(f"https://cookpad.com/us/recipes/{recipe_id}")
        
        if r.status_code == 200:
            soup = bs(r.text, "lxml")

            instructions = soup.find_all("div", itemprop="recipeInstructions")

            return [instruction.text.strip() for instruction in instructions]

        else:
            print(f"Connection is not established. statuscode: {r.status_code}")


    def get_recipe_image_by_id(self, id: str, output_name="recipe-image.jpg"):
        r = self.se.get(f"https://cookpad.com/us/recipes/{id}")
        if r.status_code == 200:
            soup = bs(r.text, "lxml")   

            # src = soup.find("a", rel="nofollow").get_attribute("href")
            src = soup.select_one("div.tofu_image img")
            print(len(src))
            content = self.se.get(src["data-src"]).content

            with open(output_name, "wb") as f:
                f.write(content)

        else:
            print(f"Connection is not established. statuscode: {r.status_code}")

        
    def get_recipe_image_url_by_id(self, recipe_id: str):
        r = self.se.get(f"https://cookpad.com/us/recipes/{recipe_id}")

        if r.status_code == 200:
            soup = bs(r.text, "lxml")  
            # src = soup.select_one("img. lazyloaded").get_attribute("src")
            # return src
            # src = soup.find("div", class_="tofu_image")#.find("img")
            src = soup.select_one("div.tofu_image img")["data-src"]  
            # print(len(src))
            # src = src.get_attribute("data-original")
            return src 
            # return src

        else:
            print(f"Connection is not established. statuscode: {r.status_code}")


    def get_recipe_author(self, recipe_id: str):
        r = self.se.get(f"https://cookpad.com/us/recipes/{recipe_id}")
        if r.status_code == 200:
            soup = bs(r.text, "lxml") 
            author = soup.select_one("div.media")
            return author["data-hidden-from"]

        else:
            print(f"Connection is not established. statuscode: {r.status_code}")

    
    def get_user_recipes(self, user_id: str):
        r = self.se.get(f"https://cookpad.com/us/users/{user_id}")

        if r.status_code == 200:
            soup = bs(r.text, "lxml")
            print(r.status_code)
            # titles = soup.select("h1.inline")
            recipes_ids = soup.select("li.flex")
            # return recipes_ids
            return [recipe_id["id"].split("_")[1] for recipe_id in recipes_ids]

        else:
            print(f"Connection is not established. statuscode: {r.status_code}")
            


    def get_recipe_by_id(self, recipe_id: str):
        r = self.se.get(f"https://cookpad.com/us/recipes/{recipe_id}") 

        if r.status_code == 200:
            soup = bs(r.text, "lxml")

            recipe_title = soup.find("h1", class_="break-words mb-xs text-cookpad-18 xs:text-cookpad-24 md:text-cookpad-36 font-semibold leading-tight clear-both field-group--no-container-xs").text.strip()
            recipe_description = soup.find("p", class_="mb-sm").text.strip()
            recipe_author = soup.find("span", class_="text-cookpad-14 xs:text-cookpad-16").text.strip()
            # about_recipe = soup.find_all("span", class_="mise-icon-text")
            recipe_cooking_time = None
            recipe_quantity_portions = None
            recipe_publicated_time = soup.select_one("div.py-xs time").text
            list_ingridiens = [ingridient.text.strip() for ingridient in soup.find_all("div", itemprop="ingredients")]
            recipe_main_image = f"https://img-global.cpcdn.com/recipes/{soup.select_one('div#recipe_image a')['href'].split('/')[-1]}/1000x1000sq70/photo.jpg"

            dict_instructions = {}
            count = 0
            for step in soup.find_all("li", class_="step numbered-list__item"):
                instruction = step.find("div", itemprop="recipeInstructions").text.strip()

                images = step.select("div.flex a") 

                dict_instructions[str(count)] = {"desc" : instruction, "images_url" : [f"https://img-global.cpcdn.com/steps/{image['href'].split('/')[-1]}/1000x1000sq70/photo.jpg" for image in images]}
                count += 1

            if soup.find("svg", class_="mise-icon mise-icon-time"):
                recipe_cooking_time = soup.select_one("span.px-rg span").text

            if soup.find("svg", class_="mise-icon mise-icon-user"):                
                recipe_quantity_portions = soup.select_one(f"div#serving_recipe_{recipe_id} span").text


            recipe_dict = {
                "title" : recipe_title,
                "main_image_url" : recipe_main_image,
                "description" : recipe_description,
                "author" : recipe_author,
                "cooking_time" : recipe_cooking_time,
                "quantity_portions" : recipe_quantity_portions,
                "publicated_at" : recipe_publicated_time,
                "ingridients" : list_ingridiens,
                "instructions" : dict_instructions
            }
            
            return recipe_dict

        else:
            print(f"Connection is not established. statuscode: {r.status_code}")
    

    def close(self):
        print("Session closed")
        self.se.close()