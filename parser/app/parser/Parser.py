from lxml import html
from lxml.html import HtmlElement

from fetch import Request
from models import UserModel

class Parser:
    request: Request = None

    def __init__(self, user: UserModel):
        self.request = Request(user)

    def _get_product_info(self, page: HtmlElement):
        product_data = dict()

        # dict из http://schema.org/Product
        item_scope_div: HtmlElement = page.xpath("//div[@itemtype='http://schema.org/Product']")[0]
        item_scope_children: list[HtmlElement] = item_scope_div.getchildren()
        offers: list[HtmlElement] = None

        # название, цена
        for child in item_scope_children:
            match(child.values()[0]):
                # sku нужен будет в качестве идентификатора
                case "sku":
                    product_data.setdefault("sku", child.values()[1])
                case "offers":
                    offers = item_scope_children.pop(item_scope_children.index(child))
                case "name":
                    product_data.setdefault("name", child.values()[1])

        for child in offers.getchildren():
                if child.values()[0] == "price":
                    product_data.setdefault(child.values()[0], child.values()[1])

        # наличие в магазинах
        stores_values_list: list[HtmlElement] = page.find_class("ty-product-feature__value")
        # массив начинается с элеманта fix: его не учитываем при счете
        counter = -1

        for store_value in stores_values_list:
            if store_value.text_content() != "  —  отсутствует":
                counter += 1

        product_data.setdefault("stores", counter)

        # рейтинг, количество отзывов
        aggregate_rating_div: list[HtmlElement] = page.xpath("//div[@itemprop='aggregateRating']")
        if len(aggregate_rating_div):
            for child in aggregate_rating_div[0].getchildren():
                    match(child.values()[0]):
                        case "reviewCount":
                            product_data.setdefault("review_count", child.values()[1])
                        case "ratingValue":
                            product_data.setdefault("rating_value", child.values()[1])

            # блоки комментариев
            comments = list()
            discussion_block: list[HtmlElement] = page.find_class("ty-pagination-container cm-pagination-container")

            for div in discussion_block:
                children: list[HtmlElement] = div.getchildren()
                for child in children:
                    children_2: list[HtmlElement] = child.getchildren()
                    for child_2 in children_2:
                        message_div: HtmlElement = child_2.find_class("ty-discussion-post__message")
                        if message_div:
                            comments.append({
                                "post_id": child_2.values()[1],
                                "text": message_div[0].text_content().replace("\r\n", "")
                            })
        
            product_data.setdefault("comments", comments)
        
        return product_data
    
    # данные пользователя
    def get_user_info(self):
        user_data = dict()

        page = self.request.get_page_from_uri("profiles-update")

        body = html.fromstring(page.content)
        profile_form = body.forms[2].form_values()
    
        for element in profile_form:
            match(element[0]):
                case "user_data[email]":
                    user_data.setdefault("email", element[1])
                case "user_data[s_firstname]":
                    user_data.setdefault("firstname", element[1])
                case "user_data[s_lastname]":
                    user_data.setdefault("lastname", element[1])
                case "user_data[s_city]":
                    user_data.setdefault("city", element[1])
        
        return user_data

    # избранные товары
    def get_grid_list(self):
        grid_list = list()

        page = self.request.get_page_from_uri("wishlist")
        body = html.fromstring(page.content)

        # получение списка товаров в избранном
        grid_divs_list = body.find_class("product-title")

        links = list()

        # полечение списка ссылок для каждого товара в избранном
        for item in grid_divs_list:
            for iterlink in item.iterlinks():
                (_, _, link, _) = iterlink
                links.append(link)

        for url in links:
            item_page = self.request.get_page_from_url(url)
            grid_list.append(self._get_product_info(html.fromstring(item_page.content)))

        return grid_list