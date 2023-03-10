
import pandas as pd
from geopy.geocoders import Nominatim
from preprocesamiento import Preprocesamiento

print("processing...")
'''

    *** ORDERS ***

'''
Orders = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_orders_dataset.csv")
orders = Preprocesamiento(Orders)

orders.reemplazar_fechas_nulas("order_purchase_timestamp", "order_approved_at")
orders.reemplazar_fechas_nulas("order_approved_at", "order_delivered_carrier_date")
orders.reemplazar_fechas_nulas("order_delivered_carrier_date", "order_delivered_customer_date")

orders.cambio_tipo_fecha("order_purchase_timestamp")
orders.cambio_tipo_fecha("order_approved_at")
orders.cambio_tipo_fecha("order_delivered_carrier_date")
orders.cambio_tipo_fecha("order_delivered_customer_date")
orders.cambio_tipo_fecha("order_estimated_delivery_date")

orders.intercambio_fechas("order_approved_at", "order_delivered_carrier_date")
orders.intercambio_fechas("order_delivered_carrier_date", "order_delivered_customer_date")

orders.clean_to_csv("orders.csv")

'''

    *** ORDER ITEMS ***

'''
Order_Items = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_order_items_dataset.csv")
order_items = Preprocesamiento(Order_Items)

order_items.clean_to_csv("order_items.csv")

'''

    *** SELLERS ***

'''

Sellers = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_sellers_dataset.csv")
sellers = Preprocesamiento(Sellers)

sellers.clean_to_csv("sellers.csv")


'''

    *** PRODUCTS ***

'''
Products = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_products_dataset.csv")
products = Preprocesamiento(Products)

products.llenar_nulos()

products.clean_to_csv("products.csv")


#kervin
'''

    *** CLOSED DEALS ***

'''
Closed_Deals = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_closed_deals_dataset.csv")
closed_deals = Preprocesamiento(Closed_Deals)
closed_deals.cambio_tipo_fecha("won_date")
closed_deals.reemplazo_str("business_segment")
closed_deals.reemplazo_str("lead_type")

closed_deals.clean_to_csv("closed_deals.csv")

'''

    *** CUSTOMERS ***

'''
Customers = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_customers_dataset.csv")
customers = Preprocesamiento(Customers)
customers.drop_columna("customer_unique_id")
customers.clean_to_csv("customers.csv")

'''

    *** PAYMENTS ***

'''
Payments = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_order_payments_dataset.csv")
payments = Preprocesamiento(Payments)
payments.reemplazo_str_regex("payment_type")
payments.clean_to_csv("payments.csv")


'''

    *** CATEGORY NAME ***

'''
Category_Name = pd.read_csv("../Proyecto_Final_OLIST/datasets/product_category_name_translation.csv")
category_name = Preprocesamiento(Category_Name)
category_name.reemplazo_str_regex("product_category_name")
category_name.reemplazo_str_regex("product_category_name_english")
category_name.clean_to_csv("category_name_translation.csv")

#lautaro
'''

    *** GEOLOCATION ***

'''

Geolocation = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_geolocation_dataset.csv")
geolocation = Preprocesamiento(Geolocation)

itabat?? = Geolocation['geolocation_city'] == 'itabatan'
# Correccion nombre ciudad para posibles errores outliers
Geolocation.loc[itabat??, 'geolocation_city'] = 'itabat??'

#Mascaras puntos extremos Brasil
# Northern latitude point
LatitudeN = Geolocation['geolocation_lat'] > (5.269582)
# Southest latitude point
LatitudeS = Geolocation['geolocation_lat'] < (-33.750936)
# Eastest longitude point
LongitudeE = Geolocation['geolocation_lng'] > (-34.793015)
# Westest longitude point
LongitudeW = Geolocation['geolocation_lng'] < (-73.98306)

#For wrong north points
geolocator = Nominatim(user_agent="burseselautaro@gmail.com")


index = 0
for i in Geolocation.loc[LatitudeN, 'geolocation_lat']:
    position = Geolocation.loc[LatitudeN, 'geolocation_lat'].index[index]
    Geolocation.loc[position, 'geolocation_lat'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).latitude
    Geolocation.loc[position, 'geolocation_lng'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).longitude
    index += 1
    pass

#For wrong south points
index = 0
for i in Geolocation.loc[LatitudeS, 'geolocation_lat']:
    position = Geolocation.loc[LatitudeS, 'geolocation_lat'].index[index]
    Geolocation.loc[position, 'geolocation_lat'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).latitude
    Geolocation.loc[position, 'geolocation_lng'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).longitude
    index += 1
    pass

#For wrong east points
index = 0
for i in Geolocation.loc[LongitudeE, 'geolocation_lng']:
    position = Geolocation.loc[LongitudeE, 'geolocation_lat'].index[index]
    Geolocation.loc[position, 'geolocation_lat'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).latitude
    Geolocation.loc[position, 'geolocation_lng'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).longitude
    index += 1
    pass

#For wrong west points
index = 0
for i in Geolocation.loc[LongitudeW, 'geolocation_lng']:
    position = Geolocation.loc[LongitudeW, 'geolocation_lat'].index[index]
    Geolocation.loc[position, 'geolocation_lat'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).latitude
    Geolocation.loc[position, 'geolocation_lng'] = geolocator.geocode(f"{Geolocation.loc[position, 'geolocation_city']}, Brasil", timeout=3).longitude
    index += 1
    pass

geolocation.clean_to_csv("geolocation.csv")

'''

    *** MARKETING ***

'''

Marketing = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_marketing_qualified_leads_dataset.csv")
marketing = Preprocesamiento(Marketing)

marketing.unificar_criterio('origin', 'unknown', 'other')
marketing.unificar_criterio('origin', 'other_publicities', 'other')

marketing.cambio_tipo_fecha('first_contact_date')

marketing.clean_to_csv('marketing.csv')

'''

    *** REVIEWS ***

'''
Reviews = pd.read_csv("../Proyecto_Final_OLIST/datasets/olist_order_reviews_dataset.csv")
reviews = Preprocesamiento(Reviews)

reviews.cambio_tipo_fecha('review_creation_date')
reviews.cambio_tipo_fecha('review_answer_timestamp')

reviews.completar_nulos('review_comment_title', 'Sin Dato')
reviews.completar_nulos('review_comment_message', 'Sin Dato')

reviews.clean_to_csv('reviews.csv')


print("datasets creados!!!")
